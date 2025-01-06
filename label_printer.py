import os
import logging
from brother_label import BrotherLabel
from utils import OUTPUT_DIR

class LabelPrinter:
    def print_labels(self):
        logging.info("Printing labels...")
        try:
            printer = BrotherLabel("PT-P900W", "usb")
            for file_name in os.listdir(OUTPUT_DIR):
                if file_name.endswith(".png"):
                    file_path = os.path.join(OUTPUT_DIR, file_name)
                    printer.print_image(file_path)
            logging.info("Labels printed successfully.")
        except Exception as e:
            logging.error(f"Printing failed: {e}")
            raise
