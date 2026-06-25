from pathlib import Path
from ..database import load_notes


def export_markdown():
    notes = load_notes()

    if not notes:
        print("Aucune note à exporter.")
        return

    # dossier de sortie
    output_dir = Path.cwd() / "notes"
    output_dir.mkdir(exist_ok=True)

    for n in notes:
        file_path = output_dir / f"note_{n['id']}.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Note {n['id']}\n\n")

            # metadata
            f.write("---\n")
            f.write(f"author: {n.get('author', 'unknown')}\n")
            f.write(f"date: {n.get('date', 'unknown')}\n")
            f.write("---\n\n")

            # contenu
            f.write(n["content"] + "\n")

    print(f"Export terminé dans le dossier : {output_dir}")