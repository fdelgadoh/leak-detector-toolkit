import os
import re
import pytesseract
from PIL import Image
import pandas as pd
from pathlib import Path

# Path to Tesseract executable for Ubuntu/WSL2
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update if `which tesseract` returns a different path

# Directory containing images - use relative path
image_dir = 'imagenes_descargadas'  # Target directory
output_csv = 'pnr_results.csv'  # Output CSV file

# Regular expression for PNR (6 alphanumeric characters) and JetSmart variations - Change Patterns to desired search
pnr_pattern = r'\b[A-Za-z0-9]{6}\b'
jetsmart_pattern = r'\b[jJ][eE][tT][sS][mM][aA][rR][tT]\b|\b[jJ][eE][tT]-[sS][mM][aA][rR][tT]\b|\b[jJ][eE][tT]\b'
combined_pattern = f'({pnr_pattern}|{jetsmart_pattern})'

# List to store results
results = []

# Function to preprocess image (optional, for better OCR accuracy)
def preprocess_image(image_path):
    img = Image.open(image_path)
    # Convert to grayscale
    img = img.convert('L')
    # Increase contrast (optional, adjust as needed)
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    return img

# Process each image in the directory and subdirectories
# Use a more comprehensive pattern to catch all image files
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']
image_files = []
for ext in image_extensions:
    image_files.extend(Path(image_dir).rglob(ext))

print(f"Found {len(image_files)} image files to process")

for image_file in image_files:
    try:
        # Get relative path excluding the target directory
        relative_path = str(image_file.relative_to(image_dir))
        
        # Preprocess the image
        img = preprocess_image(image_file)
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        # Find PNR codes and JetSmart variations in the extracted text
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
        
        print(f"Processed {relative_path}: Found {len(matches)} matches")
        
    except Exception as e:
        print(f"Error processing {image_file}: {e}")

# Save results to CSV
if results:
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")
    print(f"Total matches found: {len(results)}")
else:
    print("No matches found in any images.") 