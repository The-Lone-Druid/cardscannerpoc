import pytesseract
from PIL import Image

class TesseractHelper:
    def __init__(self):
        # You can specify the path to tesseract executable if needed
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pass

    def extract_text(self, image_path):
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"Error in Tesseract text extraction: {str(e)}")
            return "" 