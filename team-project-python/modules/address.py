from .field import Field

class Address(Field):
    def __init__(self,name) -> None:
        super().__init__(name)
        