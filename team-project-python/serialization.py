from modules import *
import json

# # serialize address book
# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, (AddressBook, Contact, Name, Birthday, Email, Note, NotesBook, Phone, Address)):
#             # Serialize objects based on their __dict__
#             return obj.__dict__
#         return super().default(obj)
    
# class MyDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(object_hook=self.dict_to_object, *args, **kwargs)

#     def dict_to_object(self, dct):
#         if 'name' in dct and 'email' in dct and 'phone' in dct:
#             # Recognize the structure of Contact
#             return Contact(**dct)
#         elif 'data' in dct and 'other_attribute' in dct:
#             # Recognize the structure of AddressBook
#             return AddressBook(**dct)
        
#         return dct


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            # Serialize objects based on their __dict__
            return obj.__dict__
        return super().default(obj)

class Decoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.dict_to_object, *args, **kwargs)

    def dict_to_object(self, dct):
        print(dct , '======dct====')
        
        if "_name" in dct:
            dct["_name"] = Name(dct["_name"]);
        if "_phone" in dct: 
            dct["_phone"] = Phone(dct["_phone"]);
        
       
        # return AddressBook(dct)
        # elif '_name' in dct and '_phone' in dct:
        #     # Recognize the structure of Contact
        #     name = self.dict_to_object(dct['_name'])
        #     phone = self.dict_to_object(dct['_phone'])
        #     email = self.dict_to_object(dct.get('_email'))
        #     address = self.dict_to_object(dct.get('_address'))
        #     birthday = self.dict_to_object(dct.get('_birthday'))
        #     return Contact(name, phone, email, address, birthday)
        # elif 'value' in dct:
        #     # Recognize the structure of Name, Email, Address, etc.
        #     return dct['value']
        # return dct