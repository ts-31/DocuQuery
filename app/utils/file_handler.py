# utils/file_handler.py
import pdfplumber

def extract_text_from_pdf(file):
    with pdfplumber.open(file.file) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)
