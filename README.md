Besoin de python

# Prérequis

python, pipx

# install commande

pipx install -e .

# upgrade commande

pipx upgrade note

# execute script

note

# execute docker

docker compose -f docker/compose.yaml build

# using note via docker create an alias

alias note="docker compose -f docker/compose.yaml run --rm note-maker"
