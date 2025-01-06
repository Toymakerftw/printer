import os
import logging

# Placeholder for sensitive information
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMzMxZTljYjE3ZDk4NWZiMmY0NDFjODc4MzYzNDM2NWE1OTE4OWFlZDY3Yjc2ZWQ1YzA4MjYxYjg4NzY4NDUyM2YwMjNhZTU1Mjc2YmNkNGQiLCJpYXQiOjE3MzYxNTk3NzIuMTUxNzcxLCJuYmYiOjE3MzYxNTk3NzIuMTUxNzczLCJleHAiOjIzNjczMTE3NzIuMTQ2NTM5LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.VWXLvZjj939tj-fjWLwQZXnKJjnLpsJQA_4bKDKEhpOe2DuebXV1gZqCXbUBdIuRlZnB8C0QaICsCiaCCe3CEUDXgQxjN9TtHGFC7z6a7d1M2TOi53qtZbsZUOKm8GlUd9eFJGNlaAGQtsRU72UQCP83ffcceyw2mnrFVoyUbNSZPJ7evH9M0_A4ACMMofyrocXTC5RJEBnLvI3PubYOZQBBM_AIy8DUOfTqE56ChbtzdwGa0ejfQgAJl2sxcZoU0JkMnaS6g883YCd65Nm8-1hQ5sL2CMl897VByZ_M7azKoOZbHOKa-B0a0A4YkvtcOMgX9wtE3VMr8pAB7FDIujaPEZaTg23emNqwJlcjwnwzLLFWrq6EX3yfYOX41a3nJrNoD0ohYyZFTfH0-SYPzeOTTLTfJQYakS4CYzRxqiHvSWy9Lc7dXuQ_C39hX9sTEaoEFqjqQpyUNBmSBE5MZyR5lCL3D4ddzR8B4vbBbKspyKyySrCcWDpmYH6dcYiHOqxR2TgBK5CAQXaJmMm2gTuSBn-YF7C3qJ8uLysnwhYvz5hoX02tjGJLVTWVDITCMpfuMWxax3SAbozSqY6FG53Pqyb8zj3l-qxpwKziJcVk18pB_7h8G-CipWIOeyzG-MPOPPeZl8weWu-kK2ZJzwTuJRxjM_sDGUyButkoVuU"
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1l0yyutZ4TUYK-k35JvA0_fDGZUX4w1A8fsZNEVBFoUU/export?format=csv"

# Directories and paths
INPUT_DIR = "input"
OUTPUT_DIR = "output"
TEMPLATE_PATH = "templates"
QR_DIR = os.path.join(INPUT_DIR, "qr")

if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
if not os.path.exists(QR_DIR):
    os.makedirs(QR_DIR)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("label_printer.log"),
                              logging.StreamHandler()])
