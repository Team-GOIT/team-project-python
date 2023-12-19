from collections import UserDict
import datetime
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, number):
        self.value = number

class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        if re.match("\d{2}.\d{2}.\d{4}", birthday):
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday sholud be in format DD.MM.YYYY")

    def show_birthday(self):
        if self.birthday:
            return self.birthday
        else:
            return f"There is no birhday for {self.name} saved"

    def add_phone(self, number):
        if re.match("\d{10}", number):
            phone = Phone(number)
            self.phones.append(phone)
        else:
            raise ValueError("Phone number should have 10 digits")

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
        # return f"Phone number {number} removed for {self.name.value}."
        return f"No phone number {number} found for {self.name.value}."

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
        # return f"Phone number {old_number} updated to {new_number}."
        return f"No phone number {old_number} found for {self.name.value}."

    def find_phone(self, number):
        if number in [phone.value for phone in self.phones]:
            return number
        else:
            return f"No phone number found for {self.name}"

    def __str__(self):
        if not self.birthday:
            message = "{:<25}{:<40}\n".format("Name", "Telephone Number")
            message += "{:.<25}{:<40}\n".format(
                (self.name.value), ("; ".join(p.value for p in self.phones))
            )

            return message
        else:
            message = "{:<25}{:<15}{:<15}\n".format(
                "Name", "Birthday", "Telephone Number"
            )
            message += "{:.<25}{:.<15}{:<15}\n".format(
                (self.name.value),
                (self.birthday.value),
                ("; ".join(p.value for p in self.phones)),
            )
            return message