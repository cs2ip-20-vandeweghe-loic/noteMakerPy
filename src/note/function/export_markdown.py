from pathlib import Path
from collections import defaultdict
from ..database import load_notes


def export_markdown():
    notes = load_notes()

    if not notes:
        print("Aucune note à exporter.")
        return

    output_dir = Path.cwd() / "notes"
    output_dir.mkdir(exist_ok=True)

    grouped = defaultdict(list)

    for n in notes:
        grouped[n.get("category", "general")].append(n)

    for category, items in grouped.items():
        file_path = output_dir / f"{category}.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Catégorie : {category}\n\n")

            for n in items:
                f.write(f"## Note {n['id']}\n")
                f.write("---\n")
                f.write(f"author: {n.get('author')}\n")
                f.write(f"date: {n.get('date')}\n")
                f.write("---\n")
                f.write(f"{n['content']}\n\n")

    print(f"Export terminé dans {output_dir}")