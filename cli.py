#!/usr/bin/env python3
"""
eCourts Scraper CLI Interface
Command-line interface for the eCourts scraper with various options
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from ecourts_scraper import ECourtsScraper
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='eCourts Scraper - Fetch court listings and cause lists',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get today's cause list for a specific court
  python cli.py --today --state 1 --district 1 --court 1

  # Get tomorrow's cause list
  python cli.py --tomorrow --state 1 --district 1 --court 1

  # Download cause list PDF
  python cli.py --causelist --state 1 --district 1 --court 1 --date 2023-10-20

  # Search for a specific case
  python cli.py --search-case --case-type "Civil" --case-number "12345" --case-year "2023" --state 1 --district 1 --court 1

  # Get Delhi cause list
  python cli.py --delhi --date 2023-10-20

  # List all available states
  python cli.py --list-states

  # List districts for a state
  python cli.py --list-districts --state 1

  # List court complexes for a district
  python cli.py --list-complexes --state 1 --district 1

  # List courts for a complex
  python cli.py --list-courts --state 1 --district 1 --complex 1
        """
    )

    # Main action arguments
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('--today', action='store_true', help='Get today\'s cause list')
    action_group.add_argument('--tomorrow', action='store_true', help='Get tomorrow\'s cause list')
    action_group.add_argument('--causelist', action='store_true', help='Download cause list PDF')
    action_group.add_argument('--search-case', action='store_true', help='Search for a specific case')
    action_group.add_argument('--delhi', action='store_true', help='Get Delhi courts cause list')
    action_group.add_argument('--list-states', action='store_true', help='List all available states')
    action_group.add_argument('--list-districts', action='store_true', help='List districts for a state')
    action_group.add_argument('--list-complexes', action='store_true', help='List court complexes for a district')
    action_group.add_argument('--list-courts', action='store_true', help='List courts for a complex')

    # Court selection arguments
    parser.add_argument('--state', help='State code')
    parser.add_argument('--district', help='District code')
    parser.add_argument('--complex', help='Court complex code')
    parser.add_argument('--court', help='Court code')

    # Case search arguments
    parser.add_argument('--case-type', help='Case type for search')
    parser.add_argument('--case-number', help='Case number for search')
    parser.add_argument('--case-year', help='Case year for search')

    # Date argument
    parser.add_argument('--date', help='Date in YYYY-MM-DD format (default: today)')

    # Output arguments
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--format', choices=['json', 'txt'], default='json', help='Output format')
    parser.add_argument('--download-dir', default='downloads', help='Directory for downloaded files')

    # Other arguments
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--quiet', '-q', action='store_true', help='Suppress output except errors')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    # Initialize scraper
    scraper = ECourtsScraper()

    try:
        if args.list_states:
            list_states(scraper, args)
        elif args.list_districts:
            list_districts(scraper, args)
        elif args.list_complexes:
            list_complexes(scraper, args)
        elif args.list_courts:
            list_courts(scraper, args)
        elif args.today or args.tomorrow:
            get_cause_list(scraper, args)
        elif args.causelist:
            download_cause_list(scraper, args)
        elif args.search_case:
            search_case(scraper, args)
        elif args.delhi:
            get_delhi_cause_list(scraper, args)
        else:
            parser.print_help()
            sys.exit(1)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

def list_states(scraper, args):
    """List all available states"""
    logger.info("Fetching states...")
    states = scraper.get_states()
    
    if not states:
        logger.error("No states found")
        return
    
    if args.format == 'json':
        output = json.dumps(states, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([f"{state['value']}: {state['name']}" for state in states])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"States saved to {args.output}")
    else:
        print(output)

