import os
import re
import pandas as pd
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET
import sys

# For .docx, .xlsx, .pptx files
try:
    from docx import Document
    DOCX_AVAILABLE = True
except ImportError:
    print("python-docx not installed. Install with: pip install python-docx")
    DOCX_AVAILABLE = False

# For .xls files (legacy format)
try:
    import xlrd
    XLRD_AVAILABLE = True
except ImportError:
    print("xlrd not installed. Install with: pip install xlrd")
    XLRD_AVAILABLE = False

# =============================================================================
# CONFIGURATION SECTION - MODIFY THESE SETTINGS AS NEEDED
# =============================================================================

# Directory containing Office files - use relative path
office_dir = 'doc_office_descargados'  # Target directory
output_csv = 'office_results.csv'  # Output CSV file
skipped_files_log = 'skipped_large_files.txt'  # Log file for skipped files

# Maximum file size in bytes (20MB = 20 * 1024 * 1024)
MAX_FILE_SIZE = 20 * 1024 * 1024

# =============================================================================
# PATTERN CONFIGURATION - MODIFY THIS SECTION FOR YOUR SEARCH PATTERNS
# =============================================================================

# Regular expression for your custom patterns
# Examples:
# - Email addresses: r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# - Phone numbers: r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
# - Credit cards: r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
# - Social Security: r'\b\d{3}-\d{2}-\d{4}\b'
# - Custom keywords: r'\b(keyword1|keyword2|keyword3)\b'

exact_pattern = r'\b(your_pattern_here)\b'

# =============================================================================
# END CONFIGURATION SECTION
# =============================================================================

# List to store results
results = []
skipped_files = []

def get_file_size_mb(file_path):
    """Get file size in MB"""
    try:
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return size_bytes, size_mb
    except OSError:
        return 0, 0

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

def extract_text_from_docx(file_path):
    """Extract text from .docx files"""
    if not DOCX_AVAILABLE:
        return ""
    
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

def extract_text_from_xlsx(file_path):
    """Extract text from .xlsx files"""
    try:
        # Open the Excel file as a ZIP archive
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            # Read the shared strings file
            shared_strings = {}
            try:
                with zip_file.open('xl/sharedStrings.xml') as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    for i, si in enumerate(root.findall('.//{*}si')):
                        text_elements = si.findall('.//{*}t')
                        shared_strings[i] = ' '.join([t.text or '' for t in text_elements])
            except KeyError:
                pass  # No shared strings file
            
            # Read all worksheets
            text = ""
            for sheet_name in zip_file.namelist():
                if sheet_name.startswith('xl/worksheets/sheet') and sheet_name.endswith('.xml'):
                    try:
                        with zip_file.open(sheet_name) as f:
                            tree = ET.parse(f)
                            root = tree.getroot()
                            
                            # Extract text from cells
                            for row in root.findall('.//{*}row'):
                                for cell in row.findall('.//{*}c'):
                                    # Get cell value
                                    value_elem = cell.find('.//{*}v')
                                    if value_elem is not None and value_elem.text:
                                        cell_value = value_elem.text
                                        
                                        # Check if it's a shared string reference
                                        if cell.get('t') == 's':
                                            try:
                                                cell_value = shared_strings[int(cell_value)]
                                            except (KeyError, ValueError):
                                                pass
                                        
                                        text += str(cell_value) + " "
                    except Exception as e:
                        print(f"Error reading sheet {sheet_name}: {e}")
                        continue
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

