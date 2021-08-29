from collections import UserDict
from datetime import timedelta
from datetime import datetime
from pathlib import Path


class AddressBook(UserDict):
    record = Record()
    data = {}

    def add_record(record):
        self.data.append(record)


class Record:
    name = Name()
    phones = Phone()
    birthday = Birthday()

    def __init__(self, name):
        self.name = name
        self.phones = None
        self.birthday = datetime.now()
        self.sequence_number = 0

    def add_phone(self, phone):
        pass

    def del_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass

    def __iter__():
        return Record()

    def __next__(self, quantity):
        if self.sequence_number < len(AddressBook.data):
            result = []
            for i in range(quantity):
                result.append(AddressBook.data[sequence_number])
                self.sequence_number += 1
            return result
        raise StopIteration()

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
    def phones(self, new_value):
        if new_value in self.phones:
            print(f'{new_value} already exists')
        else:
            self.phones.append(new_value)

    @birthday.setter
    def birthday(self, new_value):
        if isinstance(new_value, datetime(year, month, day)):
            self.birthday = new_value
        else:
            print(f'{new_value} is not datetime object')

    def days_to_birthday(self, birthday):
        if birthday < datetime.now().date():  # ??????????????????
            nextbday = datetime(year=datetime.now().year,
                                month=birthday.month, day=birthday.day).date()

            if datetime.now().date() > nextbday:
                nextbday = datetime(year=datetime.now().year+1,
                                    month=birthday.month, day=birthday.day).date()
            return (nextbday - datetime.now().date()).days


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass
