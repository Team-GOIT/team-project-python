from modules import Contact, AddressBook, NotesBook

book ={}
noteBook = NotesBook()
def initial_state(contacts):
    global book
    book = contacts

# decorator which parse all errors
def input_error(fn):
    def inner(*args, **kwargs):
        try:
            return fn(args, kwargs)
        except ValueError as e:
            print(e)
        except TypeError  as e:
            print(e)
        except NameError  as e:
            print(e)
        except IndexError  as e:
            print(e)

            
    return inner


# controllers wich parse user input and do all logic
@input_error
def add_contact(args,kwargs):
    try:
        name,*phone= args
        phone= ' '.join(phone)
        
        if not phone:
            raise IndexError
        contact = Contact(name)
        contact.add_or_edit_phone(phone)
        book.add_contact(contact)  
        
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
        contact = book.data.get(name)
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
        contact = book.data.get(name)
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
        contact = book.data.get(name)
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
    try:
        print(args)
        title,*content= args
        content= ' '.join(content)
        
        if not content:
            raise IndexError('Missing required value - Description')
        
        noteBook.add_note(title, content)
        print("Note was added")
    except:
        raise TypeError('Something went wrong. Try again')      
    
@input_error
def show_contacts(args, kwargs):
    print(book.data)
    for name,contact in book.data.items():
        print(f'{contact.name}: {contact.phone}, {contact.birthday}')

@input_error
def show_notes(args, kwargs):
    for note in noteBook.notes:
        print(note)
        
@input_error
def find_contact(args, kwargs):
    try:
        name, *arg = args
        contact = book.data.get(name)
       
        print(f'{contact.name}: {contact.phone}, {contact.birthday}' if contact else "Such contact doesn't exist")
    except:
        raise NameError("Such contact doesn't exist")

@input_error
def change_phone(args,kwargs):
    try:
        name,*phone= args
        phone= ' '.join(phone)
        contact = book.data.get(name)
        if contact:
            contact.add_or_edit_phone(phone)
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Phone")
        
@input_error
def change_email(args,kwargs):
    try:
        name,email= args
        contact = book.data.get(name)
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
        name,birthday= args
        contact = book.data.get(name)
        if contact:
            contact.add_or_edit_birthday(birthday)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Birthday")
        
@input_error
def change_address(args,kwargs):
    try:
        name, *address= args
        address= ', '.join(address)
        
        contact = book.data.get(name)
        if contact:
            # contact.edit_address(address)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Address")

@input_error
def change_note(args,kwargs):
    try:
        title,*des= args
        des= ' '.join(des)
        noteBook.edit_note(title, des)
            
        print('Note was updated successfully')
    except NameError:
        raise NameError("Such note doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Description")
        
@input_error
def show_address(args,kwargs):
    name, *args= args
    contact = book.data.get(name)
    if contact:
        return contact.address
    else:
        raise NameError
    
@input_error
def show_email(args,kwargs):
    name, *args= args
    contact = book.data.get(name)
    if contact:
        return contact.email
    else:
        raise NameError
    
@input_error
def show_phone(args,kwargs):
    name, *args= args
    contact = book.data.get(name)
    if contact:
        print(contact.phone)
    else:
        raise NameError('Such contact does oe exist')
    
@input_error
def show_birthday(args,kwargs):
    name, *args= args
    contact = book.data.get(name)
    if contact:
        print(contact.birthday)
    else:
        raise NameError
    
@input_error
def show_note(args,kwargs):
    try:
        title, *args= args
        note = noteBook.search_notes(title)
        print(note)
    except:
        raise NameError("Such note doesn't exist")
    
@input_error
def delete_address(args,kwargs):
    try:
        name, *address= args
        
        contact = book.data.get(name)
        if contact:
            # contact.delete_address()
            
            print('Address was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_email(args,kwargs):
    try:
        name, *email= args
        
        contact = book.data.get(name)
        if contact:
            # contact.delete_email()
            
            print('Email was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_birthday(args,kwargs):
    try:
        name, *birthday= args
        
        contact = book.data.get(name)
        if contact:
            contact.remove_birthday()
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_phone(args,kwargs):
    try:
        name, *phone= args
        
        contact = book.data.get(name)
        if contact:
            contact.remove_phone()
            
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error   
def delete_contact(args, kwargs):
    try:
        name, *arg = args
        contact = book.data.get(name)
        if contact:
            book.delete_contact(name)
            print("Contact was deleted successfully")
    except:
        raise NameError("Such contact doesn't exist")

@input_error   
def delete_note(args, kwargs):
    try:
        title, *arg = args
        print(noteBook.delete_note(title))
    except:
        raise NameError("Such note doesn't exist")

@input_error
def show_birthdays(args, kwargs):
    
    try:
        period, *args= args
        birthdays = book.show_birthdays(period)
        
        print(birthdays)
    except:
        raise ValueError("Period is missing")
    
    