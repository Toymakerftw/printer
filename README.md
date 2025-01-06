# Label Generation and Printing System

## Overview
This repository contains a system to automate the process of generating and printing labels for assets. The system fetches data from Google Sheets, downloads associated QR codes, generates labels using predefined templates, and prints them using a label printer.

---

## Features

- **Data Fetching**: Retrieve data directly from Google Sheets and organize it into categorized CSV files.
- **QR Code Integration**: Automatically download QR codes for each asset using an API.
- **Label Generation**: Generate labels for three types:
  - Laptop Tags
  - Asset Tags
  - Name Tags
- **Label Printing**: Print generated labels using a Brother PT-P900W label printer.
- **User-Friendly Interface**: A GUI application for controlling the workflow.
- **Error Handling**: Comprehensive logging and robust exception management.

---

## Directory Structure
```
.
├── data_fetcher.py          # Handles data fetching from Google Sheets
├── label_generator.py       # Generates labels from templates
├── label_printer.py         # Interacts with the label printer
├── label_printer_app.py     # GUI application
├── main.py                  # Entry point for the application
├── qr_code_downloader.py    # Downloads QR codes
├── utils.py                 # Configuration and utility functions
├── input/                   # Directory for input files
├── output/                  # Directory for generated labels
├── templates/               # Directory for label templates
└── label_printer.log        # Log file
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/label-system.git
   cd label-system
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Directories**:
   Required directories (`input`, `output`, `templates`) are created automatically if they do not exist.

4. **Configure Settings**:
   Update `utils.py` with the following:
   - `API_TOKEN`: Your API token for the QR code service.
   - `GOOGLE_SHEET_URL`: The Google Sheets URL for data fetching.

---

## Usage

### Run the Application
To launch the GUI:
```bash
python main.py
```

### Workflow
1. **Fetch Data**: Click "Fetch Data" to retrieve asset information from Google Sheets.
2. **Download QR Codes**: Click "Download QR Codes" to download asset-specific QR codes.
3. **Generate Labels**: Select the label type and click "Generate Labels."
4. **Print Labels**: Click "Print Labels" to print the generated labels.

---

## Dependencies

- Python 3.x
- Libraries: `tkinter`, `Pillow`, `wget`, `requests`, `logging`
- Brother PT-P900W label printer (or compatible)

---

## Logs
Logs are stored in `label_printer.log` and provide details about the system's operations and errors.

---

## License
This project is licensed under the [MIT License](LICENSE).

