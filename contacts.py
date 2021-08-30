
from datetime import timedelta
from datetime import datetime
import re
from pathlib import Path


class Contact():

    DEFAULT_CONTACTS_PATH = '/contacts'

    def __init__(self, name):

        self.name = name
        self.address = None
        self.phones = []
        self.birthday = None
        self.email = []
        self.sequence_number = 0  # ??????????

    @property
    def name(self):
        return self.name

    @property
    def phones(self):
        return self.phones

    @property
    def birthday(self):
        return self.birthday

    @phones.setter
    def add_phones(self, new_value):

        if new_value in self.phones:
            print(f'{new_value} already exists')
        else:
            self.phones.append(new_value)

    @birthday.setter
    def set_birthday(self, new_value):

        if isinstance(new_value, datetime(year, month, day)):
            self.birthday = new_value
        else:
            print(f'{new_value} is not datetime object')

    def dump_contact(self, name, address, phones, birthday, email):

        new_contact = Contact(name, address, phones, birthday, email)
        path = Path(DEFAULT_CONTACTS_PATH + '/' + name)
        with open(path, "w") as f:
            json.dumps(new_contact, f)

    def find_b_days():
        interval = int(input('enter en interval: '))
        for record in DEFAULT_CONTACTS_PATH.iterdir():
            current_contact = get_contact(record)
            birthday = current_contact['birthday']
            if interval <= days_to_birthday(birthday):
                print current_contact
        message = 'there are no more birthdays'
        return message

    def get_contact(path):
        contact = json.loads(path)
        return contact

    def phones_checkup(phones):
        for phone_number in phones:
            checkup = re.findall(
                r"\+380\(\d{2}\)\d{3}\-\d{2}\-\d{2}|\+380\(\d{2}\)\d{3}\-\d{1}\-\d{3}", phone_number)
            if checkup:
                return True
            else:
                return False

    def emails_checkup(email):
        checkup = re.findall(
            r'[a-zA-Z]+[a-zA-Z0-9_.]+@{1}[a-z]+\.[a-z]{2,}', text)
        if checkup:
            return True
        else:
            return False

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
    def hello():
        message = 'How can I help you?'
        return message

    @input_error
    def add_contact():
        contact = input('enter name,address,phones,birthday,email: ')
        name = contact.split(sep=',')[1]
        address = contact.split(sep=',')[2]
        phones = contact.split(sep=',')[3].split(sep=' ')
        birthday = contact.split(sep=',')[4]
        email = contact.split(sep=',')[5].split(sep=' ')
        if phones_checkup(phones) and email_checkup(email):
            Contact.dump_contact(self, name, address, phones, birthday, email)
            message = 'contact has been added'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    def days_to_birthday(self, birthday):
        if birthday < datetime.now().date():
            nextbday = datetime(year=datetime.now().year,
                                month=birthday.month, day=birthday.day).date()
            if datetime.now().date() > nextbday:
                nextbday = datetime(year=datetime.now().year+1,
                                    month=birthday.month, day=birthday.day).date()
            return (nextbday - datetime.now().date()).days

    @input_error
    def change_phone():

        # name = input_text.split(sep=' ')[1]
        # phone = input_text.split(sep=' ')[2]

        if phones_checkup(phones):
            # address_book[name] = phone
            message = 'phone has been changed'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    @input_error
    def change_email():

        # name = input_text.split(sep=' ')[1]
        # email = input_text.split(sep=' ')[2]

        if emails_checkup(emails):
            # address_book[name] = phone
            message = 'email has been changed'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    @input_error
    def add_phone():

        if phones_checkup(phones):
            # address_book[name] = phone
            message = 'phone has been added'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    def find_contact(text):
        message = "there isn't such contact"
        for record in DEFAULT_CONTACTS_PATH.iterdir():
            if text == get_contact(record)['name']:
                print get_contact(record)
                message = "serch comlited"
        return message

    def change_contact():
        pass

    def deleting_contact():
        pass

    # @input_error
    # def show_all():
    #     message = ''
    #     for name, phone in address_book.items():
    #         message += name + '  ' + phone + "\n"
    #     return message.rstrip()

    # def add_phone(self, phone):
    #     pass

    # def del_phone(self, phone):
    #     pass

    # def edit_phone(self, phone):
    #     pass

    # def __iter__():
    #     return Contact()

    # def __next__(self, quantity):

    #     if self.sequence_number < len(AddressBook.data):

    #         result = []

    #         for i in range(quantity):

    #             result.append(AddressBook.data[sequence_number])

    #             self.sequence_number += 1
    #         return result

    #     raise StopIteration()
