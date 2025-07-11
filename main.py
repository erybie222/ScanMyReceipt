from src.ocr.ocr_engine import run_ocr
from src.extract.parser import extract_fields
import json

image_path = "data/train/img/X00016469612.jpg"
ocr_text = run_ocr(image_path)

parsed = extract_fields(ocr_text)
print("--- OCR TEXT ---")
print(ocr_text)

print(json.dumps(parsed, indent=2, ensure_ascii=False))
