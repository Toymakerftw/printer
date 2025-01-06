import os
import csv
import requests
import logging
from utils import API_TOKEN, QR_DIR, INPUT_DIR

# Ensure the API token is correct and valid
if not API_TOKEN:
    raise ValueError("API_TOKEN is not set in the utils module.")

class QRCodeDownloader:
    def __init__(self):
        self.api_base_url = "http://localhost:8080/api/v1"
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Accept": "application/json"
        }

    def get_asset_data_by_tag(self, asset_tag):
        url = f"{self.api_base_url}/hardware/bytag/{asset_tag}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            asset_data = response.json()
            if asset_data.get('status') == 'error':
                logging.error(f"API returned an error for tag {asset_tag}: {asset_data.get('messages')}")
                return None
            logging.info(f"Successfully retrieved asset data for tag: {asset_tag}")
            print(f"Asset data for tag {asset_tag}: {asset_data}")  # Print the JSON response
            return asset_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get asset data for tag {asset_tag}. Error: {str(e)}")
            return None

    def download_qr_code(self, qr_url, file_path):
        try:
            response = requests.get(qr_url, stream=True)
            response.raise_for_status()

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            logging.info(f"Successfully downloaded QR code to: {file_path}")
            return True
        except Exception as e:
            logging.error(f"Failed to download QR code from {qr_url}. Error: {str(e)}")
            return False

    def download_qr_codes(self):
        logging.info("Downloading QR codes...")

        try:
            if not os.path.exists(QR_DIR):
                os.makedirs(QR_DIR)
                logging.info(f"Created QR directory: {QR_DIR}")

            qr_csv_path = os.path.join(INPUT_DIR, "qr.csv")
            if not os.path.exists(qr_csv_path):
                raise FileNotFoundError("QR CSV file not found")

            missing_qr_codes = []
            successful_downloads = 0

            with open(qr_csv_path, 'r') as qr_file:
                csv_reader = csv.reader(qr_file)
                total_rows = sum(1 for row in csv_reader if row)
                qr_file.seek(0)

                header_skipped = False
                for row in csv_reader:
                    if not row or not row[0].strip():
                        logging.warning("Skipping invalid or empty row in CSV.")
                        continue

                    qr_id = row[0].strip()
                    if not header_skipped and qr_id.lower() == 'qr':
                        logging.info("Skipping header row.")
                        header_skipped = True
                        continue

                    logging.info(f"Processing asset tag: {qr_id}")

                    asset_data = self.get_asset_data_by_tag(qr_id)
                    if not asset_data:
                        missing_qr_codes.append(f"{qr_id} (No asset data)")
                        continue

                    qr_url = asset_data.get('qr')
                    if not qr_url:
                        missing_qr_codes.append(f"{qr_id} (No QR URL)")
                        continue

                    file_path = os.path.join(QR_DIR, f"{qr_id}.png")
                    if self.download_qr_code(qr_url, file_path):
                        successful_downloads += 1
                    else:
                        missing_qr_codes.append(f"{qr_id} (Download failed)")

            if missing_qr_codes:
                logging.warning(f"Failed to download {len(missing_qr_codes)} QR codes:")
                for missing in missing_qr_codes:
                    logging.warning(f"- {missing}")

            status_message = (f"Downloaded {successful_downloads}/{total_rows - 1} QR codes successfully. "
                              f"{len(missing_qr_codes)} failed.")
            logging.info(status_message)

        except Exception as e:
            error_message = f"Error in QR code download process: {str(e)}"
            logging.error(error_message)
            raise
