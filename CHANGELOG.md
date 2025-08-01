# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-01-XX

### Added
- **LibreOffice/OpenDocument Support**: Added support for LibreOffice document formats
  - `.odt` (OpenDocument Text) - LibreOffice Writer documents
  - `.ods` (OpenDocument Spreadsheet) - LibreOffice Calc spreadsheets  
  - `.odp` (OpenDocument Presentation) - LibreOffice Impress presentations
  - `.odg` (OpenDocument Drawing) - LibreOffice Draw drawings
- XML-based text extraction for OpenDocument formats
- Comprehensive error handling for LibreOffice files
- Updated documentation to reflect new format support

## [1.0.0] - 2025-08-01

### Added
- Initial release of Leak Detector Toolkit
- Office Document Analyzer with support for `.docx`, `.xlsx`, `.pptx`, `.xls` files
- Image Analyzer with OCR support using Tesseract
- Template files for custom pattern configuration
- Comprehensive documentation in English and Spanish
- File size limits and error handling
- CSV output with detailed metadata
- Skipped files logging and reporting

### Features
- **Office Analyzer**:
  - Multi-format document support
  - Configurable regex patterns
  - Large file handling with size limits
  - Detailed progress tracking
  - Comprehensive error handling

- **Image Analyzer**:
  - OCR text extraction from images
  - Multi-format image support
  - Image preprocessing for better accuracy
  - Customizable search patterns
  - Progress tracking and error handling

### Technical Details
- Python 3.7+ compatibility
- Cross-platform support (Windows, macOS, Linux)
- Modular design for easy customization
- Comprehensive error handling and logging
- MIT License for open source use

### Documentation
- Complete README files in English and Spanish
- Installation instructions for all platforms
- Usage examples and configuration guides
- Troubleshooting section
- Template files with detailed comments 