# 🧠 E.L.S.A (Electronic Learning and Scrapping Algorithm)
Un algorithme capable d'interagir avec le réseau mondial de la connaissance en utilisant des sources de données locales sur la machine. Le programme permet d'accéder à un dictionnaire portable avec un nombre illimité d'informations sans utiliser une connexion Internet.

![Demo 1](https://raw.githubusercontent.com/thisiskeanyvy/ELSA/main/demo/demo1.png)

------

# 💻 Comment fonctionne l'algorithme ?

E.L.S.A utilise des datasets qui sont des fichiers contenant les informations qui sont encodées en base64. Ces fichiers peuvent être stockés localement sur la machine de l'utilisateur dans le dossier `'data/'`, ce qui permet à l'algorithme de trouver les informations sans avoir besoin d'une connexion Internet. Le programme utilise ensuite une méthode de recherche utilisant la structure JSON afin de trouver les informations dans les datasets puis renvoie les résultats à l'utilisateur.

------

# 📦 Installation et utilisation

## - Windows/MacOs :

_1. Installer les bibliothèques Python pré-requises :_
```shell
$ curl -sL https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/requirements.txt && pip install -r requirements.txt
```
_2. Télécharger le fichier exécutable :_
```shell
$ curl -sL https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/elsa_v1.0.pyc
```
_3. Télécharger les datasets et décompresser l'archive :_
```shell
$ curl -sL https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/elsa_v1.0_datasets.tar.gz && tar xzvf elsa_v1.0_datasets.tar.gz
```
_4. Démarrer l'algorithme :_
```shell
$ python elsa_v1.0.pyc
```
------

## - Linux/Android (Termux) :

_1. Installer les bibliothèques Python pré-requises :_
```shell
$ wget https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/requirements.txt && pip3 install -r requirements.txt
```
_2. Télécharger le fichier exécutable :_
```shell
$ wget https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/elsa_v1.0.pyc
```
_3. Télécharger les datasets et décompresser l'archive :_
```shell
$ wget https://github.com/thisiskeanyvy/ELSA/releases/download/v1.0/elsa_v1.0_datasets.tar.gz && tar xzvf elsa_v1.0_datasets.tar.gz
```
_4. Démarrer l'algorithme :_
```shell
$ python3 elsa_v1.0.pyc
```
------

# 🔨 Contribution pour les développeurs

------

## ✅ Mise en place de l'environnement :
_1. Cloner le dépôt Github :_
```shell
$ git clone https://github.com/thisiskeanyvy/ELSA/
```
_2. Naviguer vers le dossier du projet :_
```shell
$ cd ELSA/
```
_3. Installer les bibliothèques Python pré-requises :_
```shell
$ pip3 install -r requirements.txt
```

------

## 🚧 Compiler le code source
_Pour compiler le code source en un exécutable, vous pouvez utiliser la commande suivante :_

```shell
$ python3 build.py
```

