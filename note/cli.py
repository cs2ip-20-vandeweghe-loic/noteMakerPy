from .function.add import add_note
from .function.list import list_notes
from .function.delete import delete_note
from .function.export_markdown import export_markdown
import argparse


def main():
    # init
    parser = argparse.ArgumentParser(prog="note")

    subparsers = parser.add_subparsers(dest="command")

    # ADD
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("content", type=str, nargs="?", default=None, help="Contenu de la note")

    # LIST
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("id", type=int, nargs="?", default=None, help="ID de la note")

    # DELETE
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument(
        "target",
        nargs="?",
        default=None,
        help="ID de la note ou 'all'"
    )

    # EXPORT
    parser_export = subparsers.add_parser("export")
    parser_export.add_argument(
        "format",
        choices=["markdown"],
        help="Format d'export"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.content)

    elif args.command == "list":
        list_notes(args.id)

    elif args.command == "delete":
        delete_note(args.tar)
    elif args.command == "export":
        if args.format == "markdown":
            export_markdown()

    else:
        parser.print_help()



if __name__ == "__main__":
    main()