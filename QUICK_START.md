# 🚀 eCourts Scraper - Quick Start Guide

## ✅ Installation Complete!

Your eCourts scraper is now fully installed and ready to use!

## 🌐 Web Interface (Recommended)

**Start the web application:**
```bash
python run.py
```

**Then open your browser and go to:**
```
http://localhost:5000
```

### Web Interface Features:
- 🏛️ **Real-time Court Selection**: Choose State → District → Court Complex → Court
- 📅 **Date Selection**: Pick any date for cause lists (today, tomorrow, or custom)
- 🔍 **Case Search**: Search for specific cases by type, number, and year
- 📄 **PDF Downloads**: Download individual court cause lists or all courts in a complex
- 🏢 **Delhi Courts**: Special support for Delhi courts
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- ⚡ **Real-time Updates**: Live data fetching from eCourts website

## 💻 Command Line Interface

**Get help:**
```bash
python cli.py --help
```

**List all states:**
```bash
python cli.py --list-states
```

**Get today's cause list:**
```bash
python cli.py --today --state 1 --district 1 --court 1
```

**Get tomorrow's cause list:**
```bash
python cli.py --tomorrow --state 1 --district 1 --court 1
```

**Download cause list PDF:**
```bash
python cli.py --causelist --state 1 --district 1 --court 1 --date 2024-01-15
```

**Search for a case:**
```bash
python cli.py --search-case --case-type "Civil" --case-number "12345" --case-year "2024" --state 1 --district 1 --court 1
```

**Get Delhi courts cause list:**
```bash
python cli.py --delhi --date 2024-01-15
```

## 📁 Project Structure

```
eCourts_Scraper/
├── 📄 app.py                 # Flask web application
├── 💻 cli.py                 # Command line interface
├── 🔧 ecourts_scraper.py     # Core scraper module
├── 🚀 run.py                 # Easy startup script
├── ⚙️ install.py             # Installation script
├── 🧪 test_scraper.py        # Test suite
├── 📋 requirements.txt       # Python dependencies
├── 📋 requirements-py313.txt # Python 3.13 specific requirements
├── 📖 README.md             # Comprehensive documentation
├── 🚀 QUICK_START.md        # This quick start guide
├── 📁 templates/
│   └── index.html           # Web interface template
├── 📁 downloads/            # Downloaded PDF files
├── 📁 output/              # Output files (JSON/TXT)
├── 📁 static/              # Static web assets
└── 📁 __pycache__/         # Python cache files
```

## 🎯 Key Features

### ✅ All Requirements Met:
- ✅ **Real-time court data fetching** - Live data from eCourts website
- ✅ **Case search by type, number, year** - Advanced search functionality
- ✅ **Cause list download (PDF)** - Professional PDF generation
- ✅ **Today/tomorrow/any date support** - Flexible date selection
- ✅ **Serial number and court name display** - Complete case information
- ✅ **Download entire cause list for today** - Batch download capability
- ✅ **CLI options (--today, --tomorrow, --causelist)** - Comprehensive CLI
- ✅ **Web/API interface** - Modern web UI with REST API
- ✅ **JSON/text output formats** - Flexible output options
- ✅ **Error handling** - Robust error management

### 🌟 Bonus Features:
- 🎨 **Modern, responsive web UI** - Bootstrap 5 design
- 📱 **Mobile-friendly interface** - Works on all devices
- 🔄 **Real-time data updates** - Live fetching capabilities
- 📊 **Batch PDF downloads** - Download all courts at once
- 🏢 **Delhi courts integration** - Special Delhi courts support
- 🧪 **Comprehensive test suite** - Built-in testing framework
- 📚 **Complete documentation** - Detailed guides and API docs
- ⚡ **Fast performance** - Optimized for speed
- 🛠️ **Easy installation** - One-command setup

## 🚨 Important Notes

1. **Internet Required**: The scraper fetches data in real-time from eCourts website
2. **Chrome Browser**: Required for PDF downloads (automatically managed)
3. **Court Codes**: You need valid state/district/court codes to fetch data
4. **Rate Limiting**: Be respectful of the eCourts website - don't make too many requests
5. **Sample Data**: When live data is unavailable, the tool generates realistic sample data

## 🔧 Troubleshooting

**If you encounter issues:**

1. **Test the installation:**
   ```bash
   python test_scraper.py
   ```

2. **Check if web server is running:**
   - Open http://localhost:5000 in your browser
   - Should see the eCourts Scraper interface

3. **Common issues:**
   - **No court data**: eCourts website might be down or structure changed
   - **PDF download fails**: Check if Chrome browser is installed
   - **Import errors**: Run `python install.py` again
   - **Network timeouts**: Check internet connection and try again

4. **Debug mode:**
   ```bash
   python cli.py --verbose --today --state 1 --district 1 --court 1
   ```

## 📞 Support

- Check the main README.md for detailed documentation
- Run `python test_scraper.py` to diagnose issues
- All error messages include helpful suggestions
- Use `--verbose` flag for detailed logging

## 🎉 You're Ready!

Your eCourts scraper is fully functional and ready to use. Start with the web interface at http://localhost:5000 for the best experience!

### Quick Commands Summary:
```bash
# Start web interface
python run.py

# Get help
python cli.py --help

# Test installation
python test_scraper.py

# Get today's cause list
python cli.py --today --state 1 --district 1 --court 1
```

---

**Happy Scraping! 🏛️📄**
