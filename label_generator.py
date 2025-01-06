import os
import csv
import re
from PIL import Image, ImageDraw, ImageFont
import logging
from utils import INPUT_DIR, OUTPUT_DIR, TEMPLATE_PATH, QR_DIR

class LabelGenerator:
    def __init__(self, label_type):
        self.label_type = label_type

    def generate_labels(self):
        logging.info("Generating labels...")
        input_file = ""
        template_file = ""
        qr_csv_path = os.path.join(INPUT_DIR, "qr.csv")

        if self.label_type == "1":
            input_file = os.path.join(INPUT_DIR, "lap.csv")
            template_file = os.path.join(TEMPLATE_PATH, "1.png")
        elif self.label_type == "2":
            input_file = os.path.join(INPUT_DIR, "num.csv")
            template_file = os.path.join(TEMPLATE_PATH, "2.png")
        elif self.label_type == "3":
            input_file = os.path.join(INPUT_DIR, "assigned.csv")
            template_file = os.path.join(TEMPLATE_PATH, "3.png")
        else:
            logging.error("Invalid label type selected.")
            return

        if not os.path.exists(input_file):
            logging.error("Input CSV file not found.")
            return

        if not os.path.exists(template_file):
            logging.error("Template image not found.")
            return

        if not os.path.exists(qr_csv_path):
            logging.error("QR CSV file not found.")
            return

        qr_code_names = []
        with open(qr_csv_path, 'r') as qr_csv_file:
            qr_csv_reader = csv.reader(qr_csv_file)
            for row in qr_csv_reader:
                if row:
                    qr_code_names.append(row[0])

        try:
            with open(input_file, 'r') as fp:
                lines = fp.readlines()

            for index, line in enumerate(lines):
                if index >= len(qr_code_names):
                    logging.error("Not enough QR codes available for all entries.")
                    break

                if self.label_type == "1":
                    a, b = line.strip().split(',')
                    l = re.sub(r'\W+', '', a)

                    img = Image.open(template_file)
                    fnt1 = ImageFont.truetype('Arial.ttf', 80)
                    fnt2 = ImageFont.truetype('Arial.ttf', 30)
                    d = ImageDraw.Draw(img)

                    d.text((120, 130), a, font=fnt1, fill=(0, 0, 0))
                    d.text((130, 220), b, font=fnt2, fill=(0, 0, 0))

                    qr_code_name = qr_code_names[index]
                    qr_code_path = os.path.join(QR_DIR, f"{qr_code_name}.png")
                    if not os.path.exists(qr_code_path):
                        logging.error(f"QR code image '{qr_code_name}' not found.")
                        continue

                    overlay_image = Image.open(qr_code_path)
                    desired_size = (200, 200)
                    overlay_image = overlay_image.resize(desired_size)
                    position = (700, 70)
                    img.paste(overlay_image, position)

                    output_file_path = os.path.join(OUTPUT_DIR, f"lap-{l}.png")
                    img.save(output_file_path)

                    logging.info(f"Lap - Asset tag created for - {a}. Saved as: {output_file_path}")

                elif self.label_type == "2":
                    value1 = line.strip()
                    l = re.sub(r'\W+', '', value1)

                    img = Image.open(template_file)
                    fnt1 = ImageFont.truetype('Arial.ttf', 20)
                    fnt2 = ImageFont.truetype('Arial.ttf', 20)
                    d = ImageDraw.Draw(img)

                    d.text((35, 50), value1, font=fnt1, fill=(0, 0, 0))

                    qr_code_name = qr_code_names[index]
                    qr_code_path = os.path.join(QR_DIR, f"{qr_code_name}.png")
                    if not os.path.exists(qr_code_path):
                        logging.error(f"QR code image '{qr_code_name}' not found.")
                        continue

                    overlay_image = Image.open(qr_code_path)
                    desired_size = (60, 60)
                    overlay_image = overlay_image.resize(desired_size)
                    position = (100, 15)
                    img.paste(overlay_image, position)

                    output_file_path = os.path.join(OUTPUT_DIR, f"Asset-no-{l}.png")
                    img.save(output_file_path)

                    logging.info(f"Asset Number - {value1}. Saved as: {output_file_path}")

                elif self.label_type == "3":
                    value1 = line.strip()
                    l = re.sub(r'\W+', '', value1)

                    img = Image.open(template_file)
                    fnt1 = ImageFont.truetype('Arial.ttf', 88)
                    d = ImageDraw.Draw(img)

                    d.text((55, 285), value1, font=fnt1, fill=(0, 0, 0))

                    output_file_path = os.path.join(OUTPUT_DIR, f"Assigned to -{l}.png")
                    img.save(output_file_path)

                    logging.info(f"Assigned to - {value1}. Saved as: {output_file_path}")

            logging.info("Labels generated successfully.")
        except Exception as e:
            logging.error(f"Error generating labels: {e}")
            raise
