import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
from PIL import Image

# Função para calcular os descritores BIC


def BIC(img_path):
    try:
        fator = 64
        img = Image.open(img_path).convert('RGB').convert('L')
        histInt, histExt = [0] * fator, [0] * fator
        N, M = img.size
        for x in range(N):
            for y in range(M):
                ind = int((img.getpixel((x, y)) / 255) * (fator-1))
                if (x == 0 or y == 0 or x+1 == N or y+1 == M):
                    histExt[ind] += 1
                else:
                    # olha se os vizinho são iguais
                    if (img.getpixel((x, y)) == img.getpixel((x, y-1)) and
                            img.getpixel((x, y)) == img.getpixel((x, y+1)) and
                            img.getpixel((x, y)) == img.getpixel((x-1, y)) and
                            img.getpixel((x, y)) == img.getpixel((x+1, y))):
                        histInt[ind] += 1
                    else:
                        histExt[ind] += 1
        return histInt + histExt
    except Exception as e:
        print('\n---Erro no descritor BIC--\n', e)

# GCH


def gch(image_path):
    try:
        bins = 10
        img = Image.open(image_path).convert('RGB')
        evolution = (255/bins)
        features = []
        histR, histG, histB = [0] * bins, [0] * bins, [0] * bins
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = img.getpixel((i, j))
                lookBin = 0
                controlR = evolution
                contR, contG, contB = 0, 0, 0
                while (lookBin == 0):
                    contR += 1
                    if (r <= controlR):
                        r = controlR
                        lookBin = 1
                    else:
                        controlR += evolution
                        if (controlR >= 255):
                            controlR = 255
                lookBin = 0
                controlG = evolution
                while (lookBin == 0):
                    contG += 1
                    if (g <= controlG):
                        g = controlG
                        lookBin = 1
                    else:
                        controlG += evolution
                        if (controlG >= 255):
                            controlG = 255
                lookBin = 0
                controlB = evolution
                while (lookBin == 0):
                    contB += 1
                    if (b <= controlB):
                        b = controlB
                        lookBin = 1
                    else:
                        controlB += evolution
                        if (controlB >= 255):
                            controlB = 255
                histR[contR-1] += 1
                histG[contG-1] += 1
                histB[contB-1] += 1

        features = histR + histG + histB
        return features
    except Exception as e:
        print('\n################# (LBP) - Error in processing! #################\n', e)
