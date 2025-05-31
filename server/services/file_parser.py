import fitz  # PyMuPDF
import pandas as pd
from openpyxl import load_workbook
from services.encryption import decrypt_data
from pathlib import Path

def detect_file_type(file_path: Path) -> str:
    if file_path.suffix.lower() == ".pdf":
        return "pdf"
    elif file_path.suffix.lower() in [".xls", ".xlsx"]:
        return "excel"
    else:
        raise ValueError("Unsupported file type")

def parse_pdf(file_path: Path) -> list[dict]:
    results = []
    with open(file_path, "rb") as f:
        decrypted = decrypt_data(f.read())

    doc = fitz.open(stream=decrypted, filetype="pdf")
    for i, page in enumerate(doc):
        text = page.get_text()
        results.append({
            "type": "pdf",
            "page": i + 1,
            "text": text,
            "source_file": file_path.name
        })
    return results

def parse_excel(file_path: Path) -> list[dict]:
    results = []
    with open(file_path, "rb") as f:
        decrypted = decrypt_data(f.read())

    tmp_path = file_path.with_suffix(".decrypted.xlsx")
    with open(tmp_path, "wb") as tmp:
        tmp.write(decrypted)

    wb = load_workbook(filename=tmp_path, read_only=True)
    for sheet in wb.sheetnames:
        df = pd.read_excel(tmp_path, sheet_name=sheet)
        results.append({
            "type": "excel",
            "sheet": sheet,
            "text": df.to_string(index=False),
            "source_file": file_path.name
        })

    tmp_path.unlink()  # Clean up decrypted temp
    return results
