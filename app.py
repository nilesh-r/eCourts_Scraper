from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
from ecourts_scraper import ECourtsScraper
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize scraper
scraper = ECourtsScraper()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/states')
def get_states():
    """Get all available states"""
    try:
        states = scraper.get_states()
        return jsonify({'success': True, 'data': states})
    except Exception as e:
        logger.error(f"Error fetching states: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/districts/<state_code>')
def get_districts(state_code):
    """Get districts for a state"""
    try:
        districts = scraper.get_districts(state_code)
        return jsonify({'success': True, 'data': districts})
    except Exception as e:
        logger.error(f"Error fetching districts: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/court-complexes')
def get_court_complexes():
    """Get court complexes for a state and district"""
    try:
        state_code = request.args.get('state_code')
        district_code = request.args.get('district_code')
        
        if not state_code or not district_code:
            return jsonify({'success': False, 'error': 'State code and district code are required'})
        
        court_complexes = scraper.get_court_complexes(state_code, district_code)
        return jsonify({'success': True, 'data': court_complexes})
    except Exception as e:
        logger.error(f"Error fetching court complexes: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/courts')
def get_courts():
    """Get courts for a court complex"""
    try:
        state_code = request.args.get('state_code')
        district_code = request.args.get('district_code')
        complex_code = request.args.get('complex_code')
        
        if not all([state_code, district_code, complex_code]):
            return jsonify({'success': False, 'error': 'State code, district code, and complex code are required'})
        
        courts = scraper.get_courts(state_code, district_code, complex_code)
        return jsonify({'success': True, 'data': courts})
    except Exception as e:
        logger.error(f"Error fetching courts: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/search-case', methods=['POST'])
def search_case():
    """Search for a specific case"""
    try:
        data = request.get_json()
        
        case_type = data.get('case_type')
        case_number = data.get('case_number')
        case_year = data.get('case_year')
        state_code = data.get('state_code')
        district_code = data.get('district_code')
        court_code = data.get('court_code')
        
        if not all([case_type, case_number, case_year, state_code, district_code, court_code]):
            return jsonify({'success': False, 'error': 'All case details are required'})
        
        case_details = scraper.search_case(case_type, case_number, case_year, state_code, district_code, court_code)
        
        if case_details:
            return jsonify({'success': True, 'data': case_details})
        else:
            return jsonify({'success': False, 'error': 'Case not found'})
            
    except Exception as e:
        logger.error(f"Error searching case: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cause-list')
def get_cause_list():
    """Get cause list for a specific court and date"""
    try:
        state_code = request.args.get('state_code')
        district_code = request.args.get('district_code')
        court_code = request.args.get('court_code')
        date = request.args.get('date')
        
        if not all([state_code, district_code, court_code, date]):
            return jsonify({'success': False, 'error': 'State code, district code, court code, and date are required'})
        
        cause_list = scraper.get_cause_list(state_code, district_code, court_code, date)
        return jsonify({'success': True, 'data': cause_list})
        
    except Exception as e:
        logger.error(f"Error fetching cause list: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/download-cause-list')
def download_cause_list():
    """Download cause list PDF"""
    try:
        state_code = request.args.get('state_code')
        district_code = request.args.get('district_code')
        court_code = request.args.get('court_code')
        date = request.args.get('date')
        
        if not all([state_code, district_code, court_code, date]):
            return jsonify({'success': False, 'error': 'State code, district code, court code, and date are required'})
        
        pdf_path = scraper.download_cause_list_pdf(state_code, district_code, court_code, date)
        
        if pdf_path and os.path.exists(pdf_path):
            return send_file(pdf_path, as_attachment=True)
        else:
            return jsonify({'success': False, 'error': 'Failed to download PDF'})
            
    except Exception as e:
        logger.error(f"Error downloading cause list: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/delhi-cause-list')
def get_delhi_cause_list():
    """Get cause list from Delhi courts"""
    try:
        date = request.args.get('date')
        if not date:
            return jsonify({'success': False, 'error': 'Date is required'})
        
        cause_list = scraper.get_delhi_cause_list(date)
        return jsonify({'success': True, 'data': cause_list})
        
    except Exception as e:
        logger.error(f"Error fetching Delhi cause list: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/download-all-cause-lists')
def download_all_cause_lists():
    """Download cause lists for all courts in a complex"""
    try:
        state_code = request.args.get('state_code')
        district_code = request.args.get('district_code')
        complex_code = request.args.get('complex_code')
        date = request.args.get('date')
        
        if not all([state_code, district_code, complex_code, date]):
            return jsonify({'success': False, 'error': 'State code, district code, complex code, and date are required'})
        
        # Get all courts in the complex
        courts = scraper.get_courts(state_code, district_code, complex_code)
        
        downloaded_files = []
        for court in courts:
            court_code = court['value']
            court_name = court['name']
            
            pdf_path = scraper.download_cause_list_pdf(state_code, district_code, court_code, date)
            if pdf_path:
                downloaded_files.append({
                    'court_name': court_name,
                    'file_path': pdf_path,
                    'filename': os.path.basename(pdf_path)
                })
        
        return jsonify({'success': True, 'data': downloaded_files})
        
    except Exception as e:
        logger.error(f"Error downloading all cause lists: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    os.makedirs('downloads', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
