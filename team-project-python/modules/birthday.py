from .field import Field
from datetime import datetime

class Birthday(Field):
    #створення класу Birthday, де ми перевіряємо чи дата була введена, також чи в правильному форматі ДД-ММ-РРРР

    def __init__(self, date = None):
        self.date = self.validate_date(date) if date else None

    def validate_date(self, date):
        if not date:
            return None
        
        try:
            validated_date = datetime.strptime(date, '%d-%m-%Y')
            return validated_date.strftime('%d-%m-%Y')
        except ValueError:
            raise ValueError('Not correct format. Please use DD-MM-YYYY.')
        
    def __str__ (self):
        if self.date:
            return f'Birthday: {self.date}'
        else:
            return 'No birthday set.'

