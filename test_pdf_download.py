#!/usr/bin/env python3
"""
Test PDF download functionality
"""

import requests
import time
import os

def test_pdf_download():
    """Test PDF download via web API"""
    print(" Testing PDF download via web API...")
    
    # Wait a bit for server to start
    time.sleep(2)
    
    try:
        # Test PDF download
        url = "http://localhost:5000/api/download-cause-list"
        params = {
            'state_code': '29',
            'district_code': '1', 
            'court_code': '1',
            'date': '2025-10-18'
        }
        
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            # Check if response is a PDF file
            content_type = response.headers.get('content-type', '')
            if 'application/pdf' in content_type:
                print(" PDF download successful via web API")
                
                # Save the PDF to test
                with open('test_download.pdf', 'wb') as f:
                    f.write(response.content)
                print(" PDF saved as test_download.pdf")
                return True
            else:
                print(f" Expected PDF but got content type: {content_type}")
                return False
        else:
            print(f" PDF download failed with status: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f" Error testing PDF download: {e}")
        return False

def test_download_all():
    """Test download all cause lists"""
    print("\n Testing download all cause lists...")
    
    try:
        url = "http://localhost:5000/api/download-all-cause-lists"
        params = {
            'state_code': '29',
            'district_code': '1',
            'complex_code': '1', 
            'date': '2025-10-18'
        }
        
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                files = data.get('data', [])
                print(f" Download all successful - generated {len(files)} PDFs")
                for file_info in files:
                    print(f"   - {file_info.get('court_name')}: {file_info.get('filename')}")
                return True
            else:
                print(f" Download all failed: {data.get('error')}")
                return False
        else:
            print(f" Download all failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f" Error testing download all: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print(" PDF Download Test Suite")
    print("=" * 60)
    
    # Test individual PDF download
    pdf_success = test_pdf_download()
    
    # Test download all
    all_success = test_download_all()
    
    print("\n" + "=" * 60)
    if pdf_success and all_success:
        print(" All PDF download tests passed!")
        print(" Individual PDF download working")
        print(" Download all PDFs working")
    else:
        print(" Some PDF download tests failed")
        if not pdf_success:
            print(" Individual PDF download failed")
        if not all_success:
            print(" Download all PDFs failed")
    print("=" * 60)

if __name__ == '__main__':
    main()
