# Présentation 

Notepad en python dockerisé.

# install commande

 1   git push https://github.com/cs2ip-20-vandeweghe-loic/noteMakerPy/tree/main

 2   cd ./docker

 3   sudo docker compose up -d

# Alias 

Collez cet alias afin de pouvoir utiliser la commande "note" dans votre CLI

alias note="docker compose -f docker/compose.yaml run --rm note-maker"

# upgrade commande

pipx upgrade note

# execute script

note

# execute docker

docker compose -f docker/compose.yaml build

