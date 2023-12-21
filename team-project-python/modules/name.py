from .field import Field


class Name(Field):

    # створення класу Name, де ми перевіряємо чи передане ім'я не порожнє та складається тільки з літер

    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if not self.value.strip():
            raise ValueError('Name cannot be empty.')

    def __str__(self):
        return(self.value)
    

