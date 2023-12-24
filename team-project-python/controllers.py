from modules import Contact, AddressBook, NotesBook
import pickle
import calls_manager

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
        raise ValueError('Add name of the contact please or correct format of the phone: +380297658192')
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
        title = input("Enter note's title: ")
        if not title:
            return print("Make sure that title of the note is not empty")

        existing_note = notesManager.get_note(title)
        if not existing_note:
            content = input("Enter note's content: ")
            if not content:
                return print("Make sure content of the note not empty")

            tags = input("Enter note's tags (use ',' to separate multiple tags): ")
            tags_list = tags.replace(' ', '').split(',') if len(tags) > 0 else []

            return print(notesManager.add_note(title, content, tags_list))
        return print(f"Note with title '{title}' already exists")
    except (NameError, ValueError, TypeError, IndexError):
        return print("Please make sure that command is correct. Your note should have 'title', 'content' and optional 'tags'")

@input_error
def show_contacts(args, kwargs):
    for name ,contact in contactsManager.data.items():
        print(contact)

@input_error
def show_notes(args, kwargs):
    print(notesManager.get_all_notes())
    # try:
    #     return print(notesManager.get_all_notes())
    # except (NameError, ValueError, TypeError, IndexError):
    #     return print("Please make sure that command is correct. Example: 'all-notes'")
        
@input_error
def find_contact(args, kwargs):
    try:
        name, *arg = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact)
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
        raise TypeError("Please provide phone number in such format: +380297658192")
    except IndexError:
        raise IndexError("Please provide phone number in such format: +380297658192")


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
    except IndexError:
        raise IndexError("Please provide email in such format: kari@gmail.com")


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
    except IndexError:
        raise IndexError("Please provide birthday in such format: 13-09-1989")


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
        if not title:
            return print('Make sure that note with such title exists')

        existing_note = notesManager.get_note(title)
        if not existing_note:
            return print(f"Looks like not with '{title}' is not exist")

        if existing_note:
            print("Current note's content: ", existing_note.content)
            new_content = input("New content: ")

            if not new_content:
                return print("Note's content cannot be empty")

            print("Current note's tags: ", existing_note.tags)
            new_tags = input("New tags (use ',' to separate multiple tags): ")
            tags_list = new_tags.replace(' ', '').split(',') if len(new_tags) > 0 else []

            return print(notesManager.edit_note(title, new_content, tags_list))
    except (NameError, ValueError, TypeError, IndexError):
        return print(
            "Please make sure that command is correct. Your note should have 'title', 'content' and optional 'tags'")

@input_error
def show_address(args, kwargs):
    try:
        name, *args= args
        contact = contactsManager.data.get(name)

        if contact:
            print(contact.address)
        else:
            print("Such contact doesn't exist")

    except:
        print("Please provide contact name")

    
@input_error
def show_email(args, kwargs):
    try:
        name, *args = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.email)
        else:
            print("Such contact doesn't exist")
    except:
        print("Please provide contact name")

@input_error
def show_phone(args, kwargs):
    try:
        name, *args = args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.phone)
        else:
            print("Such contact doesn't exist")
    except:
        print("Please provide contact name")
    
@input_error
def show_birthday(args, kwargs):
    try:
        name, *args= args
        contact = contactsManager.data.get(name)
        if contact:
            print(contact.birthday)

        else:
            print("Such contact doesn't exist")

    except:
        print("Please provide contact name")
    
@input_error
def search_notes(args, kwargs):
    try:
        title = input("Enter search query: ")
        tags = input("Enter note's tags (use ',' to separate multiple): ")
        if not title and not tags:
            return print("Please enter a search query or some tags")

        tags_list = tags.split(', ')
        return print(notesManager.search_notes_by_tags(title, tags_list))
    except (NameError, ValueError, TypeError, IndexError):
        return print("Please make sure that command is correct. Please enter a search query or some tags")
    
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
    except (NameError, ValueError, TypeError, IndexError):
        return print("Please make sure that command is correct. Example: 'delete-note <note-title>'")

@input_error
def show_birthdays(args, kwargs):
    try:
        period, *args= args
        birthdays = contactsManager.show_birthdays(period)
        
        print(birthdays)
    except ValueError:
        raise ValueError("Period is missing")

@input_error
def search(args, kwargs):
    contacts = contactsManager.search(' '.join(args))

    if contacts:
        joined_contacts = '\n'.join([str(contact) for contact in contacts])
        print(f'Found contacts: \n{joined_contacts}')
    else:
        print('No contacts were found')
        
@input_error
def add_note_tag(args, kwargs):
    try:
        note_title, tag = args
        return print(notesManager.add_tag(note_title, tag))
    except (NameError, ValueError, TypeError, IndexError):
        return print("Please make sure that command is correct. Example: 'add-note-tag <note-title> <tag>'")

@input_error
def delete_note_tag(args, kwargs):
    try:
        note_title, tag = args
        return print(notesManager.delete_tag(note_title, tag))
    except (NameError, ValueError, TypeError, IndexError):
        return print("Please make sure that command is correct. Example: 'delete-note-tag <note-title> <tag>'")

@input_error
def send_sms(args, kwargs):
    contact_name, *sms_text = args
    message_text = ' '.join(sms_text)
    contact = contactsManager.data.get(contact_name)
    if contact:
        calls_manager.send_message(contact.phone, message_text)
    else:
        print(f"Looks like contact:{contact_name} not exist. Crete it, and try to send sms again")

@input_error
def voice_message(args, kwargs):
    contact_name, *message = args
    message_text = ' '.join(message)
    contact = contactsManager.data.get(contact_name)
    if contact:
        calls_manager.voice_message(contact.phone, message_text)
    else:
        print(f"Looks like contact:{contact_name} not exist. Crete it, and try to send sms again")        
        
        
