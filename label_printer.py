import os
import logging
from brother_label import BrotherLabel
from utils import OUTPUT_DIR

class LabelPrinter:
    def __init__(self, model="PT-P900W", connection="usb://0x04f9:0x2042"):
        """
        Initializes the LabelPrinter with a printer model and a connection string.
        Change the connection string as needed to match your printer's USB details.
        """
        self.model = model
        self.connection = connection

    def print_labels(self):
        logging.info("Printing labels...")
        try:
            printer = BrotherLabel(self.model, self.connection)
            # List all PNG files in the output directory
            png_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")]
            if not png_files:
                logging.info("No label images found to print.")
            for file_name in png_files:
                file_path = os.path.join(OUTPUT_DIR, file_name)
                logging.info(f"Printing label: {file_path}")
                printer.print_image(file_path)
            logging.info("Labels printed successfully.")
        except Exception as e:
            logging.error(f"Printing failed: {e}")
            raise
