# coding: utf-8
from .fonction import mean
from PIL import Image


class image_manager:
    """
    Class dedicated to the image processing
    """

    def __init__(self, img):
        self.img = img

    def divide(self):
        tab = []
        dis = [4,5,10,20]
        for k in dis:
            pas = int(100/k)
            for i in range(0,100,pas):
                for j in range(0,100,pas):
                    new = []
                    for k in range(i,i+pas):
                        for l in range(j,j+pas):
                            new.append(mean(self.img.getpixel((k, l))))
                    tab.append(mean(new))
        return tab


class splitter:
    """
    Class dedicated to the creation of objects with 
    """
    
    def __init__(self, fichier):
        self.fichier = fichier
    
    def label_feature_associate(self):
        try:
            img = Image.open("char/"+self.fichier)
            tab = []
            num = [0 for i in range(0,10)]
            num[int(self.fichier.split("_")[0])] = 10000
            tab.append(num)
            instance = image_manager(img)
            tab = tab + instance.divide()
            print(tab)
            return tab
        except Exception as e:
            print(e)
