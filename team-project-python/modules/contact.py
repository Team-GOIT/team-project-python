from .name import Name
from .address import Address

class Contact:
    def __init__(self, name, address) -> None:
        self.name = Name(name)
        self.address = Address(address)
    def __str__(self) -> str:
        return f"{self.name} is living {self.address}"