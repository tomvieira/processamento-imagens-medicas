import numpy as np
from PIL import Image


def BIC(imagem):
    imagem = Image.open(imagem)
    width,height = imagem.size
    out = []
    for i in range(width):
        for k in range(height):
            valorBinario = ""
            vetor = imagem.getpixel((i, k))
            valorBinario += quatizaNumero(vetor[0])
            valorBinario += quatizaNumero(vetor[1])
            valorBinario += quatizaNumero(vetor[2])
            valor = int(valorBinario,2)
            tupla = (valor,vetor[1],vetor[2])
            imagem.putpixel((i, k), tuple(tupla))
    i1 = np.zeros(3, dtype=int)
    im1 = np.zeros(3, dtype=int)
    j1 = np.zeros(3, dtype=int)
    jm1 = np.zeros(3, dtype=int)
    histograma1 = np.zeros(64, dtype=float)
    histograma2 = np.zeros(64, dtype=float)
    for j in range(1, width - 1):
        for k in range(1, height - 1):
            vetor = imagem.getpixel((j,k))
            i1 = imagem.getpixel((j + 1, k))
            im1 = imagem.getpixel((j - 1, k))
            j1 = imagem.getpixel((j, k + 1))
            jm1 = imagem.getpixel((j, k - 1))
            if vetor[0] == i1[0] and vetor[0] == im1[0] and vetor[0] == j1[0] and vetor[0] == jm1[0]:
                histograma1[vetor[0]] += 1
            else:
                histograma2[vetor[0]] += 1
    out.extend(histograma1)
    out.extend(histograma2)
    return out


def quatizaNumero(valor):
    if valor >= 193:
        return '11'
    elif valor >= 129:
        return '10'
    elif valor >= 64:
        return '01'
    else:
        return '00'
