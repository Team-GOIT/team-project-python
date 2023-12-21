from collections import UserDict
from datetime import datetime
from .birthday import Birthday

class AddressBook(UserDict):
    def add_contact(self,user):

        self.data[user.name.value] = user

    def add_note(self,note):
        self.data[note['title']] = note

    def find_contact(self,name):
        return self.data[name] if name in self.data.keys() else None
    def find_note(self,title):
        return self.data[title] if title in self.data.keys() else None
    def delete_contact(self,name):
        if name in self.data:
            del self.data[name]
    def show_birthdays(self, period):
        today = datetime.now()
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        grouped_birthdays = {day: [] for day in week_days}

        for record in self.data.values():
            if isinstance(record.birthday, Birthday):
                birthday_this_year = record.birthday.to_datetime().replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < int(period):
                    week_day = birthday_this_year.weekday()
                    if week_day == 6 or week_day == 5:
                        week_day = 0
                    grouped_birthdays[week_days[week_day]].append(record.name.value)

        sorted_data = dict(sorted(grouped_birthdays.items(), key=lambda x: week_days.index(x[0])))
        output = ''
        for day, names in sorted_data.items():
            output += f'{day}: {", ".join(names)}\n'

        return output
