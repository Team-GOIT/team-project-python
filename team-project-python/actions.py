from modules import Contact, AddressBook

book = AddressBook()

def initial_state(contacts):
    global book
    book = contacts

# decorator which parse all errors
def input_error(fn):
    def inner(*args, **kwargs):
        print(args, kwargs, 'here')
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



@input_error
def add_contact(args,kwargs):
    try:
        name,phone= args
        
        if not phone:
            raise IndexError('Missing required value - Phone')
        contact = Contact(name)
        contact.add_phone(phone)
        book.add_contact(contact)  
        print("Contact added")
    except:
        raise TypeError('Something went wrong. Try again')

@input_error
def add_address(args, kwargs):
    try:
        name, *address= args
        address= ', '.join(address)
        
        if not address:
            raise IndexError('Missing required value - Address')
        elif name in book.data.keys():
            contact = book.find_contact(name)
            # contact.add_address(address)
            print('Address was added')
        else:
            raise TypeError('Something went wrong. Try again')
    except:
            raise NameError("Such contact doesn't exist")
    
@input_error
def add_email(args, kwargs):
    try:
        name, email= args
        
        if not email:
            raise IndexError('Missing required value - Email')
        elif name in book.data.keys():
            contact = book.find_contact(name)
            # contact.add_email(email)
            print('Email was added')
        else:
            raise TypeError('Something went wrong. Try again')
    except:
            raise NameError("Such contact doesn't exist")
        
@input_error
def add_birthday(args, kwargs):
    print(args, 'here birth')
    try:
        name, birthday= args
        
        if name in book.data.keys():
            contact = book.find_contact(name)
            print(birthday)
            # contact.add_birthday(birthday)
            print('Birthday was added')
        else:
            raise TypeError("Such contact doesn't exist")
    
    except TypeError:
            raise TypeError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Birthday")
        
@input_error
def add_note(args, kwargs): 
    try:
        print(args)
        title,*des= args
        des= ' '.join(des)
        
        if not des:
            raise IndexError('Missing required value - Description')
        
        note ={"title":title, "des": des}
                # contact = Contact(title)
        # contact.add_phone(des)
        book.add_note(note)  
        print("Note was added")
    except:
        raise TypeError('Something went wrong. Try again')      
    
@input_error
def show_contacts(args, kwargs):
    for name,contact in book.data.items():
        print(contact)

@input_error
def show_notes(args, kwargs):
    for name,note in book.data.items():
        print(note)
        
@input_error
def find_contact(args, kwargs):
    try:
        name, *arg = args
        contact = book.find_contact(name)
        print(contact if contact else "Such contact doesn't exist")
    except:
        raise NameError("Such contact doesn't exist")

@input_error
def change_phone(args,kwargs):
    try:
        name,phone= args
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.edit_phone(phone)
            
            print('Contact was updated')
    except NameError:
        raise NameError("Such contact doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Phone")
        
@input_error
def change_email(args,kwargs):
    try:
        name,email= args
        if name in book.data.keys():
            contact = book.find_contact(name)
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
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.edit_birthday(birthday)
            
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
        
        if name in book.data.keys():
            contact = book.find_contact(name)
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
        if title in book.data.keys():
            # note = book.find_note(title)
            # note.des = des
            # contact.edit_note(note)
            
            print('Note was updated successfully')
    except NameError:
        raise NameError("Such note doesn't exist")
    except ValueError:
            raise ValueError("Missing required value - Description")
        
@input_error
def show_address(args,kwargs):
    name, *args= args
    if name in book.data.keys():
        contact = book.find_contact(name)
        return contact.address
    else:
        raise NameError
    
@input_error
def show_email(args,kwargs):
    name, *args= args
    if name in book.data.keys():
        contact = book.find_contact(name)
        return contact.email
    else:
        raise NameError
    
@input_error
def show_phone(args,kwargs):
    name, *args= args
    if name in book.data.keys():
        contact = book.find_contact(name)
        return contact.phone
    else:
        raise NameError
    
@input_error
def show_birthday(args,kwargs):
    name, *args= args
    if name in book.data.keys():
        contact = book.find_contact(name)
        return contact.birthday
    else:
        raise NameError
    
@input_error
def show_note(args,kwargs):
    title, *args= args
    if title in book.data.keys():
        note = book.find_note(title)
        print(note if note else "Such note doesn't exist")
    else:
        raise NameError
    
@input_error
def delete_address(args,kwargs):
    try:
        name, *address= args
        
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.delete_address()
            
            print('Address was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_email(args,kwargs):
    try:
        name, *email= args
        
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.delete_email()
            
            print('Email was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_birthday(args,kwargs):
    try:
        name, *birthday= args
        
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.delete_birthday()
            
            print('Birthday was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error
def delete_phone(args,kwargs):
    try:
        name, *phone= args
        
        if name in book.data.keys():
            contact = book.find_contact(name)
            # contact.delete_phone()
            
            print('Phone was deleted')
    except NameError:
        raise NameError("Such contact doesn't exist")
    
@input_error   
def delete_contact(args, kwargs):
    try:
        name, *arg = args
        if name in book.data.keys():
            book.delete_contact(name)
            print("Contact was deleted successfully")
    except:
        raise NameError("Such contact doesn't exist")

@input_error   
def delete_note(args, kwargs):
    try:
        title, *arg = args
        if title in book.data.keys():
            # book.delete_note(title)
            print("Note was deleted successfully")
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
    
    