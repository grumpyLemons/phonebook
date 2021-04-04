import json
import exceptions


# Phone book
class PhoneBook:

    def __init__(self, book_id=0) -> None:  # initialisation, basically old save_file function
        self.book_id = book_id
        try:
            with open(f"phonebook{book_id}.json", "r") as file:
                self.contacts_dictionary = json.load(file)
        except FileNotFoundError or json.decoder.JSONDecodeError:
            with open(f"phonebook{book_id}.json", "w") as file:
                self.contacts_dictionary = {}

    def __len__(self) -> int:  # return length of the phone book
        return len(self.contacts_dictionary)

    def __str__(self) -> str:  # return phone book in readable format
        return ',\n'.join([f"{name}: {self.contacts_dictionary[name]}" for name in self.contacts_dictionary])

    def save_book(self, book_id=0) -> None:  # method for saving dictionary into a json file
        with open(f"phonebook{book_id}.json", "w") as file:
            json.dump(self.contacts_dictionary, file)

    def add_contact(self, name: str, phone: str) -> None:  # add contact to the phone book
        if name not in self.contacts_dictionary:
            self.contacts_dictionary[name] = phone
        else:
            raise exceptions.ContactExists(name)

    def remove_contact(self, name: str) -> None:  # remove contact from the phone book
        if name in self.contacts_dictionary:
            self.contacts_dictionary.pop(name)
        else:
            raise exceptions.ContactNotFound(name)

    def search_for_name(self, substring: str) -> list:  # search and return contacts with given substring in their name
        fitting_entries = []
        for name in self.contacts_dictionary:
            if substring in name:
                fitting_entries.append(name)
        return fitting_entries

    def bulk_add(self, data: tuple) -> None:  # add multiple contacts
        for (name, phone) in data:
            self.add_contact(name, phone)

    def bulk_remove(self, names: tuple) -> None:  # remove multiple contacts
        for name in names:
            self.remove_contact(name)

    def __del__(self) -> None:  # method to save phone book's contents before exiting the program
        self.save_book(self.book_id)
