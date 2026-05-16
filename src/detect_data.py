from pdf2image import convert_from_path
import pytesseract
import pandas as pd
import os

# Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# IMPORTANT: tessdata folder
os.environ["TESSDATA_PREFIX"] = (
    r"C:\Program Files\Tesseract-OCR\tessdata"
)

# Convert PDF pages to images
pages = convert_from_path(
    "estado_cuenta_abril_2026.pdf",
    dpi=400,
    poppler_path=r"C:\poppler\Library\bin"
)

# Page 2
img = pages[1]

# OCR with coordinates
data = pytesseract.image_to_data(
    img,
    lang="spa",
    output_type=pytesseract.Output.DATAFRAME
)

# Remove empty rows
data = data.dropna(subset=["text"])

print(data.head(50))