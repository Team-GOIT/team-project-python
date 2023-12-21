from commands_list import commands
from controllers import *
import pickle


def write_to_file(contacts):
    with open('data.bin', 'wb') as fh:
        pickle.dump(contacts, fh)

        
def read_from_file():
    with open('data.bin', 'rb') as fh:
        decoded = pickle.load(fh)
        return decoded


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

greeting = """
          
          Welcome to the personal assistant app!
          
          You can save all your important information here.
          
          Just use such commands
          """
    
def main():
    print(greeting)
    for i in commands:
        print(i)
    
    try:
        contacts= read_from_file()
        initial_state(contacts)
    except:
        contacts = AddressBook()
        initial_state(contacts)
        
        
    
    while True:
        user_input =input("Enter the command >>>>>")
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            
            write_to_file(contacts)
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')
        elif command == 'help':
            for i in commands:
                print(i)
            
        elif command == 'add':
            add_contact(*args)
        elif command == "add-address":
            add_address(*args)
        elif command == "add-email":
            add_email(*args)
        elif command == "add-birthday":
            add_birthday(*args)
        elif command == "add-note":
            add_note(*args)
        elif command == 'all-contacts':
            show_contacts()
        elif command == 'all-notes':
            show_notes()
        elif command == 'find':
            find_contact(*args)
        elif command == 'change-phone':
            change_phone(*args)
        elif command == 'change-email':
            change_email(*args)
        elif command == 'change-address':
            change_address(*args)
        elif command == 'change-birthday':
            change_birthday(*args)
        elif command == 'change-note':
            change_note(*args)
        elif command =='show-address':
            show_address(*args)
        elif command =='show-email':
            show_email(*args)
        elif command =='show-phone':
            show_phone(*args)
        elif command =='show-birthday':
            show_birthday(*args)
        elif command =='show-note':
            show_note(*args)
        elif command == 'delete-phone':
            delete_phone(*args)
        elif command == 'delete-email':
            delete_email(*args)
        elif command == 'delete-birthday':
            delete_birthday(*args)
        elif command == 'delete-address':
            delete_address(*args)
        elif command == 'delete-contact':
            delete_contact(*args)
        elif command == 'delete-note':
            delete_note(*args)
        elif command == "show-birthdays":
            show_birthdays(*args)
        else:
            print('Invalid command')


# if __name__ == '__main__':
main()