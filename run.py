#!/usr/bin/env python3
"""
eCourts Scraper - Main Entry Point
Simple script to run the web application
"""

import os
import sys
from app import app

def main():
    """Main entry point for the web application"""
    # Create necessary directories
    directories = ['downloads', 'output', 'templates', 'static']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("=" * 60)
    print("🏛️  eCourts Scraper - Real-time Court Data")
    print("=" * 60)
    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
