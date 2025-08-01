# Installation Guide

This guide provides detailed installation instructions for the Leak Detector Toolkit on different operating systems.

## Prerequisites

### System Requirements
- **Python 3.7 or higher**
- **Tesseract OCR** (for image analysis)
- **Git** (for cloning the repository)

### Python Dependencies
The toolkit requires the following Python packages:
- `pandas>=1.3.0`
- `python-docx>=0.8.11`
- `xlrd>=2.0.1`
- `Pillow>=8.0.0`
- `pytesseract>=0.3.8`

## Installation Methods

### Method 1: Clone and Install (Recommended)

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/leak-detector-toolkit.git
cd leak-detector-toolkit
```

2. **Create a virtual environment** (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install Tesseract OCR** (see platform-specific instructions below)

### Method 2: Using pip (if published to PyPI)

```bash
pip install leak-detector-toolkit
```

## Platform-Specific Tesseract Installation

### Ubuntu/Debian Linux

```bash
# Update package list
sudo apt update

# Install Tesseract
sudo apt install tesseract-ocr

# Install additional language packs (optional)
sudo apt install tesseract-ocr-spa  # Spanish
sudo apt install tesseract-ocr-fra  # French
sudo apt install tesseract-ocr-deu  # German

# Verify installation
tesseract --version
```

### CentOS/RHEL/Fedora

```bash
# CentOS/RHEL 7/8
sudo yum install tesseract

# Fedora
sudo dnf install tesseract

# Verify installation
tesseract --version
```

### macOS

Using Homebrew:
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Tesseract
brew install tesseract

# Verify installation
tesseract --version
```

Using MacPorts:
```bash
sudo port install tesseract
```

### Windows

1. **Download Tesseract**:
   - Go to [UB-Mannheim Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki)
   - Download the latest installer for your Windows version (32-bit or 64-bit)

2. **Install Tesseract**:
   - Run the downloaded installer
   - Choose installation directory (default: `C:\Program Files\Tesseract-OCR\`)
   - Select additional language packs if needed
   - Complete the installation

3. **Add to PATH** (if not done automatically):
   - Open System Properties → Advanced → Environment Variables
   - Add `C:\Program Files\Tesseract-OCR\` to the PATH variable

4. **Verify installation**:
```cmd
tesseract --version
```

### Docker (Alternative)

If you prefer using Docker:

```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY . .

# Default command
CMD ["python", "office_analyzer_template.py"]
EOF

# Build and run
docker build -t leak-detector-toolkit .
docker run -v $(pwd):/app leak-detector-toolkit
```

## Verification

After installation, verify that everything is working:

1. **Check Python dependencies**:
```bash
python -c "import pandas, docx, xlrd, PIL, pytesseract; print('All dependencies installed successfully!')"
```

2. **Check Tesseract**:
```bash
tesseract --version
```

3. **Test the toolkit**:
```bash
# Test office analyzer
python office_analyzer_template.py --help

# Test image analyzer
python image_analyzer_template.py --help
```

## Configuration

### Tesseract Path Configuration

Update the Tesseract path in your scripts based on your system:

```python
# Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# macOS
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
```

### Environment Variables (Optional)

You can set environment variables for easier configuration:

```bash
# Linux/macOS
export TESSERACT_PATH="/usr/bin/tesseract"
export OFFICE_DIR="documents/"
export IMAGE_DIR="images/"

# Windows
set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
set OFFICE_DIR=documents\
set IMAGE_DIR=images\
```

## Troubleshooting

### Common Issues

**Tesseract not found**:
```bash
# Find Tesseract installation
which tesseract  # Linux/macOS
where tesseract  # Windows

# Update path in script if different
```

**Import errors**:
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Check Python version
python --version
```

**Permission errors**:
```bash
# Linux/macOS: Use sudo for system-wide installation
sudo pip install -r requirements.txt

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows-specific issues**:
- Ensure Visual C++ redistributables are installed
- Use Windows Subsystem for Linux (WSL) as alternative
- Check antivirus software isn't blocking installations

### Getting Help

If you encounter issues:

1. Check the [troubleshooting section](README.md#troubleshooting) in the main README
2. Search existing [GitHub issues](https://github.com/yourusername/leak-detector-toolkit/issues)
3. Create a new issue with:
   - Operating system and version
   - Python version
   - Tesseract version
   - Complete error message
   - Steps to reproduce

## Next Steps

After successful installation:

1. Read the [README.md](README.md) for usage instructions
2. Check the [examples](examples/) directory for pattern examples
3. Start with the template files for custom configurations
4. Review the [changelog](CHANGELOG.md) for latest updates 