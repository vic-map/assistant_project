import contacts
import json


def input_parcer():

    input_tasks = {
        'hello': hello,
        'add-contact': add_contact,
        "change-pnone": change_phone,
        "add-phone": phone,
        "show-all": show_all,
        "show-bdays": find_b_days,
        "find-contact": find_contact,
        "change-contact": change_contact,
        "del-contact": deleting_contact,
        "good": close_all,
        "close": close_all,
        "exit": close_all,
        '.': close_all,
        'help': helptext,
    }

    task = input_text.rsplit(sep=' ')[0].lower()
    task_to_do = input_tasks.get(task)
    return task_to_do(input_text)


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
