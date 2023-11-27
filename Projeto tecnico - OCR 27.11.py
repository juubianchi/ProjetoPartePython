import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Andrea - CASA\Tesseract-OCR\tesseract.exe'
texto = str(pytesseract.image_to_string(r"C:\Users\Andrea - CASA\Screenshot_6.png"))
# Dividir a string em linhas
lines = texto.strip().splitlines()

# Criar a matriz de duas colunas
result_matrix = [line.split('-') for line in lines if line.strip()]

result_matrix = result_matrix[1:]
# Criar uma nova matriz com uma terceira coluna para as contagens
result_matrix_with_counts = []

# Contar "P"s e "F"s na segunda coluna de cada linha e adicionar à nova matriz
for row in result_matrix:
    counts = {"P": row[1].count("P"), "F": row[1].count("F")}
    result_matrix_with_counts.append([row[0], row[1],counts['P'],counts['F']])
# Imprimir o resultado com as contagens
for row in result_matrix_with_counts:
    print(row)