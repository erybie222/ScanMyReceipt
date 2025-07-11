import os
import json
from src.ocr.ocr_engine import run_ocr
from src.extract.parser import extract_fields

INPUT_DIR = "data/train/img"
OUTPUT_DIR = "data/result/"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(INPUT_DIR, filename)
        print(f"Processing {filename}...")

        try:
            ocr_text = run_ocr(image_path)
            parsed = extract_fields(ocr_text)

            out_path = os.path.join(OUTPUT_DIR, filename.rsplit(".", 1)[0] + ".json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(parsed, f, indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"❌ Błąd przy {filename}: {e}")
