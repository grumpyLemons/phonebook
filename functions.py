import json
import exceptions

# BASIC INTERACTIONS WITH PHONEBOOK DICTIONARY

# Save/load phonebook
def load_book(file_id=0):
    with open(f"phonebook{file_id}.json", "r") as file:
        return json.load(file)


def save_book(contacts_dictionary: dict, file_id=0):
    with open(f"phonebook{file_id}.json", "w") as file:
        json.dump(contacts_dictionary, file)


# Add/remove contacts from phonebook
def add_contact(contacts_dictionary: dict, name: str, phone: str) -> None:
    if name not in contacts_dictionary:
        contacts_dictionary[name] = phone
    else:
        raise exceptions.ContactExists(name)


def remove_contact(contacts_dictionary: dict, name: str) -> None:
    if name in contacts_dictionary:
        contacts_dictionary.pop(name)
    else:
        raise exceptions.ContactNotFound(name)


# Search substring in names
def search_name(contacts_dictionary: dict, substring: str) -> None:
    for name in contacts_dictionary:
        if substring in name:
            print(f"{name} : {contacts_dictionary[name]}")


# Print phonebook's content in alphabetical order
def print_phonebook(contacts_dictionary: dict, reverse=False) -> None:
    if reverse:
        print(sorted(contacts_dictionary)[::-1])
    else:
        print(sorted(contacts_dictionary))


# ADVANCED FUNCTIONS

# Bulk add to/remove from contact list
'''def bulk_add(contacts_dictionary, names):
    for name in names:
        add_contact(contacts_dictionary, name)
        

def bulk_remove(contacts_dictionary, names):
    for name in names:
        remove_contact(contacts_dictionary, name)

'''