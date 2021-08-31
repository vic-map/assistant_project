import json
from pathlib import Path


NOTES = []


def write_notes():
    title = input("File name is: ")
    notes = input("Text: ")
    tags = input("Write tags: ")
    filename = f"{title}.json"
    with open(filename, "w") as fh:
        json.dump({'notes': notes, 'tags': [tags]}, fh)


def find_notes(folder: Path):
    for item in folder.iterdir():
        if item.is_file():
            NOTES.append(item)
    return NOTES


def delete_notes(filename):
    file_path = Path(filename)
    try:
        file_path.unlink()
    except OSError as e:
        print("Ошибка: %s : %s" % (file_path, e.strerror))


def change_notes(filename):
    with open(filename, 'r') as f:
        notes = json.load(f)
        notes['notes'] = input()
    with open(filename, "w") as fh:
        json.dump(notes, fh)


def add_tags(filename):
    with open(filename, 'r') as f:
        tags = json.load(f)
        result = tags['tags']
        result.append(input())
    with open(filename, "w") as fh:
        json.dump(tags, fh)


def find_and_sort_by_tags():
    pass


# write_notes()  # потрібно бути в папці з нотатками
# find_notes(Path('notes\\')) # потрібно бути на рівень вище ніж папка з нотатками
# delete_notes("Тут має бути назва файлу") # потрібно бути в папці з нотатками
# print(change_notes('1.json'))  # потрібно бути в папці з нотатками
# add_tags('1.json')  # потрібно бути в папці з нотатками
# print(find_and_sort_by_tags())
