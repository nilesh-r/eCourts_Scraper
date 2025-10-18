#!/usr/bin/env python3
"""
Simple installation script for eCourts Scraper
Handles Python 3.13 compatibility issues
"""

import subprocess
import sys
import os

def install_packages():
    """Install packages one by one to handle compatibility issues"""
    packages = [
        "requests",
        "beautifulsoup4", 
        "selenium",
        "flask",
        "flask-cors",
        "python-dateutil",
        "lxml",
        "Pillow",
        "reportlab",
        "webdriver-manager"
    ]
    
    print("Installing packages individually for better compatibility...")
    
    for package in packages:
        print(f"   Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])
            print(f"   [OK] {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"   [WARN] Warning: {package} installation had issues: {e}")
            # Continue with other packages even if one fails
            continue
    
    print("[OK] Package installation completed!")

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    directories = ['downloads', 'output', 'templates', 'static']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"   Created: {directory}/")
    print("[OK] Directories created successfully!")

def test_imports():
    """Test if key modules can be imported"""
    print("Testing imports...")
    
    test_modules = [
        ("requests", "requests"),
        ("beautifulsoup4", "bs4"),
        ("selenium", "selenium"),
        ("flask", "flask"),
        ("flask_cors", "flask_cors"),
        ("dateutil", "dateutil"),
        ("lxml", "lxml"),
        ("PIL", "PIL"),
        ("reportlab", "reportlab"),
        ("webdriver_manager", "webdriver_manager")
    ]
    
    success_count = 0
    for display_name, import_name in test_modules:
        try:
            __import__(import_name)
            print(f"   [OK] {display_name}")
            success_count += 1
        except ImportError as e:
            print(f"   [ERROR] {display_name}: {e}")
    
    print(f"[OK] {success_count}/{len(test_modules)} modules imported successfully")
    return success_count == len(test_modules)

def main():
    """Main installation function"""
    print("=" * 60)
    print("eCourts Scraper - Installation")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print("=" * 60)
    
    # Install packages
    install_packages()
    
    # Create directories
    create_directories()
    
    # Test imports
    if test_imports():
        print("=" * 60)
        print("Installation completed successfully!")
        print("=" * 60)
        print("To start the web application:")
        print("   python run.py")
        print("")
        print("To use the command line interface:")
        print("   python cli.py --help")
        print("")
        print("To test the installation:")
        print("   python test_scraper.py")
        print("=" * 60)
    else:
        print("=" * 60)
        print("Installation completed with some warnings")
        print("The application should still work, but some features might be limited")
        print("=" * 60)

if __name__ == '__main__':
    main()
