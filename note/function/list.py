from ..database import load_notes


def list_notes():
    notes = load_notes()

    if not notes:
        print("Aucune note enregistrée.")
        return

    print("Liste des notes :")
    for n in notes:
        print(f"[{n['id']}] {n['content']}")