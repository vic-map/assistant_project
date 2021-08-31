import contacts_f


def input_error(func):
    def inner(input_text):
        try:
            result = func()
            return result
        except KeyError:
            print('Enter correct user name')
        except TypeError:
            print('Enter correct command')
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Give me name and phone please")
    return inner


@input_error
def input_parcer(input_tasks, text):

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

    input_tasks = {
        'hello': hello,
        'hi': hello,
        'add-contact': add_contact,
        'get-contact': get_contact,
        "change-pnone": change_phone,
        "add-phone": add_phone,
        "show-all-contacts": show_all,
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

    welcome_text = f"---\nHello. I'm CLI bot.\nThe commands are:\n{input_tasks.keys()}\n---"

    print(welcome_text)

    while True:
        input_text = input('Input your command: ')
        answer = input_parcer(input_tasks, input_text)
        print(answer)
        if answer == 'Good bye!':
            break
