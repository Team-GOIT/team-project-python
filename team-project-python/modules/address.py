from .field import Field

class Address(Field):
    def __init__(self, address_string=""):
        self.address_string = address_string

    def __str__(self):
        if self.address_string:
            return f"Address: {self.address_string}"
        else:
            return "No address provided"


        