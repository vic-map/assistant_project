
from datetime import timedelta
from datetime import datetime
import re
from pathlib import Path
import os
import json
import pickle


class Contact():
    DEFAULT_PATH = "PY\\assistant_project\\contacts\\"
    last_contact = ''

    def __init__(self, name, address, phones, birthday, email):

        self.address = None

        self.email = []

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes

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
        path = Path('PY\\assistant_project\\contacts\\' + name + '.json')
        print(path)
        with open(path, "wb") as fh:
            pickle.dump(new_contact, fh)

    def get_contact(name):
        path = Path('PY\\assistant_project\\contacts\\' + name + '.json')
        with open(path, 'rb') as fh:
            contact = str(pickle.load(fh))
        # last_contact = contact['name']
        print(contact)
        return contact

    def find_b_days():
        interval = int(input('enter en interval: '))
        for record in DEFAULT_CONTACTS_PATH.iterdir():
            current_contact = get_contact(record)
            birthday = current_contact['birthday']
            if interval <= days_to_birthday(birthday):
                print(current_contact)
        message = 'there are no more birthdays'
        return message

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

    # @input_error
    def add_contact(arguments):
        print(arguments)
        name = arguments.split(sep=', ')[0]
        address = arguments.split(sep=', ')[1]
        phones = arguments.split(sep=', ')[2]
        birthday = arguments.split(sep=', ')[3]
        email = arguments.split(sep=', ')[4]
        new_contact = Contact(name, address, phones, birthday, email)
        # if Contact.phones_checkup(phones) and Contact.email_checkup(email):
        #     Contact.dump_contact(self, name, address, phones, birthday, email)
        #     message = 'contact has been added'
        # else:
        #     message = 'check oyur input, smth is incorrect'

        new_contact.dump_contact(name, address, phones, birthday, email)

        message = 'contact has been added'
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

        if emails_checkup(emails):
            # address_book[name] = phone
            message = 'email has been changed'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    @input_error
    def add_phone(name, value):
        contact = get_contact(name)
        if phones_checkup(phones):
            contact.phone.append(value)
            message = 'phone has been added'
        else:
            message = 'check oyur input, smth is incorrect'
        return message

    def find_contact(text):
        message = "there isn't such contact"
        for record in DEFAULT_CONTACTS_PATH.iterdir():
            if text == get_contact(record)['name']:
                print(get_contact(record))
                message = "serch comlited"
        return message

    @input_error
    def change_contact(name, attribute, value):

        contact = get_contact(name)
        contact.attribute = value
        dump_contact(self, name, address, phones, birthday, email)
        message = 'contact has been chenged'
        return message

    def deleting_contact(name):
        os.remove(DEFAULT_CONTACTS_PATH + '/' + name)
        pass

    def show_all():

        for item in DEFAULT_CONTACTS_PATH.iterdir():
            print(get_contact(item))
        return message.rstrip()
