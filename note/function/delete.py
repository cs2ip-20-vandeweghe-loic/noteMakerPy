from ..database import load_notes, save_notes


def delete_note():
    notes = load_notes()

    if not notes:
        print("Aucune note enregistrée.")
        return

    try:
        note_id = int(input("ID à supprimer : "))
    except ValueError:
        print("ID invalide")
        return

    new_notes = [n for n in notes if n["id"] != note_id]

    if len(new_notes) == len(notes):
        print("Note introuvable")
        return

    save_notes(new_notes)
    print(f"Note #{note_id} supprimée.")