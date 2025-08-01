# Leak Detector Toolkit

A comprehensive toolkit for detecting sensitive information leaks in Office documents and images through pattern matching and OCR analysis.

## 🚀 Features

### Office Document Analyzer
- **Multi-format Support**: Analyzes `.docx`, `.xlsx`, `.pptx`, `.xls` files
- **Pattern Matching**: Customizable regex patterns for sensitive data detection
- **Large File Handling**: Configurable file size limits with detailed logging
- **Comprehensive Output**: CSV reports with file metadata and match details

### Image Analyzer
- **OCR Integration**: Uses Tesseract for text extraction from images
- **Multi-format Support**: Processes `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`
- **Image Preprocessing**: Automatic contrast enhancement for better OCR accuracy
- **Pattern Detection**: Customizable patterns for sensitive information

## 📋 Requirements

### System Dependencies
- **Python 3.7+**
- **Tesseract OCR** (for image analysis)

### Python Dependencies
```
pandas>=1.3.0
python-docx>=0.8.11
xlrd>=2.0.1
Pillow>=8.0.0
pytesseract>=0.3.8
```

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/fdelgadoh/leak-detector-toolkit.git
cd leak-detector-toolkit
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install Tesseract OCR**:

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**macOS**:
```bash
brew install tesseract
```

**Windows**:
Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

## 📖 Usage

### Office Document Analysis

1. **Use the template for custom patterns**:
```bash
python office_analyzer_template.py
```

2. **Or use the pre-configured Jetsmart extractor**:
```bash
python extract_jetsmart_office.py
```

### Image Analysis

1. **Use the template for custom patterns**:
```bash
python image_analyzer_template.py
```

2. **Or use the pre-configured PNR extractor**:
```bash
python extract_jetsmart_png.py
```

## ⚙️ Configuration

### Office Analyzer Settings
- `office_dir`: Directory containing Office files (default: `doc_office_descargados`)
- `output_csv`: Output CSV filename (default: `office_results.csv`)
- `MAX_FILE_SIZE`: Maximum file size limit in bytes (default: 20MB)
- `exact_pattern`: Regex pattern for sensitive data detection

### Image Analyzer Settings
- `image_dir`: Directory containing images (default: `imagenes_descargadas`)
- `output_csv`: Output CSV filename (default: `image_results.csv`)
- `tesseract_cmd`: Path to Tesseract executable
- `combined_pattern`: Regex pattern for sensitive data detection

## 📊 Output Format

### Office Analysis Results
| Column | Description |
|--------|-------------|
| File | Name of the Office file |
| PATH | Relative path within the directory |
| Match | The specific pattern found |
| File_Type | File extension |
| File_Size_MB | File size in megabytes |

### Image Analysis Results
| Column | Description |
|--------|-------------|
| Image | Name of the image file |
| PATH | Relative path within the directory |
| Match | The specific pattern found |

## 🔧 Customization

### Creating Custom Patterns

1. **Copy the template files**:
```bash
cp office_analyzer_template.py my_office_analyzer.py
cp image_analyzer_template.py my_image_analyzer.py
```

2. **Modify the pattern variables**:
```python
# For Office files
exact_pattern = r'\b(your_pattern_here)\b'

# For images
combined_pattern = r'\b(your_pattern_here)\b'
```

3. **Adjust other settings as needed**:
- File size limits
- Output filenames
- Directory paths

## 🐛 Troubleshooting

### Common Issues

**Tesseract not found**:
- Ensure Tesseract is installed and in your PATH
- Update the `tesseract_cmd` path in the script

**Import errors**:
- Install missing packages: `pip install -r requirements.txt`
- For Windows .doc files: `pip install pywin32`

**Large file processing**:
- Adjust `MAX_FILE_SIZE` in the script
- Check the `skipped_large_files.txt` log

**OCR accuracy**:
- Ensure images are clear and high-resolution
- Adjust preprocessing parameters in the script

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## ⚠️ Disclaimer

This tool is designed for legitimate security research and data protection purposes. Users are responsible for ensuring compliance with applicable laws and regulations when using this software.

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the template files for examples 