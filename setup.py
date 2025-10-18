#!/usr/bin/env python3
"""
Setup script for eCourts Scraper
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    
    # Try the main requirements file first
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("[OK] Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print("Error with specific versions, trying flexible versions...")
        
        # Try the flexible requirements file
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements-py313.txt"])
            print("[OK] Requirements installed successfully with flexible versions!")
            return True
        except subprocess.CalledProcessError as e2:
            print(f"[ERROR] Error installing requirements: {e2}")
            print("Try installing manually: pip install requests beautifulsoup4 selenium flask flask-cors python-dateutil lxml Pillow reportlab webdriver-manager")
            return False

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    directories = ['downloads', 'output', 'templates', 'static']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"   Created: {directory}/")
    print("[OK] Directories created successfully!")

def main():
    """Main setup function"""
    print("=" * 60)
    print("eCourts Scraper Setup")
    print("=" * 60)
    
    # Install requirements
    if not install_requirements():
        print("[ERROR] Setup failed. Please check the error messages above.")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    print("=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("To start the web application:")
    print("   python run.py")
    print("")
    print("To use the command line interface:")
    print("   python cli.py --help")
    print("")
    print("For more information, see README.md")
    print("=" * 60)

if __name__ == '__main__':
    main()
