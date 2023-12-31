commands = [
    "",
    "{:^50}|{:^50}|{:^50}|".format("Action", "Command with expected values", "Result"),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show all commands", "help", "Show you all existing commands"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Close the application", "close or exit", "Close the application"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add new contact",
        "add <name> <phone>",
        "The contact will be added to your address book",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add address to the contact",
        "add-address <name> <address>",
        "The address will be added to existing contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add email to the contact",
        "add-email <name> <email>",
        "The email will be added to existing contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add birthday to the contact",
        "add-birthday <name> <birthday>",
        "The birthday will be added to existing contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add note to address book",
        "add-note <title> <description>",
        "The note will be added to your address book",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show all contacts", "all-contacts", "Show all contacts from your address book"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show all notes", "all-notes", "Show all notes from your address book"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Find existing contact",
        "find <name>",
        "Show existing contact with all information",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Change phone of the contact",
        "change-phone <name> <new-phone>",
        "Replace existing phone with a new one",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Change email of the contact",
        "change-email <name> <new-email>",
        "Replace existing email with a new one",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Change birthday of the contact",
        "change-birthday <name> <new-birthday>",
        "Replace existing birthday with a new one",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Change address of the contact",
        "change-address <name> <new-address>",
        "Replace existing address with a new one",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Update note", "change-note <title> <new-des>", "Change note description"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show address of the contact",
        "show-address <name>",
        "Show  address of the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show email of the contact", "show-email <name>", "Show email of the contact"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show birthday of the contact",
        "show-birthday <name>",
        "Show birthday of the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show phone of the contact", "show-phone <name>", "Show phone of the contact"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show note", "show-note <title>", "Show note from your address book"
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete phone from the contact",
        "delete-phone <name>",
        "Delete phone from the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete address from the contact",
        "delete-address <name>",
        "Delete address from the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete email from the contact",
        "delete-email <name>",
        "Delete email from the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete birthday from the contact",
        "delete-birthday <name>",
        "Delete birthday from the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete contact from your address book",
        "delete-contact <name>",
        "Delete contact from your address book",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete note from your address book",
        "delete-note <title>",
        "Delete note from your address book",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Show the nearest birthdays",
        "show-birthdays <period>",
        "Show all birthdays in mentioned period",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Send sms to contact",
        "send-sms <contact-name>",
        "SMS will be sent to the contact",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Send voice message",
        "send-voice <contact-name>",
        "The phone call will read the message you send.",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Add new tag to note",
        "add-note-tag <note-name> <note-tag>",
        "Tag will be added to the note",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Delete tag from the note",
        "delete-note-tag <note-name> <note-tag>",
        "Tag will be removed from the note",
    ),
    "",
    "{:<50}|{:^50}|{:^50}|".format(
        "Search contact by input", "search <input>", "Search contact by input"
    ),
    "",
]

commands_array = [
    "help",
    "exit",
    "close",
    "help",
    "add",
    "add-address",
    "add-email",
    "add-birthday",
    "add-note",
    "all-contacts",
    "all-notes",
    "find",
    "change-phone",
    "change-email",
    "change-address",
    "change-birthday",
    "change-note",
    "show-address",
    "show-email",
    "show-phone",
    "show-birthday",
    "search-notes",
    "delete-phone",
    "delete-email",
    "delete-birthday",
    "delete-address",
    "delete-contact",
    "delete-note",
    "show-birthdays",
    "add-note-tag",
    "delete-note-tag",
    "send-sms",
    "send-voice" "search",
]
