import pytesseract
import re
import fitz
from PIL import Image
import os
import cv2 as cv2
import pandas as pd

# Exemplo 1: Retirando informações de imagem
def exemplo_1():
    return (pytesseract.image_to_string('teste.png'))

# Exemplo 2: Buscando padrões no texto por Regex
# https://regexr.com/
def exemplo_2(text):
    result = re.search(pattern="([0-9])\w+", string=text)
    return result[0]

# Exemplo 3: Lendo arquivos PDFs
def exemplo_3():
    local = os.getcwd()
    doc = fitz.open(f"{local}//pdf_exemplo.pdf")
    i = 0
    #convertendo paginas do PDF para imagens
    for page in doc:
        i += 1
        pix = page.get_pixmap(dpi=200)
        pix.save(f"./images_pdf/{i}.png")
        
    # Coletando imagens da pasta
    images = os.listdir("./images_pdf")
    
    # lendo cada imagem da pasta
    tags = pd.read_excel("coordenadas.xlsx")
    for image in images:
        img = cv2.imread(f"./images_pdf/{image}")
        for i in tags.index:
            box = img[
                tags['y1'][i]:tags['y2'][i],
                tags['x1'][i]:tags['x2'][i]
                ]
            text = pytesseract.image_to_string(box)
            print(f"{tags['tag'][i]}: {text}")


if __name__ == "__main__":
    print(exemplo_1())
    print(exemplo_2("® Join the official Python Developers Survey 2022 and win valuable prizes"))
    exemplo_3()