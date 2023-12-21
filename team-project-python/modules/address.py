from .field import Field

class Address(Field):

    #створюємо клас Address та перевіряємо чи адреса обов'язково містить країну та місто, а також чи поштовий індекс складається з 5ти цифр
    
    def __init__(self, country='', city='', street='', house_number='', postal_code=''):
        self.country = country
        self.city = city
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.validate()

    def validate(self):
        if not self.country or not self.city:
            raise ValueError('Country and city is required for an address.')
        
        if self.postal_code and (not self.postal_code.isdigit() or len(self.postal_code) != 5):
            raise ValueError('Postal code should be a 5-digit number.')

    def __str__(self):
        address_parts = [self.country, self.city, self.street, self.house_number, self.postal_code]
        formatted_address = ', '.join(filter(None, address_parts))

        if formatted_address:
            return f'Address: {formatted_address}'
        else:
            return 'No address provided.'


        