import numpy as np
from PIL import Image

def LCH(pathImage, valorDivisao):
    imagem = Image.open(pathImage)
    w,h = imagem.size
    quantidadeBinsDesejada = 64
    tamanhoHistograma = quantidadeBinsDesejada / 3
    out = []

    fatorDivisao = 256 / tamanhoHistograma
    histogramaR = np.zeros(int(tamanhoHistograma) + 1, dtype=int)
    histogramaG = np.zeros(int(tamanhoHistograma) + 1, dtype=int)
    histogramaB = np.zeros(int(tamanhoHistograma) + 1, dtype=int)
    maxLinha = w
    maxColuna = h
    maxI = int(maxLinha / valorDivisao)
    maxi = int(maxLinha / valorDivisao)
    maxJ = int(maxColuna / valorDivisao)
    maxj = int(maxColuna / valorDivisao)
    inicioI = 0
    inicioJ = 0
    contI = 0
    contJ = 0
    vetor = np.zeros(3, dtype=int)
    while (contJ != valorDivisao):
      inicioJ = 0
      maxJ = maxj
      contI = 0
      while (contI != valorDivisao):
        for i in range(len(histogramaR)):
          histogramaR[i] = 0.0
          histogramaG[i] = 0.0
          histogramaB[i] = 0.0
        for i  in range(inicioI,maxI):
          for j in range(inicioJ, maxJ):
            vetor = imagem.getpixel((i, j))
            histogramaR[int(vetor[0] / fatorDivisao)] = histogramaR[int(vetor[0] / fatorDivisao)] + 1.0
            histogramaG[int(vetor[1] / fatorDivisao)] = histogramaG[int(vetor[1] / fatorDivisao)] + 1.0
            histogramaB[int(vetor[2] / fatorDivisao)] = histogramaB[int(vetor[2] / fatorDivisao)] + 1.0

        out.extend(histogramaR)
        out.extend(histogramaG)
        out.extend(histogramaB)

        inicioJ = maxJ
        maxJ += maxj
        if maxJ > maxColuna:
          maxJ = maxColuna
        contI = contI + 1

      inicioI = maxI
      maxI += maxi
      if (maxi > maxLinha):
        maxJ = maxLinha
      contJ = contJ + 1

    return out

