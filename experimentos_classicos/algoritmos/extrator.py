import argparse
import glob
from bic import BIC
from gch import GCH
from lch import LCH
import numpy as np


def extrator(diretorio, metodo):
    arq = open('output/fruits_'+metodo+'.csv', 'w')
    print(diretorio)
    # varre todas as imagens do diretorio aplicando
    # descritores e salvando em um arquivo csv
    for i in glob.glob(diretorio + '/*'):
        imagePath = i
        print('--------> ', imagePath, '  <-----------')
        classe = imagePath.split("/")
        features = []

        if (metodo == 'bic'):
            features = BIC(imagePath)
        elif (metodo == 'gch'):
            features = GCH(imagePath)
        elif (metodo == 'lch'):
            features = LCH(imagePath, 2)
        arr = np.asarray(features)
        arr.tofile(arq, sep=',')
        arq.write(',' + classe[len(classe)-1][0:3])
        arq.write('\n')


extrator('Fruits/images', 'gch')
extrator('Fruits/images', 'bic')
extrator('Fruits/images', 'lch')
