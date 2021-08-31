
from datetime import timedelta
from datetime import datetime
import re
from pathlib import Path
import os
import json
import pickle


default_contact_path = "PY\\assistant_project\\contacts\\"
# last_contact = ''


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


def add_contact(arguments):
    new_contact = {}
    new_contact['name'] = arguments.split(sep=', ')[0]
    new_contact['address'] = arguments.split(sep=', ')[1]
    new_contact['phones'] = arguments.split(sep=', ')[2]
    new_contact['birthday'] = arguments.split(sep=', ')[3]
    new_contact['email'] = arguments.split(sep=', ')[4]
    # new_contact = {'name', 'address', 'phones', 'birthday', 'email'}
    if phones_checkup(phones) and email_checkup(email):
        dump_contact(new_contact)
        message = 'contact has been added'
    else:
        message = 'check oyur input, smth is incorrect'
    return message


def find_contact(text):
    message = "there isn't such contact"
    for record in default_contact_path.iterdir():
        if text == get_contact(record)['name']:
            print(get_contact(record))
            message = "serch comlited"
    return message


def dump_contact(contact):

    path = default_contact_path + contact['name'] + '.json'
    # print(path)
    with open(path, "w") as fh:
        json.dump(contact, fh)
    message = 'contact has been written'
    return message


def get_contact(name):
    path = default_contact_path + contact['name'] + '.json'
    with open(path, 'r') as fh:
        contact = json.load(fh)
    # last_contact = contact['name']
    # print(contact)
    return contact


def deleting_contact(name):
    contact = get_contact(name)
    if contact:
        os.remove(default_contact_path + contact['name'] + '.json')
        message = f"the contact {contact['name']} was removed"
    return message


def find_b_days():
    interval = int(input('enter en interval: '))
    for item in default_contact_path.iterdir():
        current_contact = get_contact(item)
        birthday = current_contact['birthday']
        if interval <= days_to_birthday(birthday):
            print(current_contact)
    message = 'there are no more birthdays'
    return message


def days_to_birthday(birthday):
    if birthday < datetime.now().date():
        nextbday = datetime(year=datetime.now().year,
                            month=birthday.month, day=birthday.day).date()
        if datetime.now().date() > nextbday:
            nextbday = datetime(year=datetime.now().year+1,
                                month=birthday.month, day=birthday.day).date()
        return (nextbday - datetime.now().date()).days


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


# -------------------------------------------------------------------------------------------------


@ input_error
def change_contact(name, attribute, value):

    contact = get_contact(name)
    contact.attribute = value
    dump_contact(self, name, address, phones, birthday, email)
    message = 'contact has been chenged'
    return message


@ input_error
def add_phones(name, new_value):
    if phones_checkup(new_value):
        contact = get_contact(name)
        if new_value in contact['phones']:
            message = f'{new_value} already exists'
        else:
            contact['phones'].append(new_value)
            message = 'phone number has been added'
    return message


def set_birthday(ew_value):

    if isinstance(new_value, datetime(year, month, day)):
        self.birthday = new_value
    else:
        print(f'{new_value} is not datetime object')


@ input_error
def change_phone():

    # name = input_text.split(sep=' ')[1]
    # phone = input_text.split(sep=' ')[2]

    if phones_checkup(phones):
        # address_book[name] = phone
        message = 'phone has been changed'
    else:
        message = 'check oyur input, smth is incorrect'
    return message


@ input_error
def change_email():

    if emails_checkup(emails):
        # address_book[name] = phone
        message = 'email has been changed'
    else:
        message = 'check oyur input, smth is incorrect'
    return message


def show_all():

    for item in default_contact_path.iterdir():
        print(get_contact(item))
    return message.rstrip()
