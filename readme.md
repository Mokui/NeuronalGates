### ML Project

This project aim to recognize letter from an image

You'll need [Postman](https://www.getpostman.com/) to launch the requests

For python version, you may run :

```console
$ python --version
```

which should return

```console
$ python --version
Python 3.6.7
```

or higher.

Don't forget to satisfied the requirements

```console
$ pip install -r requirements.txt
```

## How to

Launch the example of the preparation codes :
```console
$ cd kmeans
$ python main.py
```

To launch the number API :

```console
$ cd transform
$ python api.py
```

To launch the TF-IDF API :

```console
$ cd categorize
$ python main.py
```

It launch (by default) on 127.0.0.1:5000/ and 127.0.0.1:5050/
This the list of use for the API on POSTMAN:

POST: http://127.0.0.1:5000/image/ 

send this in body (don't forget this is a JSON content!)->

```
{
    "image": [255.0, 255.0, 255.0, 254.9976, 179.8104, 183.1008, 247.7772, 217.602, 213.6828, 162.7584, 180.468, 238.3296, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 254.99625, 255.0, 198.466875, 169.86375, 249.721875, 234.99, 247.569375, 178.693125, 138.62625, 218.859375, 169.71375, 244.51875, 250.828125, 214.629375, 197.04, 205.74375, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 254.985, 255.0, 255.0, 255.0, 212.1375, 193.95, 243.6375, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 234.0, 92.73, 150.2175, 91.65, 233.8875, 255.0, 255.0, 174.96, 225.2775, 255.0, 238.8975, 106.155, 253.74, 137.5425, 207.15, 255.0, 255.0, 125.115, 215.7675, 255.0, 255.0, 114.72, 88.365, 74.8575, 192.975, 220.3125, 208.2975, 90.4425, 252.3075, 255.0, 255.0, 238.3125, 191.445, 157.0725, 147.51, 130.65, 133.53, 179.445, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 254.94, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 209.1, 129.45, 121.05, 144.75, 209.79, 254.76, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 228.45, 65.91, 63.99, 76.17, 63.75, 63.75, 114.42, 245.91, 255.0, 255.0, 255.0, 255.0, 255.0, 249.03, 169.62, 231.33, 255.0, 255.0, 255.0, 255.0, 197.55, 63.75, 177.27, 252.36, 208.59, 124.68, 63.75, 179.64, 255.0, 255.0, 255.0, 255.0, 255.0, 217.44, 63.75, 159.78, 255.0, 255.0, 255.0, 255.0, 206.43, 63.75, 163.86, 255.0, 255.0, 228.42, 63.75, 159.3, 255.0, 255.0, 255.0, 255.0, 255.0, 214.56, 63.75, 159.78, 255.0, 255.0, 255.0, 255.0, 239.16, 63.75, 133.26, 255.0, 249.96, 194.25, 63.75, 159.3, 255.0, 255.0, 255.0, 255.0, 255.0, 158.4, 63.75, 193.29, 255.0, 255.0, 255.0, 255.0, 255.0, 123.51, 94.08, 144.75, 81.21, 63.75, 63.99, 198.3, 255.0, 255.0, 255.0, 255.0, 255.0, 99.81, 75.45, 244.23, 255.0, 255.0, 255.0, 255.0, 255.0, 177.54, 63.75, 63.75, 63.75, 63.75, 107.94, 159.3, 159.3, 181.08, 190.17, 159.78, 163.41, 69.72, 116.79, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 247.11, 196.14, 151.44, 104.34, 76.38, 63.75, 63.75, 63.75, 63.75, 63.75, 63.75, 63.75, 63.75, 167.49, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 252.36, 235.8, 235.8, 226.74, 197.55, 197.55, 208.11, 198.51, 232.26, 254.28, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0, 255.0]
}
```

POST: http://127.0.0.1:5050/file/

send ONE of this in body (don't forget this is a JSON content!)->

```
{
    "title": "Calamars_frits",
    "content": "Etape 1 Coupez les calamars en rondelles et laissez les macérer dans un peu de jus de citron et d'huile avec du sel et du poivre pendant 30 mn. Etape 2 Séchez-les autant que possible avec du papier essuie-tout, puis passez-les dans la farine, les oeufs battus et à nouveau dans la farine. Etape 3 Faites-les frire dans l'huile bien chaude jusqu'à ce qu'ils soient dorés."
}

{
    "title": "Courgettes_au_barbecue",
    "content": "Etape 1 Coupez les courgettes en tranches de 5 mm dans le sens de la longueur (garder la peau), assaisonnez avec le sel (pas trop) et les herbes de Provence. Etape 2 Faites griller sur la grille du barbecue environs 5 min par côté (en fonction de la hauteur de la grille), retirez quand on commence à voir les traces noires de la grille (avant qu'elles ne soient trop sèches). Etape 3 Servir aussitôt avec un peu de crème fraîche assaisonnée d'herbes et de sel."
}


{
    "title": "Mousse_glacée_aux_cerises",
    "content": "Etape 1 Avec un blender : Etape 2 Mixer ensemble les cerises dénoyautées, le jus de citron et le sucre jusqu'à l'obtention d'une crème liquide onctueuse. Etape 3 Battre la crème fraîche et incorporer le tout. Etape 4 Mettre dans un moule choisi et décorer à loisir. (en photo un exemple de décoration avec des confiseries) Etape 5 Mettre au congélateur pour environ 3 heures. Etape 6 Sans blender : Etape 7 Il est conseillé de laisser le sucre fondre un peu à froid dans les cerises dénoyautées et le jus de citron avant de mixer."
}

{
    "title": "Mousse_glacée_aux_cerises",
    "content": "Etape 1 Avec un blender : Etape 2 Mixer ensemble les cerises dénoyautées, le jus de citron et le sucre jusqu'à l'obtention d'une crème liquide onctueuse. Etape 3 Battre la crème fraîche et incorporer le tout. Etape 4 Mettre dans un moule choisi et décorer à loisir. (en photo un exemple de décoration avec des confiseries) Etape 5 Mettre au congélateur pour environ 3 heures. Etape 6 Sans blender : Etape 7 Il est conseillé de laisser le sucre fondre un peu à froid dans les cerises dénoyautées et le jus de citron avant de mixer."
}

{
    "title": "Crumble_à_la_rhubarbe_et_aux_fraises",
    "content": "Etape 1: Couper la rhubarbe en tronçons de 1 à 2 cm de long. Etape 2: Couper les fraises en 2, si elles sont trop grosses. Etape 3: Beurrer un plat à four. Etape 4: Disposer rhubarbe et fraises dans le plat, parsemer de petits morceaux d'écorces d'orange confite. Etape 5: Faire des grumeaux avec ses mains avec le beurre (ramolli), la farine et le sucre et en recouvrir les fruits sur 1 centimètre d'épaisseur. Etape 6: Faire cuire à four moyen entre une 1/2 h et 3/4 d'h. Il faut que le dessus soit bien doré. Etape 7: Servir chaud avec la crème liquide montée en Chantilly."
}
```

GET: http://127.0.0.1:5050/result/
