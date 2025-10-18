# 🏛️ eCourts Scraper

A comprehensive Python application for fetching court listings and cause lists from eCourts India in real-time. This tool provides both a modern web interface and a powerful command-line interface for accessing court data, downloading cause lists, and searching for specific cases across all Indian states and union territories.

## ✨ Features

### 🌐 Modern Web Interface
- **Real-time Court Data Fetching**: Dynamically load states, districts, court complexes, and courts
- **Interactive UI**: Modern, responsive web interface built with Bootstrap 5
- **Case Search**: Advanced search for specific cases using case type, number, and year
- **Cause List Download**: Download cause lists as PDF files for specific courts or all courts in a complex
- **Delhi Courts Support**: Special support for Delhi courts with dedicated interface
- **Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Updates**: Live data fetching from eCourts website

### 💻 Command Line Interface
- **Comprehensive Commands**: Support for all operations via CLI
- **Flexible Output**: Save results in JSON or text format
- **Batch Operations**: Download cause lists for multiple courts at once
- **Comprehensive Logging**: Detailed logging with configurable verbosity levels
- **Cross-platform**: Works on Windows, macOS, and Linux

### 📊 Core Functionality
- **Complete Court Hierarchy**: State → District → Court Complex → Court navigation
- **Date-based Filtering**: Get cause lists for today, tomorrow, or any specific date
- **PDF Generation**: Download cause lists as professionally formatted PDF files
- **Case Details**: Comprehensive case information including serial numbers and court names
- **Error Handling**: Robust error handling with user-friendly messages
- **Fallback Data**: Sample data generation when live data is unavailable

## 🚀 Installation

### Prerequisites
- **Python 3.7+** (Python 3.8+ recommended)
- **Chrome browser** (for Selenium WebDriver - automatically managed)
- **Internet connection** (for real-time data fetching)
- **4GB RAM minimum** (for Selenium operations)

### Quick Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd eCourts_Scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the installation script** (optional)
   ```bash
   python install.py
   ```

4. **Start the application**
   ```bash
   python run.py
   ```

### Manual Setup

1. **Create necessary directories**
   ```bash
   mkdir -p downloads output templates static
   ```

2. **Install Python dependencies**
   ```bash
   pip install requests beautifulsoup4 selenium flask flask-cors python-dateutil lxml Pillow reportlab webdriver-manager
   ```

3. **Verify installation**
   ```bash
   python test_scraper.py
   ```

## 📖 Usage

### 🌐 Web Interface (Recommended)

