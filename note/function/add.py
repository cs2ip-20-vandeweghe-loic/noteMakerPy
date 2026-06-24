from ..database import load_notes, save_notes


def add_note():
    print("Créer une note")
    content = input("> ")

    notes = load_notes()

    note_id = 1
    if notes:
        note_id = max(n["id"] for n in notes) + 1

    notes.append({
        "id": note_id,
        "content": content
    })

    save_notes(notes)

    print(f"Note #{note_id} enregistrée.")