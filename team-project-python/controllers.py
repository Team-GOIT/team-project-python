from modules import Contact, AddressBook, NotesBook
# import calls_manager

# lets move it from here
# lets use more clear variables names
contacts = AddressBook()
notes = NotesBook()

# this part should be improved before usage
# def initial_state(contacts):
#     global book
#     book = contacts

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
        contacts.add_contact(contact)
        
    except ValueError:
        raise ValueError('Add name of the contact please or correct format of the phone: +123 456789 / +(456) 789012345 / +789 0123456789')
    except IndexError:
        raise IndexError('Phone is required. Please add phone to the contact')

@input_error
def add_address(args, kwargs):
    try:
        name, *address= args
        # address= ', '.join(address)
        print(address)
        if not address:
            raise IndexError('Missing required value - Address')
        
        # use class method
        contact = contacts.data.get(name)
        if contact:
            contact.add_or_edit_address(address)
            print('Address was added')
        else:
            raise NameError('name')
            # raise NameError("Such contact doesn't exist")
    except ValueError:
        raise ValueError('val')
    except NameError:
        raise NameError('name')
    except TypeError:
        raise TypeError('type')
    except IndexError:
        raise IndexError('idx')
            # raise ValueError("Add address in such format please: <name> <country> <city> <street> <house_number> <postal_code>")
    
@input_error
def add_email(args, kwargs):
    try:
        name, email= args
    
        if not email:
            raise IndexError('Missing required value - Email')
        contact = contacts.data.get(name)
        if contact:
            contact.add_or_edit_email(email)
            print('Email was added')
        else:
            raise NameError("Such contact doesn't exist")
    except:
            raise ValueError('Please provide a valid email address.')
        
@input_error
def add_birthday(args, kwargs):
    print(args, 'here birth')
    try:
        name, birthday= args
        contact = contacts.data.get(name)
        if contact:
            contact.add_or_edit_birthday(birthday)
            
        else:
            raise TypeError("Such contact doesn't exist")
    
    except TypeError:
            raise TypeError("Not correct format. Please use DD-MM-YYYY.")
    except ValueError:
            raise ValueError("Missing required value - Birthday")
        
@input_error
def add_note(args, kwargs):
    title = input("Enter note's title: ")
    content = input("Enter note's content: ")
    tags = input("Enter note's tags: ")
    tags_list = tags.split(' ')

    if not content or not title:
        raise ValueError('Make sure you added title and content of the note')

    print(notes.add_note(title, content, tags_list))

    
@input_error
def show_contacts(args, kwargs):
    for name ,contact in contacts.data.items():
        print(f'{contact.name}: {contact.phone}, {contact.birthday}')

@input_error
def show_notes(args, kwargs):
    print(notes.get_all_notes())
        
@input_error
def find_contact(args, kwargs):
    try:
        name, *arg = args
        contact = contacts.data.get(name)
       
        print(f'{contact.name}: {contact.phone}, {contact.birthday}' if contact else "Such contact doesn't exist")
    except:
        raise NameError("Such contact doesn't exist")

@input_error
def change_note(args, kwargs):
    title, *des= args

    content = input("Enter note's content: ")

#   Update this line
    tags = input("Enter note's tags: ")
    tags_list = tags.split(' ')

    print(notes.edit_note(title, content, tags_list))
        
@input_error
def change_email(args, kwargs):
    try:
        name, email = args
        # use method from class
        contact = contacts.data.get(name)
        if contact:
            # contact.edit_email(email)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Email")

@input_error
def change_birthday(args,kwargs):
    try:
        name,birthday = args
        # use method from class
        contact = contacts.data.get(name)
        if contact:
            contact.add_or_edit_birthday(birthday)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Birthday")
        
@input_error
def change_address(args, kwargs):
    try:
        name, *address= args
        address= ', '.join(address)
        
        contact = contacts.data.get(name)
        if contact:
            # contact.edit_address(address)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Address")

@input_error
def change_note(args, kwargs):
    try:
        title,*des= args
        des= ' '.join(des)
        notes.edit_note(title, des)

        print('Note was updated successfully')
    except NameError:
        raise NameError("Such note doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Description")
        
@input_error
def show_address(args, kwargs):
    name, *args = args
    contact = notes.data.get(name)
    if contact:
        return contact.address
    else:
        raise NameError
    
@input_error
def show_email(args, kwargs):
    name, *args = args
    contact = notes.data.get(name)
    if contact:
        return contact.email
    else:
        raise NameError
    
@input_error
def show_phone(args, kwargs):
    name, *args = args
    # use class method
    contact = contacts.data.get(name)
    if contact:
        print(contact.phone)
    else:
        raise NameError('Such contact does oe exist')
    
@input_error
def show_birthday(args, kwargs):
    name, *args = args
    contact = contacts.data.get(name)
    if contact:
        print(contact.birthday)
    else:
        raise NameError
    
@input_error
def show_note(args, kwargs):
    title, *args = args
    print(notes.get_note(title))

@input_error
def search_notes(args, kwargs):
    query, *args = args
    print(notes.search_notes(query))
    
@input_error
def delete_address(args, kwargs):
    try:
        name, *address = args
        
        # can we use class method here?
        contact = contacts.data.get(name)
        if contact:
            # contact.delete_address()
            
            print('Address was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_email(args, kwargs):
    try:
        name, *email = args
        
        # can we use class method here?
        contact = contacts.data.get(name)
        if contact:
            # contact.delete_email()
            
            print('Email was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_birthday(args, kwargs):
    try:
        name, *birthday = args
        
        contact = contacts.data.get(name)
        if contact:
            contact.remove_birthday()
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_phone(args, kwargs):
    try:
        name, *phone = args
        
        contact = contacts.data.get(name)
        if contact:
            contact.remove_phone()
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error   
def delete_contact(args, kwargs):
    try:
        name, *arg = args
        contact = contacts.data.get(name)
        if contact:
            contacts.delete_contact(name)
            print("Contact was deleted successfully")
    except:
        raise NameError("Such contact doesn't exist")

@input_error   
def delete_note(args, kwargs):
    title, *arg = args
    print(notes.delete_note(title))

@input_error
def show_birthdays(args, kwargs):
    
    try:
        period, *args= args
        birthdays = contacts.show_birthdays(period)
        
        print(birthdays)
    except:
        raise ValueError("Period is missing")

@input_error
def add_note_tag(args, kwargs):
    note_title, tag = args
    print(notes.add_tag(note_title, tag))

@input_error
def delete_note_tag(args, kwargs):
    note_title, tag = args
    print(notes.delete_tag(note_title, tag))

@input_error
def search_notes_by_tag(tags, kwargs):
    print(notes.search_notes_by_tags(tags))

@input_error
def send_sms(args, kwargs):
    contact_name, sms_text = args
    # This line returns error. Why?
    contact = contacts.find_contact(contact_name)
    if contact:
        print('contact', contact)
        # calls_manager.send_message(contact.phone, sms_text)