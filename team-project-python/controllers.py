from modules import Contact, AddressBook, NotesBook
import pickle
import calls_manager

# contacts = AddressBook()
# notes = NotesBook()

contactsManager = AddressBook()
notesManager = NotesBook()

# save data to database
def write_to_file():
    with open('contacts.bin', 'wb') as fh:
        global contactsManager
        pickle.dump(contactsManager, fh)
    with open('notes.bin', 'wb') as fh:
        global notesManager
        pickle.dump(notesManager, fh)


# take data from database
def read_from_file():
    try:
        with open('contacts.bin', 'rb') as fh:
            global contactsManager

            decoded = pickle.load(fh)
            contactsManager = decoded
        with open('notes.bin', 'rb') as fh:
            global notesManager

            decoded = pickle.load(fh)
            notesManager = decoded
    except:
        contactsManager = AddressBook()
        notesManager = NotesBook()


# decorator which parse all errors
def input_error(fn):
    def inner(*args, **kwargs):
        try:
            return fn(args, kwargs)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except NameError as e:
            print(e)
        except IndexError as e:
            print(e)

    return inner


# controllers wich parse user input and do all logic
@input_error
def add_contact(args, kwargs):
    try:
        name,*phone= args
        phone= ' '.join(phone)

        if not phone:
            raise IndexError
        contact = Contact(name)
        contact.add_or_edit_phone(phone)
        contactsManager.add_contact(contact)

    except ValueError:
        raise ValueError('Add name of the contact please or correct format of the phone: +123 456789 / +(456) 789012345 / +789 0123456789')
    except IndexError:
        raise IndexError('Phone is required. Please add phone to the contact')

@input_error
def add_address(args, kwargs):
    try:
        name, *address= args
        address= ', '.join(address)
        if not address:
            raise IndexError
        contact = contactsManager.data.get(name)
        if contact:
            contact.add_or_edit_address(address)
            print('Address was added')
        else:
            raise NameError
    except ValueError:
        raise ValueError("Contact is required field. Please provide the contact name")
    except NameError:
        raise NameError("Such contact doesn't exist")
    except IndexError:
        raise IndexError('Address is required field. Please provide the address')

@input_error
def add_email(args, kwargs):
    try:
        name, email= args

        if not email:
            raise IndexError
        contact = contactsManager.data.get(name)
        if contact:
            contact.add_or_edit_email(email)
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError('Contact and email are required fields. Please provide the contact name and email in such format <name> kari@gmail.com')

@input_error
def add_birthday(args, kwargs):
    try:
        name, birthday= args
        contact = contactsManager.data.get(name)
        if contact:
            contact.add_or_edit_birthday(birthday)

        else:
            raise TypeError("Such contact doesn't exist")

    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError('Contact and birthday are required fields. Please provide the contact name and birthday in such format <name> 13-09-1989')

@input_error
def add_note(args, kwargs):
    try:
        title, *content = args
        content = ' '.join(content)

        if not content:
            raise IndexError

        notesManager.add_note(title, content)
        print("Note was added")
    except IndexError:
        raise IndexError('Missing required value - Description')
    except ValueError:
        raise ValueError('Missing required values - Title and Description')

@input_error
def show_contacts(args, kwargs):
    for name ,contact in contactsManager.data.items():
        print(f'{contact.name}: {contact.phone}, {contact.birthday}')

@input_error
def show_notes(args, kwargs):
    print(notesManager.get_all_notes())
        
@input_error
def find_contact(args, kwargs):
    try:
        name, *arg = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.name, contact.birthday, contact.address)
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Provide the name of the contact please")

@input_error
def change_phone(args,kwargs):
    try:
        name,*phone = args
        phone= ' '.join(phone)
        contact = contactsManager.data.get(name)
        if not phone:
            raise IndexError
        if contact:
            try:
                contact.add_or_edit_phone(phone)
            except:
                raise TypeError
        else: raise NameError
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Missing required value - Phone or Contact")
    except TypeError:
        raise TypeError("Please provide phone number in such format: +123 456789 / +(456) 789012345 / +789 0123456789")
        
