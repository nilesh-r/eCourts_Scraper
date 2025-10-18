#!/usr/bin/env python3
"""
Test script for eCourts Scraper
Simple tests to verify the scraper functionality
"""

import sys
import os
from datetime import datetime
from ecourts_scraper import ECourtsScraper

def test_basic_functionality():
    """Test basic scraper functionality"""
    print("Testing eCourts Scraper...")
    
    scraper = ECourtsScraper()
    
    # Test 1: Get states
    print("1. Testing state fetching...")
    try:
        states = scraper.get_states()
        if states:
            print(f"   [OK] Found {len(states)} states")
        else:
            print("   [WARN] No states found (this might be normal if the website is down)")
    except Exception as e:
        print(f"   [ERROR] Error fetching states: {e}")
    
    # Test 2: Test Delhi cause list
    print("2. Testing Delhi cause list...")
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        delhi_cause_list = scraper.get_delhi_cause_list(today)
        if delhi_cause_list:
            print(f"   [OK] Found {len(delhi_cause_list)} cases in Delhi cause list")
        else:
            print("   [WARN] No cases found in Delhi cause list (this might be normal)")
    except Exception as e:
        print(f"   [ERROR] Error fetching Delhi cause list: {e}")
    
    # Test 3: Test file operations
    print("3. Testing file operations...")
    try:
        test_data = {"test": "data", "timestamp": datetime.now().isoformat()}
        result = scraper.save_results(test_data, "test_output.json")
        if result and os.path.exists(result):
            print(f"   [OK] File operations working: {result}")
            os.remove(result)  # Clean up
        else:
            print("   [ERROR] File operations failed")
    except Exception as e:
        print(f"   [ERROR] Error testing file operations: {e}")
    
    print("Basic functionality test completed!")

def test_web_interface():
    """Test if web interface can start"""
    print("\nTesting web interface...")
    try:
        from app import app
        print("   [OK] Web interface imports successfully")
        print("   [INFO] To test the full web interface, run: python run.py")
    except Exception as e:
        print(f"   [ERROR] Error importing web interface: {e}")

def test_cli_interface():
    """Test if CLI interface works"""
    print("\nTesting CLI interface...")
    try:
        import cli
        print("   [OK] CLI interface imports successfully")
        print("   [INFO] To test CLI, run: python cli.py --help")
    except Exception as e:
        print(f"   [ERROR] Error importing CLI interface: {e}")

def main():
    """Main test function"""
    print("=" * 60)
    print("eCourts Scraper Test Suite")
    print("=" * 60)
    
    test_basic_functionality()
    test_web_interface()
    test_cli_interface()
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
    print("If you see any [ERROR] messages above, please check:")
    print("1. Internet connection")
    print("2. Python dependencies (run: pip install -r requirements.txt)")
    print("3. Chrome browser installation")
    print("4. eCourts website availability")
    print("=" * 60)

if __name__ == '__main__':
    main()
