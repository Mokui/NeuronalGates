# coding: utf-8
from neural_network.image_processing import Image_Manager
import requests
import json
from PIL import Image
import os
import json


def main():
    fichier = "test/test.png"
    img = Image.open(fichier)
    instance = Image_Manager(img)
    instance.divide()
    print(instance.get_tab()[:])
    pred = requests.post("http://127.0.0.1:5000/image/", {"image": instance.get_tab()[:]})

if __name__ == "__main__":
    main()