1. **Start the web server**
   ```bash
   python run.py
   # or
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Use the interface**
   - **Step 1**: Select State → District → Court Complex → Court (optional)
   - **Step 2**: Choose a date (today, tomorrow, or custom date)
   - **Step 3**: Click "Fetch Cause List" to get the cause list
   - **Step 4**: Use "Download PDF" to download individual court cause lists
   - **Step 5**: Use "Download All Courts PDFs" to download all courts in a complex

### 🔍 Case Search
- Enter case type, case number, and case year
- Select the appropriate court
- Click "Search Case" to find specific case details

### 🏢 Delhi Courts
- Use the dedicated Delhi courts section
- Select date and get cause lists from all Delhi courts

### 💻 Command Line Interface

#### 📋 Basic Commands

**List available states:**
```bash
python cli.py --list-states
```

**List districts for a state:**
```bash
python cli.py --list-districts --state 1
```

**List court complexes for a district:**
```bash
python cli.py --list-complexes --state 1 --district 1
```

**List courts for a complex:**
```bash
python cli.py --list-courts --state 1 --district 1 --complex 1
```

#### 📅 Cause List Operations

**Get today's cause list:**
```bash
python cli.py --today --state 1 --district 1 --court 1
```

**Get tomorrow's cause list:**
```bash
python cli.py --tomorrow --state 1 --district 1 --court 1
```

**Get cause list for a specific date:**
```bash
python cli.py --today --state 1 --district 1 --court 1 --date 2024-01-15
```

**Download cause list PDF:**
```bash
python cli.py --causelist --state 1 --district 1 --court 1 --date 2024-01-15
```

#### 🔍 Case Search

**Search for a specific case:**
```bash
python cli.py --search-case --case-type "Civil" --case-number "12345" --case-year "2024" --state 1 --district 1 --court 1
```

#### 🏢 Delhi Courts

**Get Delhi courts cause list:**
```bash
python cli.py --delhi --date 2024-01-15
```

#### 📁 Output Options

**Save results to file:**
```bash
python cli.py --today --state 1 --district 1 --court 1 --output results.json
```

**Specify output format:**
```bash
python cli.py --today --state 1 --district 1 --court 1 --format txt --output results.txt
```

**Set download directory:**
```bash
python cli.py --causelist --state 1 --district 1 --court 1 --download-dir /path/to/downloads
```

#### 🔧 Verbosity Options

**Verbose output:**
```bash
python cli.py --today --state 1 --district 1 --court 1 --verbose
```

**Quiet mode:**
```bash
python cli.py --today --state 1 --district 1 --court 1 --quiet
```

## 📁 Project Structure

```
eCourts_Scraper/
├── 📄 app.py                 # Flask web application
├── 💻 cli.py                 # Command-line interface
├── 🔧 ecourts_scraper.py     # Core scraper module
├── 🚀 run.py                 # Easy startup script
├── ⚙️ install.py             # Installation script
├── 🧪 test_scraper.py        # Test suite
├── 📋 requirements.txt       # Python dependencies
├── 📋 requirements-py313.txt # Python 3.13 specific requirements
├── 📖 README.md             # This file
├── 🚀 QUICK_START.md        # Quick start guide
├── 📁 templates/
│   └── index.html           # Web interface template
├── 📁 downloads/            # Downloaded PDF files
├── 📁 output/              # Output files (JSON/TXT)
├── 📁 static/              # Static web assets
└── 📁 __pycache__/         # Python cache files
```

## 🔌 API Endpoints

The web application provides the following REST API endpoints:

### 📋 Court Data
- `GET /api/states` - Get all available states
- `GET /api/districts/<state_code>` - Get districts for a state
- `GET /api/court-complexes?state_code=X&district_code=Y` - Get court complexes
- `GET /api/courts?state_code=X&district_code=Y&complex_code=Z` - Get courts

### 🔍 Case Operations
- `POST /api/search-case` - Search for a specific case
- `GET /api/cause-list?state_code=X&district_code=Y&court_code=Z&date=YYYY-MM-DD` - Get cause list

### 📄 Download Operations
- `GET /api/download-cause-list?state_code=X&district_code=Y&court_code=Z&date=YYYY-MM-DD` - Download PDF
- `GET /api/download-all-cause-lists?state_code=X&district_code=Y&complex_code=Z&date=YYYY-MM-DD` - Download all PDFs

### 🏢 Delhi Courts
- `GET /api/delhi-cause-list?date=YYYY-MM-DD` - Get Delhi cause list

## ⚙️ Configuration

### Environment Variables
- `FLASK_ENV` - Flask environment (development/production)
- `FLASK_DEBUG` - Enable/disable Flask debug mode

### Chrome Driver
The application automatically downloads and manages Chrome WebDriver using `webdriver-manager`. No manual setup required.

## 🛠️ Error Handling

The application includes comprehensive error handling:
- **Network connectivity issues** - Automatic retry mechanisms
- **Invalid court codes or dates** - User-friendly validation messages
- **Missing case data** - Fallback to sample data generation
- **PDF download failures** - Graceful error handling with retry options
- **Selenium WebDriver issues** - Automatic driver management and fallback

All errors are logged and user-friendly error messages are displayed.

## 🔧 Troubleshooting

### Common Issues

1. **Chrome Driver Issues**
   - Ensure Chrome browser is installed
   - Check internet connectivity for driver download
   - Run `python test_scraper.py` to diagnose

2. **Network Timeouts**
   - Check eCourts website availability
   - Verify internet connection
   - Try again after a few minutes

3. **PDF Download Failures**
   - Verify court codes are correct
   - Check if cause list exists for the specified date
   - Ensure sufficient disk space

4. **Case Search Issues**
   - Ensure all case details are provided
   - Verify case exists in the specified court
   - Check case number format

### Debug Mode

Enable debug mode for detailed logging:
```bash
python run.py  # Web interface with debug
python cli.py --verbose --today --state 1 --district 1 --court 1  # CLI with verbose output
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is for educational and research purposes. Please respect the eCourts website's terms of service and use responsibly.

## ⚠️ Disclaimer

This tool is designed for legitimate court data access. Users are responsible for complying with all applicable laws and regulations. The developers are not responsible for any misuse of this tool.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the error logs
3. Run `python test_scraper.py` to diagnose issues
4. Open an issue on the repository

## 📝 Changelog

### Version 1.0.0
- ✅ Initial release
- ✅ Web interface with real-time court data fetching
- ✅ Command-line interface with comprehensive options
- ✅ PDF download functionality
- ✅ Case search capabilities
- ✅ Delhi courts support
- ✅ Error handling and logging
- ✅ Mobile-responsive design
- ✅ Sample data generation for testing

---

**Note**: This tool is designed to work with the official eCourts India website. Please ensure you have proper authorization to access court data and comply with all applicable terms of service.

## 🌟 Features Summary

- 🏛️ **Complete Court Coverage**: All Indian states and union territories
- 📱 **Mobile Responsive**: Works on all devices
- 🔄 **Real-time Data**: Live fetching from eCourts website
- 📄 **PDF Generation**: Professional cause list PDFs
- 🔍 **Advanced Search**: Case search by multiple criteria
- 💻 **Dual Interface**: Web UI and CLI
- 🛠️ **Robust Error Handling**: Graceful fallbacks and user feedback
- 🧪 **Comprehensive Testing**: Built-in test suite
