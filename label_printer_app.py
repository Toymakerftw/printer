import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import logging
from data_fetcher import DataFetcher
from qr_code_downloader import QRCodeDownloader
from label_generator import LabelGenerator
from label_printer import LabelPrinter
from utils import INPUT_DIR, OUTPUT_DIR, TEMPLATE_PATH, QR_DIR

class LabelPrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Label Printer App")
        self.label_type = tk.StringVar(value="1")

        tk.Label(root, text="Select Label Type:").grid(row=0, column=0, padx=5, pady=5)
        tk.Radiobutton(root, text="Laptop Tag", variable=self.label_type, value="1").grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(root, text="Asset Tag", variable=self.label_type, value="2").grid(row=0, column=2, padx=5, pady=5)
        tk.Radiobutton(root, text="Name Tag", variable=self.label_type, value="3").grid(row=0, column=3, padx=5, pady=5)

        tk.Button(root, text="Fetch Data", command=self.fetch_data).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(root, text="Download QR Codes", command=self.download_qr_codes).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(root, text="Generate Labels", command=self.generate_labels).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(root, text="Print Labels", command=self.print_labels).grid(row=1, column=3, padx=5, pady=5)

        self.status = tk.Label(root, text="Status: Ready", anchor="w")
        self.status.grid(row=2, column=0, columnspan=4, sticky="we", padx=5, pady=5)

    def update_status(self, message):
        self.status.config(text=f"Status: {message}")
        self.root.update()
        logging.info(message)

    def fetch_data(self):
        def task():
            self.update_status("Fetching data from Google Sheets...")
            try:
                DataFetcher().fetch_data()
                self.update_status("Data processed and saved.")
            except Exception as e:
                self.update_status(f"Error: {e}")
                logging.error(f"Error fetching data: {e}")
        threading.Thread(target=task).start()

    def download_qr_codes(self):
        def task():
            self.update_status("Downloading QR codes...")
            try:
                QRCodeDownloader().download_qr_codes()
                self.update_status("QR codes downloaded successfully.")
            except Exception as e:
                self.update_status(f"Error downloading QR codes: {e}")
                logging.error(f"Error downloading QR codes: {e}")
        threading.Thread(target=task).start()

    def generate_labels(self):
        def task():
            self.update_status("Generating labels...")
            label_type = self.label_type.get()
            try:
                LabelGenerator(label_type).generate_labels()
                self.update_status("Labels generated successfully.")
            except Exception as e:
                self.update_status(f"Error generating labels: {e}")
                logging.error(f"Error generating labels: {e}")
        threading.Thread(target=task).start()

    def print_labels(self):
        def task():
            self.update_status("Printing labels...")
            try:
                LabelPrinter().print_labels()
                self.update_status("Labels printed successfully.")
            except Exception as e:
                self.update_status(f"Printing failed: {e}")
                logging.error(f"Printing failed: {e}")
        threading.Thread(target=task).start()