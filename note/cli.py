import sys

from .function.add import add_note
from .function.list import list_notes
from .function.delete import delete_note


def usage():
    print("Usage:")
    print("  note add       Ajouter une note")
    print("  note list      Afficher les notes")
    print("  note delete    Supprimer une note")
    print(f"[{sys.argv}]")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1]

    if cmd == "add":
        add_note(sys.argv[2:])
    elif cmd == "list":
        list_notes(sys.argv[2:])
    elif cmd == "delete":
        delete_note()
    else:
        usage()


if __name__ == "__main__":
    main()