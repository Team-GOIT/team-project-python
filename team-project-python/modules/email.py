from .field import Field
import re

class Email(Field):
    #створення класу Email, де відбувається валідація введеної пошти на стандартний формат електроної пошти

    def __init__(self, email = None):
        self.email = self.validate_email(email) if email else None

    def validate_email(self, email):
        if not email:
            return None
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return email
        else:
            raise ValueError('Please provide a valid email address.')

    def str(self):
        if self.email:
            return f'Email: {self.email}'
        else:
            return 'No email set.'