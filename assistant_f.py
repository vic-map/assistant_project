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
        'get-contact': contacts_f.get_contact,
        "change-pnone": contacts_f.change_phone,
        "add-phone": contacts_f.add_phone,
        "show-all-contacts": contacts_f.show_all,
        "show-bdays": contacts_f.find_b_days,
        "change-contact": contacts_f.change_contact,
        "del-contact": contacts_f.deleting_contact,
        # "write-note": write_note,
        # "change-note": change_note,
        # "edit-note": edit_note,
        # "add-note-tag": add_tag,
        # "find_tag": find_tag,
        # "find-note": find_note,
        # "read-note": read_note,
        # "del-note": remove_note,
        # "del-tag": remove_tag,
        # "sort-folder": files_f.scan,  # ???????????
        # "goodbye": close_all,
        # "close": close_all,
        # "exit": close_all,
        # '.': close_all,
        # 'help': helptext,
    }
    task = input_text.rsplit(sep=': ')[0].lower()

    if len(input_text.rsplit(sep=': ')) > 1:
        arguments = input_text.lower().rsplit(sep=': ')[1]
        return input_tasks.get(task)(arguments)
    return input_tasks.get(task)()


def hello():
    return 'How can I help you?'


def helptext():
    text = 'HELP!!!'
    print(text)


def close_all():
    message = 'Good bye!'
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
