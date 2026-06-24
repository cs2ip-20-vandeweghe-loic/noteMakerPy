import sys

from .function.add import add_note
from .function.list import list_notes
from .function.delete import delete_note


def usage():
    print("Usage:")
    print("  note -a    Ajouter une note")
    print("  note -ps   Afficher les notes")
    print("  note -d    Supprimer une note")


def main():
    if len(sys.argv) != 2:
        usage()
        return

    cmd = sys.argv[1]

    if cmd == "-a":
        add_note()
    elif cmd == "-ps":
        list_notes()
    elif cmd == "-d":
        delete_note()
    else:
        usage()


if __name__ == "__main__":
    main()