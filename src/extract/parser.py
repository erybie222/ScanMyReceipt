import re
from typing import List, Dict

def extract_fields(ocr_text: str) -> Dict:
    lines = ocr_text.splitlines()

    result = {
        "shop": "",
        "date": "",
        "invoice_no": "",
        "total": None,
        "items": [],
        "payment_method": ""
    }

    for line in lines:
        if "SDN BHD" in line or "MARKETING" in line:
            result["shop"] = line.strip()
            break

    for line in lines:
        match = re.search(r"(\d{2}/\d{2}/\d{4})\s+(\d{1,2}:\d{2}:\d{2})", line)
        if match:
            result["date"] = f"{match.group(1)} {match.group(2)}"
            break

    for line in lines:
        if "Invoice No" in line:
            idx = lines.index(line)
            if idx + 1 < len(lines):
                result["invoice_no"] = lines[idx + 1].strip()
            break

    for line in lines[::-1]:
        match = re.search(r"TOTAL[:\s]+(\d+[.,]?\d*)", line.upper())
        if match:
            try:
                result["total"] = float(match.group(1).replace(",", ""))
            except:
                pass
            break

    for line in lines:
        if any(m in line.upper() for m in ["CASH", "VISA", "MASTERCARD"]):
            result["payment_method"] = line.strip()
            break

    for i, line in enumerate(lines):
        if "Qty:" in line:
            name = line.strip()
            qty_line = lines[i]
            price_line = lines[i + 1] if i + 1 < len(lines) else ""
            try:
                qty = int(re.search(r"Qty:\s*(\d+)", qty_line).group(1))
                price = float(re.findall(r"[\d]+[.,]?[\d]*", price_line)[-1])
                result["items"].append({
                    "name": name.split("Qty")[0].strip(),
                    "qty": qty,
                    "price": price
                })
            except:
                continue

    return result
