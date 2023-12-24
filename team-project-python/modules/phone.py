from .field import Field

import re


class Phone(Field):
    # створення класу Phone, де ми перевіряємо чи передан правильний формат телефону

    def __init__(self, number=None):
        self.number = self.validate_phone_number(number) if number else None

    def validate_phone_number(self, number):
        if not number:
            return None

        # перевірка чи номер телефону починається з +, далі (код країни) та сам номер телефону
        # We will update mask or commands description for this command
        pattern = r'\+380\d{9}'

        if re.match(pattern, number):
            return number
        else:
            raise ValueError('Not correct format. Please use + (country code) phone number.')

    def __str__(self):
        return self.number
        # if self.number:
        #     return self.number
        # return f'Phone number: {self.number}'
        # else:
        #       return 'No phone number set.'

