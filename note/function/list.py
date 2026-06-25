from ..database import load_notes


def list_notes(id=None):
    notes = load_notes()

    if not notes:
        print("Aucune note enregistrée.")
        return

    if not id:
        print("Liste des notes :")
        for n in notes:
            print(
                f"[{n['id']}] {n['content']} "
                f"({n['author']} - {n['date']})"
            )
        return

    note_id = int(id)

    for n in notes:
        if n["id"] == note_id:
            print(
                f"[{n['id']}] {n['content']} "
                f"({n['author']} - {n['date']})"
            )
            return

    print(f"Aucune note trouvée avec l'id {note_id}")