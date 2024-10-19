def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
    largura, altura = map(int, dimensoes.split())
    return cabecalho, largura, altura, maiorvalor, pixels

def write_pgm(arquivo, cabecalho, largura, altura, maiorvalor, pixels):
    with open(arquivo, 'w') as f:
        f.write(f"{cabecalho}\n{largura} {altura}\n{maiorvalor}\n")
        for i in range(altura):
            f.write(" ".join(map(str, pixels[i * largura:(i + 1) * largura])) + "\n")

def resize_image(pixels, original_largura, original_altura, nova_largura, nova_altura):
    new_pixels = []
    x_ratio = original_largura / nova_largura
    y_ratio = original_altura / nova_altura

    for i in range(nova_altura):
        for j in range(nova_largura):
            orig_x = int(j * x_ratio)
            orig_y = int(i * y_ratio)
            new_pixels.append(pixels[orig_y * original_largura + orig_x])
    
    return new_pixels

def resize_and_save(input_arquivo, output_arquivo, nova_largura, nova_altura):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    new_pixels = resize_image(pixels, largura, altura, nova_largura, nova_altura)
    write_pgm(output_arquivo, cabecalho, nova_largura, nova_altura, maiorvalor, new_pixels)

#Entrado com a imagem inicial disponibilizada no Classroom
arquivo_entrada = 'Entrada_EscalaCinza.pgm'

#criando imagem 10x menor
resize_and_save(arquivo_entrada, 'imagem_10x_menor.pgm', 480 // 10, 320 // 10)

# Criando imagem 480x320
resize_and_save(arquivo_entrada, 'imagem_480x320.pgm', 480, 320)

# Criando imagem em 720p
resize_and_save(arquivo_entrada, 'imagem_720p.pgm', 1280, 720)

# Criando imagem em 1080p
resize_and_save(arquivo_entrada, 'imagem_1080p.pgm', 1920, 1080)

# Criando imagem em 4k
resize_and_save(arquivo_entrada, 'imagem_4k.pgm', 3840, 2160)

# Criando imagem interpolada 8k
resize_and_save(arquivo_entrada, 'imagem_8k.pgm', 7680, 4320)
