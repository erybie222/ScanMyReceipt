import easyocr
import cv2
import os
import warnings

warnings.filterwarnings("ignore")
reader = easyocr.Reader(['en'], gpu=True)

def run_ocr(image_path:str) -> str:
    result = reader.readtext(image_path, detail =0)
    return "\n".join(result)

def process_folder(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok = True)
    for filename in os.listdir( input_dir):
        if filename.lower().endswith((".jpg" , ".png", ".jpeg")):
            path = os.path.join(input_dir, filename)
            text = run_ocr(path)
            out_path = os.path.join(output_dir, filename.rsplit(".", 1)[0] + ".txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)