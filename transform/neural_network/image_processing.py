# coding: utf-8
from .fonction import mean
from PIL import Image


def instance(img):
    tab = []
    dis = [4,5,10,20]
    for k in dis:
        pas = int(100/k)
        for i in range(0,100,pas):
            for j in range(0,100,pas):
                new = []
                for k in range(i,i+pas):
                    for l in range(j,j+pas):
                        new.append( mean( img.getpixel((k,l)) ) )
                tab.append(mean(new))
    return tab
                    
def creer_instance(fichier):
    try:
        print(fichier)
        img = Image.open("char/"+fichier)
        tab = []
        num = [0 for i in range(0,10)]
        ele = int(fichier.split("_")[0])
        num[ele] = 10000
        tab.append(num)
        tab = tab + instance(img)
        return tab
    except Exception as e:
        print(e)