import re
from .name import Name
from .address import Address
from .phone import Phone
from .email import Email
from .birthday import Birthday


class Contact:
    def __init__(self, name: str) -> None:
        self._name = Name(name)
        self._phone = None
        self._email = None
        self._address = None
        self._birthday = None

    def __str__(self) -> str:
        info_array = [
            f"Contact {self._name}",
            self._phone,
            self._email,
            self._address,
            self._birthday,
        ]
        return ", ".join(map(lambda n: str(n), filter(lambda n: n, info_array)))

    @property
    def name(self) -> Name:
        return self._name

    @property
    def phone(self) -> Phone:
        return self._phone

    @property
    def email(self) -> Email:
        return self._email

    @property
    def address(self) -> Address:
        return self._address

    @property
    def birthday(self) -> Birthday:
        return self._birthday

    def add_or_edit_phone(self, value: str) -> None:
        self._set_field("_phone", Phone(value), "Phone successfully added/updated")

    def add_or_edit_email(self, value: str) -> None:
        self._set_field("_email", Email(value), "Email successfully added/updated")

    def add_or_edit_address(self, value: str) -> None:
        self._set_field(
            "_address", Address(value), "Address successfully added/updated"
        )

    def add_or_edit_birthday(self, value: str) -> None:
        self._set_field(
            "_birthday", Birthday(value), "Birthday successfully added/updated"
        )

    def remove_phone(self) -> None:
        self._set_field("_phone", None, "Phone successfully removed")

    def remove_email(self) -> None:
        self._set_field("_email", None, "Email successfully removed")

    def remove_address(self) -> None:
        self._set_field("_address", None, "Address successfully removed")

    def remove_birthday(self) -> None:
        self._set_field("_birthday", None, "Birthday successfully removed")

    def contains_value(self, value) -> bool:
        pattern = re.compile(f".*{re.escape(value)}.*", re.IGNORECASE)

        for field in ["_name", "_phone", "_email", "_address", "_birthday"]:
            if pattern.match(str(getattr(self, field, ""))):
                return True

        return False

    def _set_field(self, field, value, success_message):
        setattr(self, field, value)
        print(success_message)