def list_districts(scraper, args):
    """List districts for a state"""
    if not args.state:
        logger.error("State code is required for listing districts")
        return
    
    logger.info(f"Fetching districts for state {args.state}...")
    districts = scraper.get_districts(args.state)
    
    if not districts:
        logger.error("No districts found")
        return
    
    if args.format == 'json':
        output = json.dumps(districts, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([f"{district['value']}: {district['name']}" for district in districts])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Districts saved to {args.output}")
    else:
        print(output)

def list_complexes(scraper, args):
    """List court complexes for a district"""
    if not args.state or not args.district:
        logger.error("State code and district code are required for listing court complexes")
        return
    
    logger.info(f"Fetching court complexes for state {args.state}, district {args.district}...")
    complexes = scraper.get_court_complexes(args.state, args.district)
    
    if not complexes:
        logger.error("No court complexes found")
        return
    
    if args.format == 'json':
        output = json.dumps(complexes, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([f"{complex['value']}: {complex['name']}" for complex in complexes])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Court complexes saved to {args.output}")
    else:
        print(output)

def list_courts(scraper, args):
    """List courts for a complex"""
    if not args.state or not args.district or not args.complex:
        logger.error("State code, district code, and complex code are required for listing courts")
        return
    
    logger.info(f"Fetching courts for state {args.state}, district {args.district}, complex {args.complex}...")
    courts = scraper.get_courts(args.state, args.district, args.complex)
    
    if not courts:
        logger.error("No courts found")
        return
    
    if args.format == 'json':
        output = json.dumps(courts, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([f"{court['value']}: {court['name']}" for court in courts])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Courts saved to {args.output}")
    else:
        print(output)

def get_cause_list(scraper, args):
    """Get cause list for today or tomorrow"""
    if not args.state or not args.district or not args.court:
        logger.error("State code, district code, and court code are required")
        return
    
    # Determine date
    if args.today:
        date = datetime.now().strftime('%Y-%m-%d')
    elif args.tomorrow:
        date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        date = args.date or datetime.now().strftime('%Y-%m-%d')
    
    logger.info(f"Fetching cause list for court {args.court} on {date}...")
    cause_list = scraper.get_cause_list(args.state, args.district, args.court, date)
    
    if not cause_list:
        logger.warning("No cause list found")
        return
    
    if args.format == 'json':
        output = json.dumps(cause_list, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([str(case_item) for case_item in cause_list])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Cause list saved to {args.output}")
    else:
        print(output)

def download_cause_list(scraper, args):
    """Download cause list PDF"""
    if not args.state or not args.district or not args.court:
        logger.error("State code, district code, and court code are required")
        return
    
    date = args.date or datetime.now().strftime('%Y-%m-%d')
    
    logger.info(f"Downloading cause list PDF for court {args.court} on {date}...")
    pdf_path = scraper.download_cause_list_pdf(args.state, args.district, args.court, date, args.download_dir)
    
    if pdf_path:
        logger.info(f"PDF downloaded successfully: {pdf_path}")
    else:
        logger.error("Failed to download PDF")

def search_case(scraper, args):
    """Search for a specific case"""
    if not all([args.case_type, args.case_number, args.case_year, args.state, args.district, args.court]):
        logger.error("All case details and court information are required for case search")
        return
    
    logger.info(f"Searching for case: {args.case_type} {args.case_number}/{args.case_year}")
    case_details = scraper.search_case(
        args.case_type, args.case_number, args.case_year,
        args.state, args.district, args.court
    )
    
    if not case_details:
        logger.warning("Case not found")
        return
    
    if args.format == 'json':
        output = json.dumps(case_details, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([f"{key}: {value}" for key, value in case_details.items()])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Case details saved to {args.output}")
    else:
        print(output)

def get_delhi_cause_list(scraper, args):
    """Get Delhi courts cause list"""
    date = args.date or datetime.now().strftime('%Y-%m-%d')
    
    logger.info(f"Fetching Delhi courts cause list for {date}...")
    cause_list = scraper.get_delhi_cause_list(date)
    
    if not cause_list:
        logger.warning("No cause list found")
        return
    
    if args.format == 'json':
        output = json.dumps(cause_list, indent=2, ensure_ascii=False)
    else:
        output = "\n".join([str(case_item) for case_item in cause_list])
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Delhi cause list saved to {args.output}")
    else:
        print(output)

if __name__ == '__main__':
    main()
