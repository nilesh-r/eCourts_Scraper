#!/usr/bin/env python3
"""
Test web server functionality
"""

import requests
import time
import sys

def test_web_server():
    """Test if web server is running and responding"""
    print(" Testing web server...")
    
    # Wait a bit for server to start
    time.sleep(3)
    
    try:
        # Test main page
        response = requests.get('http://localhost:5000', timeout=10)
        if response.status_code == 200:
            print(" Main page is accessible")
        else:
            print(f" Main page returned status {response.status_code}")
            return False
    except Exception as e:
        print(f" Main page not accessible: {e}")
        return False
    
    try:
        # Test states API
        response = requests.get('http://localhost:5000/api/states', timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and data.get('data'):
                print(f" States API working - found {len(data['data'])} states")
            else:
                print(" States API returned no data")
                return False
        else:
            print(f" States API returned status {response.status_code}")
            return False
    except Exception as e:
        print(f" States API not accessible: {e}")
        return False
    
    try:
        # Test districts API
        response = requests.get('http://localhost:5000/api/districts/29', timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and data.get('data'):
                print(f" Districts API working - found {len(data['data'])} districts for Delhi")
            else:
                print(" Districts API returned no data")
                return False
        else:
            print(f" Districts API returned status {response.status_code}")
            return False
    except Exception as e:
        print(f" Districts API not accessible: {e}")
        return False
    
    print(" Web server is working perfectly!")
    return True

if __name__ == '__main__':
    if test_web_server():
        print("\n All tests passed! Your eCourts scraper is ready to use.")
        print(" Open your browser and go to: http://localhost:5000")
    else:
        print("\n Some tests failed. Please check the server logs.")
        sys.exit(1)
