# Kit de Herramientas para Detección de Fugas

Un kit completo de herramientas para detectar fugas de información sensible en documentos de Office e imágenes mediante coincidencia de patrones y análisis OCR.

## 🚀 Características

### Analizador de Documentos Office
- **Soporte Multi-formato**: Analiza archivos `.docx`, `.xlsx`, `.pptx`, `.xls`
- **Coincidencia de Patrones**: Patrones regex personalizables para detección de datos sensibles
- **Manejo de Archivos Grandes**: Límites de tamaño de archivo configurables con registro detallado
- **Salida Completa**: Reportes CSV con metadatos de archivos y detalles de coincidencias

### Analizador de Imágenes
- **Integración OCR**: Usa Tesseract para extracción de texto de imágenes
- **Soporte Multi-formato**: Procesa `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`
- **Preprocesamiento de Imágenes**: Mejora automática de contraste para mejor precisión OCR
- **Detección de Patrones**: Patrones personalizables para información sensible

## 📋 Requisitos

### Dependencias del Sistema
- **Python 3.7+**
- **Tesseract OCR** (para análisis de imágenes)

### Dependencias de Python
```
pandas>=1.3.0
python-docx>=0.8.11
xlrd>=2.0.1
Pillow>=8.0.0
pytesseract>=0.3.8
```

## 🛠️ Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/fdelgadoh/leak-detector-toolkit.git
cd leak-detector-toolkit
```

2. **Instalar dependencias de Python**:
```bash
pip install -r requirements.txt
```

3. **Instalar Tesseract OCR**:

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**Arch Linux**:
```bash
sudo pacman -S tesseract
sudo pacman -S tesseract-data-eng
sudo pacman -S tesseract-data-spa
# Establecer variable de entorno para datos de Tesseract
set -gx TESSDATA_PREFIX /usr/share/tessdata
```

**macOS**:
```bash
brew install tesseract
```

**Windows**:
Descargar desde [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

## 📖 Uso

### Análisis de Documentos Office

1. **Usar la plantilla para patrones personalizados**:
```bash
python office_analyzer_template.py
```

2. **O usar el extractor Jetsmart pre-configurado**:
```bash
python extract_jetsmart_office.py
```

### Análisis de Imágenes

1. **Usar la plantilla para patrones personalizados**:
```bash
python image_analyzer_template.py
```

2. **O usar el extractor PNR pre-configurado**:
```bash
python extract_jetsmart_png.py
```

## ⚙️ Configuración

### Configuración del Analizador Office
- `office_dir`: Directorio que contiene archivos Office (predeterminado: `doc_office_descargados`)
- `output_csv`: Nombre del archivo CSV de salida (predeterminado: `office_results.csv`)
- `MAX_FILE_SIZE`: Límite máximo de tamaño de archivo en bytes (predeterminado: 20MB)
- `exact_pattern`: Patrón regex para detección de datos sensibles

### Configuración del Analizador de Imágenes
- `image_dir`: Directorio que contiene imágenes (predeterminado: `imagenes_descargadas`)
- `output_csv`: Nombre del archivo CSV de salida (predeterminado: `image_results.csv`)
- `tesseract_cmd`: Ruta al ejecutable de Tesseract
- `combined_pattern`: Patrón regex para detección de datos sensibles

## 📊 Formato de Salida

### Resultados del Análisis Office
| Columna | Descripción |
|---------|-------------|
| File | Nombre del archivo Office |
| PATH | Ruta relativa dentro del directorio |
| Match | El patrón específico encontrado |
| File_Type | Extensión del archivo |
| File_Size_MB | Tamaño del archivo en megabytes |

### Resultados del Análisis de Imágenes
| Columna | Descripción |
|---------|-------------|
| Image | Nombre del archivo de imagen |
| PATH | Ruta relativa dentro del directorio |
| Match | El patrón específico encontrado |

## 🔧 Personalización

### Crear Patrones Personalizados

1. **Copiar los archivos de plantilla**:
```bash
cp office_analyzer_template.py mi_analizador_office.py
cp image_analyzer_template.py mi_analizador_imagenes.py
```

2. **Modificar las variables de patrón**:
```python
# Para archivos Office
exact_pattern = r'\b(tu_patron_aqui)\b'

# Para imágenes
combined_pattern = r'\b(tu_patron_aqui)\b'
```

3. **Ajustar otras configuraciones según sea necesario**:
- Límites de tamaño de archivo
- Nombres de archivos de salida
- Rutas de directorios

## 🐛 Solución de Problemas

### Problemas Comunes

**Tesseract no encontrado**:
- Asegúrate de que Tesseract esté instalado y en tu PATH
- Actualiza la ruta `tesseract_cmd` en el script

**Errores de importación**:
- Instala paquetes faltantes: `pip install -r requirements.txt`
- Para archivos .doc en Windows: `pip install pywin32`

**Procesamiento de archivos grandes**:
- Ajusta `MAX_FILE_SIZE` en el script
- Revisa el registro `skipped_large_files.txt`

**Precisión OCR**:
- Asegúrate de que las imágenes sean claras y de alta resolución
- Ajusta los parámetros de preprocesamiento en el script

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

1. Haz fork del repositorio
2. Crea una rama de características
3. Haz tus cambios
4. Agrega pruebas si es aplicable
5. Envía un pull request

## ⚠️ Descargo de Responsabilidad

Esta herramienta está diseñada para investigación de seguridad legítima y propósitos de protección de datos. Los usuarios son responsables de asegurar el cumplimiento de las leyes y regulaciones aplicables al usar este software.

## 📞 Soporte

Para problemas y preguntas:
- Abre un issue en GitHub
- Revisa la sección de solución de problemas
- Revisa los archivos de plantilla para ejemplos 