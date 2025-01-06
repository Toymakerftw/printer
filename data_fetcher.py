import os
import csv
import wget
import shutil
import logging
from utils import GOOGLE_SHEET_URL, INPUT_DIR

class DataFetcher:
    def fetch_data(self):
        logging.info("Fetching data from Google Sheets...")
        try:
            # Download the file
            filename = wget.download(GOOGLE_SHEET_URL)
            logging.info("Data fetched successfully. Processing...")

            # Process the downloaded file
            with open(filename, "r", newline="") as file, \
                 open("lap.csv", "w") as lap, \
                 open("assigned.csv", "w") as assigned, \
                 open("num.csv", "w") as num, \
                 open("qr.csv", "w") as qr:

                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    if not row:  # Skip empty rows
                        continue
                    if any(cell.startswith('/*') or cell.startswith('//') for cell in row):  # Skip comment rows
                        logging.warning(f"Skipping comment row: {row}")
                        continue
                    if len(row) >= 5:  # Check if the row has at least 5 columns
                        print(row[2], ",", row[3], file=lap)
                        print(row[0], file=num)
                        print(row[1], file=assigned)
                        print(row[4], file=qr)
                    else:
                        logging.warning(f"Skipping row with insufficient columns: {row}")

            # Remove the original file
            os.remove(filename)

            # Move files to the input directory
            destination_dir = INPUT_DIR
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            shutil.move("lap.csv", os.path.join(destination_dir, "lap.csv"))
            shutil.move("assigned.csv", os.path.join(destination_dir, "assigned.csv"))
            shutil.move("num.csv", os.path.join(destination_dir, "num.csv"))
            shutil.move("qr.csv", os.path.join(destination_dir, "qr.csv"))

            logging.info("Data processed and saved.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise
