import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.ocr.ocr_engine import process_folder

INPUT_DIR = "data/test/img/"
OUTPUT_DIR = "data/result/"

process_folder(INPUT_DIR, OUTPUT_DIR)
