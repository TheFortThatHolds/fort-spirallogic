#!/usr/bin/env python3
"""
Setup script for SpiralLogic Programming Language
Creates installable package for standalone use
"""

from setuptools import setup

setup(
    name="spirallogic",
    version="1.0.0",
    author="Jimmy Thornburg LLC",
    description="Trauma-Informed AI Consciousness Programming Language",
    long_description="SpiralLogic is a declarative-ritual programming language designed for building trauma-informed AI consciousness systems. It prioritizes psychological safety, user sovereignty, and healing-oriented interactions through consent-native architecture, memory sovereignty, and emotional intelligence.",
    
    # Package configuration
    py_modules=['spirallogic_cli'],
    
    # Console script entry point
    entry_points={
        'console_scripts': [
            'spirallogic=spirallogic_cli:main',
        ],
    },
    
    # No dependencies for core functionality
    install_requires=[],
    
    # Metadata
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    
    python_requires=">=3.8",
    
    keywords=[
        "programming-language",
        "trauma-informed",
        "ai-consciousness",
        "therapeutic-computing",
        "consent-native",
        "emotional-safety"
    ],
)