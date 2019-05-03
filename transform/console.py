# coding: utf-8
from neural_network.image_processing import Image_Manager
from PIL import Image


def main():
    fichier = "test/test.png"
    img = Image.open(fichier)
    instance = Image_Manager(img)
    instance.divide()
    print(instance.get_tab()[:])

if __name__ == "__main__":
    main()