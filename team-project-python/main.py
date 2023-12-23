from commands_list import commands, commands_array
import controllers
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

    controllers.read_from_file()
    completer = WordCompleter(commands_array, ignore_case=True, sentence=True)

    while True:
        user_input = prompt("Enter the command >>>>>", completer=completer)
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            controllers.write_to_file()
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')
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
            controllers.change_phone(*args)
        elif command == 'change-email':
            controllers.change_email(*args)
        elif command == 'change-address':
            controllers.change_address(*args)
        elif command == 'change-birthday':
            controllers.change_birthday(*args)
        elif command == 'change-note':
            controllers.change_note(*args)
        elif command =='show-address':
            controllers.show_address(*args)
        elif command =='show-email':
            controllers.show_email(*args)
        elif command =='show-phone':
            controllers.show_phone(*args)
        elif command =='show-birthday':
            controllers.show_birthday(*args)
        elif command =='show-note':
            controllers.show_note(*args)
        elif command == 'delete-phone':
            controllers.delete_phone(*args)
        elif command == 'delete-email':
            controllers.delete_email(*args)
        elif command == 'delete-birthday':
            controllers.delete_birthday(*args)
        elif command == 'delete-address':
            controllers.delete_address(*args)
        elif command == 'delete-contact':
            controllers.delete_contact(*args)
        elif command == 'delete-note':
            controllers.delete_note(*args)
        elif command == "show-birthdays":
            controllers.show_birthdays(*args)
        elif command =='send-sms':
            controllers.send_sms(*args)
        elif command =='send-voice':
            controllers.voice_message(*args)
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