def extract_text_from_pptx(file_path):
    """Extract text from .pptx files"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            text = ""
            # Read all slide files
            for slide_name in zip_file.namelist():
                if slide_name.startswith('ppt/slides/slide') and slide_name.endswith('.xml'):
                    try:
                        with zip_file.open(slide_name) as f:
                            tree = ET.parse(f)
                            root = tree.getroot()
                            
                            # Extract text from text elements
                            for text_elem in root.findall('.//{*}t'):
                                if text_elem.text:
                                    text += text_elem.text + " "
                    except Exception as e:
                        print(f"Error reading slide {slide_name}: {e}")
                        continue
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

def extract_text_from_xls(file_path):
    """Extract text from .xls files (legacy format)"""
    if not XLRD_AVAILABLE:
        return ""
    
    try:
        workbook = xlrd.open_workbook(file_path)
        text = ""
        for sheet_name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(sheet_name)
            for row_idx in range(sheet.nrows):
                for col_idx in range(sheet.ncols):
                    cell_value = sheet.cell_value(row_idx, col_idx)
                    if cell_value:
                        text += str(cell_value) + " "
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

def extract_text_from_office_file(file_path):
    """Extract text from Office files based on file extension"""
    file_ext = file_path.suffix.lower()
    
    if file_ext == '.docx':
        return extract_text_from_docx(file_path)
    elif file_ext == '.xlsx':
        return extract_text_from_xlsx(file_path)
    elif file_ext == '.pptx':
        return extract_text_from_pptx(file_path)
    elif file_ext == '.xls':
        return extract_text_from_xls(file_path)
    elif file_ext == '.doc':
        print(f"Skipping {file_path}: .doc files not supported in this version")
        return ""
    else:
        print(f"Unsupported file format: {file_ext}")
        return ""

def main():
    """Main function with error handling"""
    global results, skipped_files
    
    # Check if directory exists
    if not os.path.exists(office_dir):
        print(f"Directory {office_dir} not found!")
        print("Please update the 'office_dir' variable in the configuration section.")
        return
    
    # Process each Office file in the directory and subdirectories
    office_extensions = ['*.docx', '*.xls', '*.xlsx', '*.pptx']
    office_files = []
    
    try:
        for ext in office_extensions:
            office_files.extend(Path(office_dir).rglob(ext))
    except Exception as e:
        print(f"Error scanning directory: {e}")
        return

    print(f"Found {len(office_files)} Office files to process")
    print(f"Maximum file size limit: {format_file_size(MAX_FILE_SIZE)}")
    print(f"Search pattern: {exact_pattern}")
    
    # Process files with progress tracking
    for i, office_file in enumerate(office_files, 1):
        try:
            # Check file size before processing
            file_size_bytes, file_size_mb = get_file_size_mb(office_file)
            
            if file_size_bytes > MAX_FILE_SIZE:
                print(f"Skipping file {i}/{len(office_files)}: {office_file.name} (Size: {format_file_size(file_size_bytes)})")
                skipped_files.append({
                    'file': str(office_file),
                    'size_bytes': file_size_bytes,
                    'size_mb': file_size_mb,
                    'reason': 'File too large'
                })
                continue
            
            print(f"Processing file {i}/{len(office_files)}: {office_file.name} (Size: {format_file_size(file_size_bytes)})")
            
            # Get relative path excluding the target directory
            relative_path = str(office_file.relative_to(office_dir))
            
            # Extract text from the Office file
            text = extract_text_from_office_file(office_file)
            
            if text:
                # Find exact patterns in the extracted text
                matches = re.findall(exact_pattern, text, re.IGNORECASE)
                
                # Store results
                for match in matches:
                    results.append({
                        'File': office_file.name,
                        'PATH': relative_path,
                        'Match': match,
                        'File_Type': office_file.suffix.lower(),
                        'File_Size_MB': round(file_size_mb, 2)
                    })
                
                print(f"  Found {len(matches)} matches")
            else:
                print(f"  No text extracted")
            
        except Exception as e:
            print(f"Error processing {office_file}: {e}")
            skipped_files.append({
                'file': str(office_file),
                'size_bytes': get_file_size_mb(office_file)[0],
                'size_mb': get_file_size_mb(office_file)[1],
                'reason': f'Error: {str(e)}'
            })
            continue  # Continue with next file instead of crashing

    # Save results to CSV
    try:
        if results:
            df = pd.DataFrame(results)
            df.to_csv(output_csv, index=False, encoding='utf-8')
            print(f"\nResults saved to {output_csv}")
            print(f"Total matches found: {len(results)}")
            
            # Print summary by file type
            print("\nSummary by file type:")
            summary = df.groupby('File_Type').size()
            for file_type, count in summary.items():
                print(f"  {file_type}: {count} matches")
        else:
            print("No matches found in any Office files.")
    except Exception as e:
        print(f"Error saving results: {e}")

    # Save skipped files log
    try:
        if skipped_files:
            with open(skipped_files_log, 'w', encoding='utf-8') as f:
                f.write("Skipped Files Report\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Total files skipped: {len(skipped_files)}\n")
                f.write(f"Maximum file size limit: {format_file_size(MAX_FILE_SIZE)}\n\n")
                
                # Group by reason
                by_reason = {}
                for file_info in skipped_files:
                    reason = file_info['reason']
                    if reason not in by_reason:
                        by_reason[reason] = []
                    by_reason[reason].append(file_info)
                
                for reason, files in by_reason.items():
                    f.write(f"\n{reason} ({len(files)} files):\n")
                    f.write("-" * 30 + "\n")
                    for file_info in files:
                        f.write(f"  {file_info['file']} - {format_file_size(file_info['size_bytes'])}\n")
                
                # Summary statistics
                total_size_skipped = sum(f['size_bytes'] for f in skipped_files)
                f.write(f"\n\nSummary:\n")
                f.write(f"Total size of skipped files: {format_file_size(total_size_skipped)}\n")
                f.write(f"Average size of skipped files: {format_file_size(total_size_skipped // len(skipped_files))}\n")
            
            print(f"\nSkipped files report saved to {skipped_files_log}")
            print(f"Total files skipped: {len(skipped_files)}")
            total_size_skipped = sum(f['size_bytes'] for f in skipped_files)
            print(f"Total size of skipped files: {format_file_size(total_size_skipped)}")
        else:
            print("\nNo files were skipped.")
    except Exception as e:
        print(f"Error saving skipped files log: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1) 