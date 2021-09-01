import json
from pathlib import Path


default_notes_path = '\\notes\\'


# write_note()  # потрібно бути в папці з нотатками
# find_note(Path('notes\\')) # потрібно бути на рівень вище ніж папка з нотатками
# delete_notes("Тут має бути назва файлу") # потрібно бути в папці з нотатками
# print(change_note('1.json'))  # потрібно бути в папці з нотатками
# add_tag('1.json')  # потрібно бути в папці з нотатками
# print(find_and_sort_by_tag())


# ========= Yura ========


def write_note(title, tags, text):
    note = {'name': title, 'tags': tags, 'text': text}
    message = dump_note(note)
    return message


def dump_note(note):
    path = default_note_path + note['name'] + '.json'
    with open(path, "w") as fh:
        json.dump(note, fh)
        message = f"note {note['name']} has been written"
    return message


def read_note(title):
    filename = title + '.json'
    for item in default_notes_path.iterdir():
        if item == filename:
            message = get_note(title)['text']
    return message


def get_note(title):
    path = default_note_path + title + '.json'
    with open(path, 'r') as fh:
        note = json.load(fh)
    return note


def find_note(title):
    filename = title + '.json'
    for item in default_notes_path.iterdir():
        if item == filename:
            message = get_note(title)
    return message


def change_note(title, text):
    note = get_note(title)
    note['text'] = text
    dump_note(note)
    message = f"note {note['name']} has been changed"
    return message


def edit_note(title):
    pass


def remove_note(title):
    path = default_note_path + title + '.json'
    path.unlink()
    message = f'the note {title} has been removed'
    return message
#


def add_tag(title, tag):
    note = get_note(title)
    if tag in note['tags']:
        message = f'there is such tag in the note {title}'
    else:
        note['tags'].append(tag)
        dump_note(note)
        message = f'the tag {tag} was added to note {title}'
    return message


def remove_tag(title, tag):
    note = get_note(title)
    if tag in note['tags']:
        note['tags'].remove(tag)
        dump_note(note)
        message = f'the tag {tag} was removed from note {title}'
    else:
        message = f"the tag {tag} is not exist in note {title}"
    return message


def find_tag(tag):
    note_list = []
    for item in default_notes_path.iterdir():
        note = get_note(item.pref())
        if tag in note['tags']:
            note_list.append(note['name'])
            message = f"the {tag} is in notes:\n {note_list.sort()}"
    return message
