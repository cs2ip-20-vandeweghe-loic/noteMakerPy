from ..database import load_notes
from collections import defaultdict


def list_notes(id=None):
    notes = load_notes()

    if not notes:
        print("Aucune note enregistrée.")
        return

    # une note
    if id is not None:
        for note in notes:
            if note["id"] == int(id):
                print(f"[{note['id']}] {note['content']} ({note['category']})")
                print(f"({note['author']} - {note['date']})")
                return
        print(f"Aucune note trouvée avec l'id {id}")
        return

    # toutes les notes
    grouped = defaultdict(list)

    for note in notes:
        grouped[note.get("category", "general")].append(note)

    for category, items in grouped.items():
        print(f"\n {category}")
        for note in items:
            print(f"  - [{note['id']}] {note['content']}")
            print(f"  ({note['author']} - {note['date']})")
