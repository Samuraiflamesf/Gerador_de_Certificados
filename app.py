from PIL import Image, ImageDraw, ImageFont
import pandas as pd


altura = 650         # Defina a altura necessária para escrever o nome
fonte = 'Inter.ttf'  # Fonte para utilizada para escrever o nome
tamanho_fonte = 60   # Defina o tamanho da fonte

def generate_certificate(nome, template, output):
    img = Image.open(template)
    # Carrega a fonte desejada
    font = ImageFont.truetype(fonte, size=tamanho_fonte)
    draw = ImageDraw.Draw(img)
    # Posições dos textos
    nome_pos = (img.width/2, altura)

    # Insere as informações no certificado
    draw.text(nome_pos, nome, fill=(0, 0, 0), font=font, anchor="mm")
    img.save(output)


# Gera um certificado para cada linha do arquivo CSV
data = pd.read_csv('nomes.csv')

for index, row in data.iterrows():
    nome = row['nome']
    template = 'modelo.png'
    output = f'Feitos/{nome}.png'
    generate_certificate(nome, template, output)
