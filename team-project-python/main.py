
from commands_list import commands, commands_array
from controllers import *
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter



# parse input, split for command and provided values
def parse_input(user_input):
    if not user_input:
        return '', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# message to greet the user
greeting = """

          Welcome to the personal assistant app!

          You can save all your important information here.

          Just use such commands
          """
    
# parse all commands
def main():
    print(greeting)
    for i in commands:
        print(i)

    read_from_file()

    completer = WordCompleter(commands_array, ignore_case=True, sentence=True)

    while True:
        user_input = prompt("Enter the command >>>>>", completer=completer)
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:

            write_to_file()
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


if __name__ == '__main__':
    main()
