from ..database import load_notes


def list_notes(idNote=None):
    notes = load_notes()

    if not notes:
        print("Aucune note enregistrée.")
        return

    if not idNote:
        print("Liste des notes :")
        for n in notes:
            print(f"[{n['id']}] {n['content']}")
        return

    note_id = int(idNote[0])

    for n in notes:
        if n["id"] == note_id:
            print(f"[{n['id']}] {n['content']}")
            return

    print(f"Aucune note trouvée avec l'id {note_id}")