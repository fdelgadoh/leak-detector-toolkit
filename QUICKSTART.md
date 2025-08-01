# Quick Start Guide

Get up and running with the Leak Detector Toolkit in 5 minutes!

## Prerequisites

- Python 3.7+
- Tesseract OCR (for image analysis)

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/fdelgadoh/leak-detector-toolkit.git
cd leak-detector-toolkit
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install Tesseract**:
```bash
# Ubuntu/Debian
sudo apt install tesseract-ocr

# Arch Linux
sudo pacman -S tesseract tesseract-data-eng tesseract-data-spa
set -gx TESSDATA_PREFIX /usr/share/tessdata

# macOS
brew install tesseract

# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
```

## Quick Usage

### 1. Office Document Analysis

**For custom patterns**:
```bash
# Copy the template
cp office_analyzer_template.py my_search.py

# Edit the pattern in my_search.py
# Change: exact_pattern = r'\b(your_pattern_here)\b'
# To: exact_pattern = r'\b(confidential|secret)\b'

# Run the search
python my_search.py
```

**For Jetsmart-specific search**:
```bash
python extract_jetsmart_office.py
```

### 2. Image Analysis

**For custom patterns**:
```bash
# Copy the template
cp image_analyzer_template.py my_image_search.py

# Edit the pattern in my_image_search.py
# Change: combined_pattern = f'({pattern1}|{pattern2})'
# To: combined_pattern = r'\b[A-Za-z0-9]{6}\b'

# Run the search
python my_image_search.py
```

**For PNR/JetSmart search**:
```bash
python extract_jetsmart_png.py
```

## Configuration

### Directory Structure
```
leak-detector-toolkit/
├── doc_office_descargados/    # Put Office files here
├── imagenes_descargadas/      # Put images here
├── office_analyzer_template.py
├── image_analyzer_template.py
└── extract_jetsmart_*.py
```

### Common Patterns

**Email addresses**:
```python
exact_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```

**Phone numbers**:
```python
exact_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
```

**Credit cards**:
```python
exact_pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
```

**Custom keywords**:
```python
exact_pattern = r'\b(keyword1|keyword2|keyword3)\b'
```

## Output

Results are saved to CSV files:
- `office_results.csv` - Office document analysis results
- `image_results.csv` - Image analysis results
- `jetsmart_office_results.csv` - Jetsmart office results
- `pnr_results.csv` - PNR/JetSmart image results

## Troubleshooting

**Tesseract not found**:
```python
# Update path in script
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux
```

**Import errors**:
```bash
pip install --upgrade -r requirements.txt
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [examples/](examples/) for more pattern examples
- Review [INSTALL.md](INSTALL.md) for complete installation guide 