@input_error
def change_email(args, kwargs):
    try:
        name, email = args

        contact = contactsManager.data.get(name)
        if not email:
            raise IndexError
        if contact:
            try:
                contact.add_or_edit_email(email)
            except:
                raise TypeError
        else: raise NameError

    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Missing required value - email or Contact")
    except TypeError:
        raise TypeError("Please provide email in such format: kari@gmail.com")

@input_error
def change_birthday(args, kwargs):
    try:
        name,birthday = args
        contact = contactsManager.data.get(name)
        if not birthday:
            raise IndexError
        if contact:
            try:
                contact.add_or_edit_birthday(birthday)
            except:
                raise TypeError
        else: raise NameError

    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Missing required value - birthday or Contact")
    except TypeError:
        raise TypeError("Please provide birthday in such format: 13-09-1989")
        
@input_error
def change_address(args, kwargs):
    try:
        name, *address= args
        address= ' '.join(address)
        contact = contactsManager.data.get(name)
        if not address:
            raise ValueError
        if contact:
            contact.add_or_edit_address(address)
        else: raise NameError

    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Missing required values - address or Contact. Please provide address or Contact name")

@input_error
def change_note(args, kwargs):
    try:
        title, *des = args
        des = ' '.join(des)
        notesManager.edit_note(title, des)
            
        print('Note was updated successfully')
    except NameError:
        raise NameError("Such note doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Description")
        
@input_error
def show_address(args, kwargs):
    try:
        name, *args = args
        contact = contactsManager.data.get(name)
        if not contact:
            raise AttributeError
        print(contact.address)
        # else:

    except TypeError:
        TypeError("TypeErrorPlease provide contact name")
    except AttributeError:
        AttributeError("NameErrorSuch contact doesn't exist")
    except ValueError:
        ValueError("ValueErrorPlease provide contact name")
    except IndexError:
        IndexError("IndexErrorPlease provide contact name")
    
@input_error
def show_email(args, kwargs):
    try:
        name, *args = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.email)
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error
def show_phone(args, kwargs):
    try:
        name, *args = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.phone)
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")
    
@input_error
def show_birthday(args, kwargs):
    try:
        name, *args= args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.birthday)
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")
    
@input_error
def show_note(args, kwargs):
    try:
        title, *args = args
        print(notesManager.search_notes(title))
    except:
        raise NameError("Such note doesn't exist")
    
@input_error
def delete_address(args, kwargs):
    try:
        name, *address = args
        
        # can we use class method here?
        contact = contactsManager.data.get(name)
        if contact:
            contact.remove_address()
            
            print('Address was deleted')
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error
def delete_email(args, kwargs):
    try:
        name, *email = args
        
        # can we use class method here?
        contact = contactsManager.data.get(name)
        if contact:
            contact.remove_email()
            
            print('Email was deleted')
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error
def delete_birthday(args, kwargs):
    try:
        name, *birthday = args
        
        contact = contactsManager.data.get(name)
        if contact:
            contact.remove_birthday()
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error
def delete_phone(args, kwargs):
    try:
        name, *phone = args
        
        contact = contactsManager.data.get(name)
        if contact:
            contact.remove_phone()
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error
def delete_contact(args, kwargs):
    try:
        name, *arg = args
        contact = contactsManager.data.get(name)
        if contact:
            contactsManager.delete_contact(name)
            print("Contact was deleted successfully")
        else:
            raise NameError
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError("Please provide contact name")

@input_error   
def delete_note(args, kwargs):
    try:
        title, *arg = args
        print(notesManager.delete_note(title))
    except:
        raise NameError("Such note doesn't exist")

@input_error
def show_birthdays(args, kwargs):
    try:
        period, *args= args
        birthdays = contactsManager.show_birthdays(period)
        
        print(birthdays)
    except ValueError:
        raise ValueError("Period is missing")


@input_error
def send_sms(args, kwargs):
    contact_name, sms_text = args
    # calls_manager.send_message(contact.phone, sms_text)

def voice_message(args, kwargs):
    contact_name, sms_text = args
    # This line returns error. Why?
    # contact = contacts.find_contact(contact_name)
    # if contact:
        # calls_manager.voice_message(contact.phone, sms_text)