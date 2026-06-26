# Présentation 

Notepad en python dockerisé.

# Installation

Vous pouvez télécharger le container via la commande ci-dessous :

```
docker pull ghcr.io/cs2ip-20-vandeweghe-loic/note-maker:main
```

Si vous resentez le besoins de télécharger manuellement le dépot, veuillez suivre les étapes suivantes :

```
 1   git pull https://github.com/cs2ip-20-vandeweghe-loic/noteMakerPy/tree/main

 2   cd ./docker

 3   sudo docker compose up -d
```
# Executer docker
```
docker compose -f docker/compose.yaml build
```
# Alias 

Collez cet alias afin de pouvoir utiliser la commande "note" dans votre CLI
```
alias note="docker compose -f docker/compose.yaml run --rm note-maker"
```

# Structure des commandes
```
usage: note [-h] {add,list,delete,export} ...

positional arguments:
  {add,list,delete,export}

options:
  -h, --help            show this help message and exit
```

# Divers

Pour toutes autres questions, n'hésitez pas à nous contacter 