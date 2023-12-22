from commands_list import commands
import controllers
import pickle

# Lets move write_to_file from here
def write_to_file(contacts):
    with open('data.bin', 'wb') as fh:
        pickle.dump(contacts, fh)

 # Lets move read_from_file from here
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
     # Lets create a help method/controller
    for i in commands:
        print(i)

    # Lets move it from here
#     try:
#         contacts= read_from_file()
#         initial_state(contacts)
#     except:
#         contacts = AddressBook()
#         initial_state(contacts)

    while True:
        user_input =input("Enter the command:")
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            
            write_to_file(contacts)
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')

        # Lets use help method/controller instead
        elif command == 'help':
            for i in commands:
                print(i)
            
        elif command == 'add':
            controllers.add_contact(*args)
        elif command == "add-address":
            controllers.add_address(*args)
        elif command == "add-email":
            controllers.add_email(*args)
        elif command == "add-birthday":
            controllers.add_birthday(*args)
        elif command == "add-note":
            controllers.add_note(*args)
        elif command == 'all-contacts':
            controllers.show_contacts()
        elif command == 'all-notes':
            controllers.show_notes()
        elif command == 'find':
            controllers.find_contact(*args)
        elif command == 'change-phone':
            controllers.change_phone(args)
        elif command == 'change-email':
            controllers.change_email(args)
        elif command == 'change-address':
            controllers.change_address(args)
        elif command == 'change-birthday':
            controllers.change_birthday(args)
        elif command == 'change-note':
            controllers.change_note(args)
        elif command =='show-address':
            controllers.show_address(args)
        elif command =='show-email':
            controllers.show_email(args)
        elif command =='show-phone':
            controllers.show_phone(args)
        elif command =='send-sms':
            controllers.send_sms(*args)
        elif command =='show-birthday':
            controllers.show_birthday(args)
        elif command =='show-note':
            controllers.show_note(args)
        elif command == 'delete-phone':
            controllers.delete_phone(args)
        elif command == 'delete-email':
            controllers.delete_email(args)
        elif command == 'delete-birthday':
            controllers.delete_birthday(args)
        elif command == 'delete-address':
            controllers.delete_address(args)
        elif command == 'delete-contact':
            controllers.delete_contact(args)
        elif command == 'delete-note':
            controllers.delete_note(args)
        elif command == "show-birthdays":
            controllers.show_birthdays(args)
        else:
            print('Invalid command')

# if __name__ == '__main__':
main()