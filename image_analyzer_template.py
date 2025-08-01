import os
import re
import pytesseract
from PIL import Image
import pandas as pd
from pathlib import Path

# =============================================================================
# CONFIGURATION SECTION - MODIFY THESE SETTINGS AS NEEDED
# =============================================================================

# Path to Tesseract executable - UPDATE THIS PATH FOR YOUR SYSTEM
# Common paths:
# - Ubuntu/Debian: '/usr/bin/tesseract'
# - macOS: '/usr/local/bin/tesseract'
# - Windows: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Directory containing images - use relative path
image_dir = 'imagenes_descargadas'  # Target directory
output_csv = 'image_results.csv'  # Output CSV file

# =============================================================================
# PATTERN CONFIGURATION - MODIFY THIS SECTION FOR YOUR SEARCH PATTERNS
# =============================================================================

# Regular expression for your custom patterns
# Examples:
# - Email addresses: r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# - Phone numbers: r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
# - Credit cards: r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
# - Social Security: r'\b\d{3}-\d{2}-\d{4}\b'
# - PNR codes: r'\b[A-Za-z0-9]{6}\b'
# - Custom keywords: r'\b(keyword1|keyword2|keyword3)\b'

# You can combine multiple patterns using the | operator
pattern1 = r'\b(your_first_pattern_here)\b'
pattern2 = r'\b(your_second_pattern_here)\b'
combined_pattern = f'({pattern1}|{pattern2})'

# =============================================================================
# END CONFIGURATION SECTION
# =============================================================================

# List to store results
results = []

def preprocess_image(image_path):
    """
    Preprocess image for better OCR accuracy
    Modify this function to adjust image processing parameters
    """
    img = Image.open(image_path)
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Increase contrast (adjust the enhancement factor as needed)
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Increase contrast by factor of 2
    
    # Optional: Add more preprocessing steps here
    # - Resize image for better OCR
    # - Apply filters
    # - Adjust brightness
    
    return img

def main():
    """Main function with error handling"""
    
    # Check if directory exists
    if not os.path.exists(image_dir):
        print(f"Directory {image_dir} not found!")
        print("Please update the 'image_dir' variable in the configuration section.")
        return
    
    # Check if Tesseract is available
    try:
        pytesseract.get_tesseract_version()
        print(f"Tesseract version: {pytesseract.get_tesseract_version()}")
    except Exception as e:
        print(f"Error: Tesseract not found or not properly configured.")
        print(f"Please install Tesseract and update the 'tesseract_cmd' path.")
        print(f"Error details: {e}")
        return
    
    # Process each image in the directory and subdirectories
    # Use a comprehensive pattern to catch all image files
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']
    image_files = []
    
    try:
        for ext in image_extensions:
            image_files.extend(Path(image_dir).rglob(ext))
    except Exception as e:
        print(f"Error scanning directory: {e}")
        return

    print(f"Found {len(image_files)} image files to process")
    print(f"Search pattern: {combined_pattern}")
    
    # Process files with progress tracking
    for i, image_file in enumerate(image_files, 1):
        try:
            print(f"Processing image {i}/{len(image_files)}: {image_file.name}")
            
            # Get relative path excluding the target directory
            relative_path = str(image_file.relative_to(image_dir))
            
            # Preprocess the image
            img = preprocess_image(image_file)
            
            # Perform OCR
            text = pytesseract.image_to_string(img)
            
            # Find patterns in the extracted text
            matches = re.findall(combined_pattern, text)
            
            # Store results
            for match in matches:
                # Handle tuple output from regex groups (take the first non-empty group)
                if isinstance(match, tuple):
                    match = next((m for m in match if m), '')
                results.append({
                    'Image': image_file.name,
                    'PATH': relative_path,
                    'Match': match
                })
            
            print(f"  Found {len(matches)} matches")
            
        except Exception as e:
            print(f"Error processing {image_file}: {e}")
            continue

    # Save results to CSV
    try:
        if results:
            df = pd.DataFrame(results)
            df.to_csv(output_csv, index=False, encoding='utf-8')
            print(f"\nResults saved to {output_csv}")
            print(f"Total matches found: {len(results)}")
            
            # Print summary
            print("\nSummary:")
            unique_images = df['Image'].nunique()
            unique_matches = df['Match'].nunique()
            print(f"  Images processed: {len(image_files)}")
            print(f"  Images with matches: {unique_images}")
            print(f"  Unique matches found: {unique_matches}")
            
            # Show top matches
            if len(results) > 0:
                print("\nTop matches:")
                match_counts = df['Match'].value_counts().head(10)
                for match, count in match_counts.items():
                    print(f"  '{match}': {count} occurrences")
        else:
            print("No matches found in any images.")
    except Exception as e:
        print(f"Error saving results: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}") 