import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Andrea - CASA\Tesseract-OCR\tesseract.exe'
texto = pytesseract.image_to_string(r"C:\Users\Andrea - CASA\imagemteste.png")
print(texto)

texto = str(pytesseract.image_to_string(r"C:\Users\Andrea - CASA\Tentativambf.png"))
texto1 = texto.split("\n")
texto2 = [texto1]
print(texto2)