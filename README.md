# Présentation 

Notepad en python dockerisé.

# Installation
```
 1   git push https://github.com/cs2ip-20-vandeweghe-loic/noteMakerPy/tree/main

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
