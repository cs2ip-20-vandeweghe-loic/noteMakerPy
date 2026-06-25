from pathlib import Path
import json
import os


DB_FILE = Path(os.getenv("NOTES_DB", Path.home() / ".notes.json"))


def load_notes():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as data:
            return json.load(data)
    return []


def save_notes(notes):
    with open(DB_FILE, "w", encoding="utf-8") as data:
        json.dump(notes, data, indent=4, ensure_ascii=False)