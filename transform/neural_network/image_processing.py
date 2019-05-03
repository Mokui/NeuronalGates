# coding: utf-8
from .fonction import mean
from PIL import Image


class Image_Manager:
    """
    Class dedicated to the image processing
    """

    def __init__(self, img):
        self.img = img
        self.tab = []

    def divide(self):
        dis = [4,5,10,20]
        for k in dis:
            pas = int(100/k)
            for i in range(0,100,pas):
                for j in range(0,100,pas):
                    new = []
                    for k in range(i,i+pas):
                        for l in range(j,j+pas):
                            new.append(mean(self.img.getpixel((k, l))))
                    self.tab.append(mean(new))
    
    def get_tab(self):
        return self.tab


class splitter:
    """
    Class dedicated to the creation of objects with 
    """
    
    def __init__(self, fichier):
        self.fichier = fichier
        self.tab = []
    
    def label_feature_associate(self):
        try:
            img = Image.open("dataset/"+self.fichier)
            num = [0 for i in range(0,10)]
            ele = int(self.fichier.split("_")[0])
            num[ele] = 10000
            self.tab.append(num)
            instance = Image_Manager(img)
            instance.divide()
            self.tab = self.tab + instance.get_tab()
        except Exception as e:
            print("zoulou error:" + str(e))

    def get_tab(self):
        return self.tab

