DEFAULT_ADDRESS_BOOK_PATH = ".address_book.bin"


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("you don't have an address book yet")
        return address_book()


def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


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
def input_parcer():

    input_tasks = {
        'hello': hello,
        'add': add,
        "change": change,
        "phone": phone,
        "show": show_all,
        "good": close_all,
        "close": close_all,
        "exit": close_all,
        '.': close_all
    }

    task = input_text.rsplit(sep=' ')[0].lower()
    task_to_do = input_tasks.get(task)
    return task_to_do(input_text)


@input_error
def hello():
    message = 'How can I help you?'
    return message


@input_error
def add():
    name = input_text.split(sep=' ')[1]
    phone = input_text.split(sep=' ')[2]
    address_book[name] = phone
    message = 'phone has been added'
    return message


@input_error
def change():
    name = input_text.split(sep=' ')[1]
    phone = input_text.split(sep=' ')[2]
    address_book[name] = phone
    message = 'phone has been changed'
    return message


@input_error
def phone():
    name = input_text.split(sep=' ')[1]
    message = address_book[name]
    return message


@input_error
def show_all():
    message = ''
    for name, phone in address_book.items():
        message += name + '  ' + phone + "\n"
    return message.rstrip()


@input_error
def close_all():
    dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
    message = 'Good bye!'
    return message
