
from datetime import timedelta
from datetime import datetime
import re
from pathlib import Path
import os
import json
import pickle

default_contact_path = "PY/assistant_project/contacts/"
message = "operation failed"


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


# @ input_error
def add_contact(arguments):
    contact = {}
    contact['name'] = arguments.split(sep=', ')[0]
    contact['phones'] = arguments.split(sep=', ')[1].split(sep='; ')
    contact['address'] = arguments.split(sep=', ')[2]
    contact['birthday'] = arguments.split(sep=', ')[3]
    contact['emails'] = arguments.split(sep=', ')[4].split(sep='; ')
    if phone_checkup(contact['phones']) and email_checkup('emails'):
        message = dump_contact(contact)
    else:
        message = 'check oyur input, smth is incorrect'
    return message


def find_contact(text):
    message = f'contact {text} not found'
    for item in Path(default_contact_path).iterdir():
        title = item.name.split(sep='.')[0]
        if text == title:
            contact = get_contact(title)
            print_contact(contact)
            message = "serch comlited"
    return message


def print_contact(contact):
    print(
        f"---------- \n - name: {contact['name']}\n -phones: {contact['phones']}\n -address: {contact['address']}\n -birthday: {contact['birthday']}\n -emails: {contact['emails']}")


def dump_contact(contact):

    path = default_contact_path + contact['name'] + '.json'

    with open(path, "w") as fh:
        json.dump(contact, fh)
    message = f"contact {contact['name']} has been written"
    return message


def get_contact(name):
    path = Path(default_contact_path + name + '.json')
    with open(path, 'r') as fh:
        contact = json.load(fh)
    return contact


def deleting_contact(name):
    contact = get_contact(name)
    if contact:
        os.remove(default_contact_path + contact['name'] + '.json')
        message = f"the contact {contact['name']} was removed"
    return message


def find_b_days(text):
    interval = int(text)
    for item in Path(default_contact_path).iterdir():
        contact = get_contact(item.name.split(sep='.')[0])
        if interval >= days_to_birthday(contact['birthday']):
            print(f"{contact['name']} --> {contact['birthday']}")
    message = 'there are no more birthdays'
    return message


def days_to_birthday(birthday_text):
    birthday = datetime.strptime(birthday_text, '%Y-%m-%d').date()
    if birthday < datetime.now().date():
        nextbday = datetime(year=datetime.now().year,
                            month=birthday.month, day=birthday.day).date()
        if datetime.now().date() > nextbday:
            nextbday = datetime(year=datetime.now().year+1,
                                month=birthday.month, day=birthday.day).date()
        return (nextbday - datetime.now().date()).days


def phone_checkup(phones):
    return True
    # print('in phones_checkup')
    # for phone_number in phones:
    #     checkup = re.findall(
    #         r"\+380\(\d{2}\)\d{3}\-\d{2}\-\d{2}|\+380\(\d{2}\)\d{3}\-\d{1}\-\d{3}", phone_number)
    #     if checkup:
    #         return True
    #     else:
    #         return False


def email_checkup(email):

    return True
    checkup = re.findall(
        r'[a-zA-Z]+[a-zA-Z0-9_.]+@{1}[a-z]+\.[a-z]{2,}', text)
    if checkup:
        return True
    else:
        return False


@ input_error
def change_name(name, new_value):
    contact = get_contact(name)
    contact['name'] = new_value
    deleting_contact(name)
    dump_contact(contact)
    message = 'contact has been chenged'
    return message


# @ input_error
def add_phone(arguments):
    name = arguments.split(sep=', ')[0]
    new_value = arguments.split(sep=', ')[1]
    if phone_checkup(new_value):
        contact = get_contact(name)
        if new_value in contact['phones']:
            message = f'{new_value} already exists'
        else:
            contact['phones'].append(new_value)
            dump_contact(contact)
            message = 'phone number has been added'
    return message


def remove_phone(arguments):
    name = arguments.split(sep=', ')[0]
    value = arguments.split(sep=', ')[1]
    contact = get_contact(name)
    if value in contact['phones']:
        contact['phones'].remove(value)
        dump_contact(contact)
        message = f'phone number {value} has been removed from contact {name}'
    return message


def remove_email(arguments):
    name = arguments.split(sep=', ')[0]
    value = arguments.split(sep=', ')[1]
    contact = get_contact(name)
    if value in contact['emails']:
        contact['emails'].remove(value)
        dump_contact(contact)
        message = f'email {value} has been removed from contact {name}'
    return message


@ input_error
def add_email(arguments):
    name = arguments.split(sep=', ')[0]
    new_value = arguments.split(sep=', ')[1]
    if email_checkup(new_value):
        contact = get_contact(name)
        if new_value in contact['emails']:
            message = f'{new_value} already exists'
        else:
            contact['emails'].append(new_value)
            dump_contact(contact)
            message = 'email has been added'
    return message


def show_all():
    for item in Path(default_contact_path).iterdir():
        contact = get_contact(item.name.split(sep='.')[0])
        print_contact(contact)
    message = 'the contact list ended'
    return message


def set_b_day(arguments):
    name = arguments.split(sep=', ')[0]
    new_value = arguments.split(sep=', ')[1]
    contact = get_contact(name)
    contact['birthday'] = new_value
    dump_contact(contact)
    message = 'birthday have been set'

    return message


def set_address(arguments):
    name = arguments.split(sep=', ')[0]
    new_value = arguments.split(sep=', ')[1]
    contact = get_contact(name)
    contact['address'] = new_value
    dump_contact(contact)
    message = 'address have been set'

    return message


@ input_error
def change_phone(name, old_value, new_value):
    if phones_checkup(new_value):
        contact = get_contact(name)
        contact['phones'].remove(old_value)
        contact['phones'].append(new_value)
        dump_contact(contact)
        message = 'phone has been changed'
    else:
        message = 'check oyur input, smth is incorrect'
    return message


@ input_error
def change_email(name, old_value, new_value):
    if emails_checkup(new_value):
        contact = get_contact(name)
        contact['emails'].remove(old_value)
        contact['emails'].append(new_value)
        dump_contact(contact)
        message = 'email has been changed'
    else:
        message = 'check oyur input, smth is incorrect'
    return message


if __name__ == "__main__":

    welcome_text = 'wooo'

    print(welcome_text)
