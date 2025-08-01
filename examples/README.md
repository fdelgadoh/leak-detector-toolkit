# Examples

This directory contains example configurations and usage patterns for the Leak Detector Toolkit.

## Pattern Examples

### Common Data Patterns

#### Email Addresses
```python
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```

#### Phone Numbers (US Format)
```python
phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
```

#### Credit Card Numbers
```python
credit_card_pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
```

#### Social Security Numbers (US)
```python
ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
```

#### PNR Codes (6 alphanumeric characters)
```python
pnr_pattern = r'\b[A-Za-z0-9]{6}\b'
```

#### IP Addresses
```python
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
```

#### API Keys (common formats)
```python
api_key_pattern = r'\b[A-Za-z0-9]{32,64}\b'
```

### Custom Keywords

#### Company Names
```python
company_pattern = r'\b(company1|company2|company3)\b'
```

#### Project Codes
```python
project_pattern = r'\b(PRJ|PROJ)-\d{4,6}\b'
```

#### Internal References
```python
internal_ref_pattern = r'\b(INT|REF)-\d{4,8}\b'
```

## Configuration Examples

### Office Analyzer Configuration

```python
# Basic configuration
office_dir = 'documents/'
output_csv = 'results.csv'
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB limit

# Multiple patterns
pattern1 = r'\b(email@company\.com)\b'
pattern2 = r'\b(API_KEY_[A-Z0-9]{32})\b'
exact_pattern = f'({pattern1}|{pattern2})'
```

### Image Analyzer Configuration

```python
# Tesseract path for different systems
# Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# macOS
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Multiple patterns for images
pattern1 = r'\b[A-Za-z0-9]{6}\b'  # PNR codes
pattern2 = r'\b\d{3}-\d{2}-\d{4}\b'  # SSN
combined_pattern = f'({pattern1}|{pattern2})'
```

## Usage Examples

### 1. Basic Office Document Search

```bash
# Copy template
cp office_analyzer_template.py my_office_search.py

# Edit the pattern in my_office_search.py
# exact_pattern = r'\b(confidential|secret|private)\b'

# Run the search
python my_office_search.py
```

### 2. Image OCR Search

```bash
# Copy template
cp image_analyzer_template.py my_image_search.py

# Edit the pattern in my_image_search.py
# combined_pattern = r'\b[A-Za-z0-9]{6}\b'

# Run the search
python my_image_search.py
```

### 3. Combined Search

```bash
# Search for multiple sensitive data types
python office_analyzer_template.py
python image_analyzer_template.py

# Combine results
cat office_results.csv image_results.csv > combined_results.csv
```

## Advanced Patterns

### Complex Regex Patterns

#### Multi-line Credit Card
```python
credit_card_multiline = r'\b\d{4}\s*\d{4}\s*\d{4}\s*\d{4}\b'
```

#### Flexible Phone Numbers
```python
phone_flexible = r'\b(?:\+?1[-.]?)?\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})\b'
```

#### Database Connection Strings
```python
db_connection = r'\b(?:mysql|postgresql|mongodb)://[^\s]+\b'
```

### Pattern Validation

Before using patterns in production, test them with sample data:

```python
import re

# Test pattern
test_pattern = r'\b[A-Za-z0-9]{6}\b'
test_data = "ABC123 DEF456 GHI789"

matches = re.findall(test_pattern, test_data)
print(f"Found matches: {matches}")
```

## Best Practices

1. **Use word boundaries** (`\b`) to avoid partial matches
2. **Test patterns** with sample data before deployment
3. **Start specific** and broaden patterns as needed
4. **Consider false positives** when designing patterns
5. **Use case-insensitive matching** when appropriate
6. **Document patterns** for future reference
7. **Regular expression testing** tools can help validate patterns 