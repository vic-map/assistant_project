import contacts_f
import notes_f
import files_f

# default_contact_path = "contacts/"
default_notes_path = "notes/"
message = "operation failed"


# def input_error(func):
#     def inner(input_text):
#         try:
#             result = func()
#             return result
#         except KeyError:
#             print('Enter correct user name')
#         except TypeError:
#             print('Enter correct command')
#         except ValueError:
#             print("Give me name and phone please")
#         except IndexError:
#             print("Give me name and phone please")
#     return inner


# @input_error
def input_parcer(text):

    input_tasks = {
        'hello': hello,
        'hi': hello,
        'add-contact': contacts_f.add_contact,
        "find-contact": contacts_f.find_contact,
        "del-contact": contacts_f.deleting_contact,
        "show-all-contacts": contacts_f.show_all,
        "show-bdays": contacts_f.find_b_days,
        "change-name": contacts_f.change_name,
        "add-phone": contacts_f.add_phone,
        "add-email": contacts_f.add_email,
        # "del-pnone": contacts_f.remove_phone,
        # "del-email": contacts_f.remove_email,
        "set-address": contacts_f.set_address,
        "set-bday": contacts_f.set_b_day,
        "write-note": notes_f.write_note,
        "change-note": notes_f.change_note,
        # "edit-note": notes_f.edit_note,
        "add-note-tag": notes_f.add_tag,
        "find-tag": notes_f.find_tag,
        "find-note": notes_f.find_note,
        # "read-note": notes_f.read_note,
        "del-note": notes_f.remove_note,
        "del-tag": notes_f.remove_tag,
        "sort-folder": files_f.scan,  # ???????????
        'goodbye': close_all,
        "close": close_all,
        "exit": close_all,
        '.': close_all,
        'help': helptext
    }

    task = input_text.split(sep=': ')[0].lower()

    if len(input_text.split(sep=': ')) > 1:
        arguments = input_text.lower().split(sep=': ')[1]
        return input_tasks.get(task)(arguments)
    return input_tasks.get(task)()


def hello():
    return 'How can I help you?'


def helptext():
    text = 'HELP!!!'
    print(text)


def close_all():
    message = 'Goodbye!'
    return message


if __name__ == "__main__":

    welcome_text = f"---\nHello. I'm CLI bot.\nThe commands are:\n\n---"

    print(welcome_text)

    while True:
        input_text = input('Input your command: ')
        answer = input_parcer(input_text)
        print(answer)
        if answer == 'Goodbye!':
            break
