from ..database import load_notes, save_notes
from datetime import datetime
from getpass import getuser


def add_note(newNote=None):
    print("Créer une note")
    if not newNote:
        content = input("> ")
    else:
        content = newNote

    notes = load_notes()

    note_id = 1
    if notes:
        note_id = max(n["id"] for n in notes) + 1

    notes.append({
        "id": note_id,
        "content": content,
        "date": datetime.now().isoformat(timespec="seconds"),
        "author": getuser()
    })

    save_notes(notes)

    print(f"Note #{note_id} enregistrée.")