# Présentation

Notepad en python dockerisé.

# Documentation

Veuillez vous réferer à cette [documentation](https://github.com/cs2ip-20-vandeweghe-loic/noteMakerDoc) pour tout autre question sur le projet.

# Installation local non dockerisé

```
pipx install -e
```

# Installation dockerisé

Vous pouvez télécharger le container via la commande ci-dessous :

```
docker pull ghcr.io/cs2ip-20-vandeweghe-loic/note-maker:main

docker run note-maker
```

Si vous ressentez le besoins de télécharger manuellement le dépot, veuillez suivre les étapes suivantes :

```
 1   git pull https://github.com/cs2ip-20-vandeweghe-loic/noteMakerPy/tree/main

 2   cd ./docker

 3   sudo docker compose up -d
```

# Création du script bash docker

```
Création d'un fichier note contenant :

#!/bin/sh

mkdir -p "$HOME/.note-maker"

docker run --rm \
    -v "$HOME/.note-maker:/data" \
    -e NOTES_DB=/data/.notes.json \
    -e NOTES_EXPORT_DIR=/data/notes \
    note-maker "$@"
```

# Rendre le script executable

```
chmod +x note
```

# Installation du script local

```
mkdir -p ~/.local/bin
mv note ~/.local/bin/
```

# Structure des commandes

```
usage: note [-h] {add,list,delete,export} ...

positional arguments:
  {add,list,delete,export}

options:
  -h, --help            show this help message and exit
```
