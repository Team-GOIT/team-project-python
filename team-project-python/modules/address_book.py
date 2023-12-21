
from collections import UserDict
from datetime import datetime
from .birthday import Birthday
from .contact import Contact;

class AddressBook(UserDict):
    
    def add_contact(self,user):
       
        self.data[user.name.value] = user
        
    def find_contact(self,name):
        print(self.data)
        return self.data[name] if name in self.data.keys() else None
    def delete_contact(self,name):
        if name in self.data:
            del self.data[name]
    def show_birthdays(self,period):
        today = datetime.now()
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        grouped_birthdays = {day: [] for day in week_days}
   
        for name,contact in self.data.items():
            birthday = contact.birthday
            
            if isinstance(birthday, Birthday):
                print(True)
                str_time = str(birthday).split(': ')[1]
               
                birthday_this_year = datetime.strptime(str_time, '%d-%m-%Y').replace(year=today.year)
                print(birthday_this_year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days
                
                if 0 <= delta_days < int(period):
                    print('period', period, delta_days)
                    
                    week_day = birthday_this_year.weekday()
                    if week_day == 6 or week_day == 5:
                        week_day = 0
                    grouped_birthdays[week_days[week_day]].append(contact.name.value)

        sorted_data = dict(sorted(grouped_birthdays.items(), key=lambda x: week_days.index(x[0])))
        output = ''
        for day, names in sorted_data.items():
            output += f'{day}: {", ".join(names)}\n'

        return output

