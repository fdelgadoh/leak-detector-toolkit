#!/usr/bin/env python3
"""
Setup script for Leak Detector Toolkit
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="leak-detector-toolkit",
    version="1.0.0",
    author="Leak Detector Toolkit Team",
    author_email="your-email@example.com",
    description="A comprehensive toolkit for detecting sensitive information leaks in Office documents and images",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/leak-detector-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "leak-detector-office=leak_detector_toolkit.office_analyzer:main",
            "leak-detector-image=leak_detector_toolkit.image_analyzer:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="security, data-leak, ocr, document-analysis, pattern-matching",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/leak-detector-toolkit/issues",
        "Source": "https://github.com/yourusername/leak-detector-toolkit",
        "Documentation": "https://github.com/yourusername/leak-detector-toolkit#readme",
    },
) 