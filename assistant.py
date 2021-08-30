import contacts
import json


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
        'add-contact': contacts.Contact.add_contact,
        'get-contact': contacts.Contact.get_contact,
        "change-pnone": contacts.Contact.change_phone,
        "add-phone": contacts.Contact.add_phone,
        "show-all-contacts": contacts.Contact.show_all,
        "show-bdays": contacts.Contact.find_b_days,
        "find-contact": contacts.Contact.find_contact,
        "change-contact": contacts.Contact.change_contact,
        "del-contact": contacts.Contact.deleting_contact,
        "good": close_all,
        "close": close_all,
        "exit": close_all,
        '.': close_all,
        'help': helptext,
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

    # address_book = {'Vic': '123', 'Inn': '456', 'Len': '789'}

    welcome_text = "---\nHello. I'm CLI bot.\nThe commands are:\nhello; add; change ... ; phone ... ; show all; good bye; close; exit; and '.'\n---"

    print(welcome_text)

    while True:
        input_text = input('Input your command: ')
        answer = input_parcer(input_text)
        print(answer)
        if answer == 'Good bye!':
            break
