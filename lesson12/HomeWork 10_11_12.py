import re
import pickle
from collections import UserDict

DEFAULT_ADDRESS_BOOK_PATH = ".address_book.bin"


def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class AddressBook(UserDict, Field):

    def add_phone(self, contact):
        for_contact = contact.split()
        if len(for_contact) == 2:
            record = Record(for_contact[0], for_contact[1])
        elif len(for_contact) == 3:
            record = Record(for_contact[0], for_contact[1], for_contact[2])

        if len(for_contact) >= 2:
            if for_contact[0] not in address_book.keys():
                address_book[for_contact[0]] = Phone.sanitize_phone_number(for_contact[1])
                hello_fun()
            else:
                print("This contact exists, you want to add the number?")
                answer = input('Y/N ')
                if answer.upper() == "Y":
                    address_book[for_contact[0]] = address_book[for_contact[0]] + ", " + Phone.sanitize_phone_number(
                        for_contact[1])
                    hello_fun()
                else:
                    hello_fun()
        else:
            print("WRONG! You must enter the name and phone's number separated by a space")
            hello_fun()

    def change_phone(self, contact):
        for_contact = contact.split()
        if len(for_contact) >= 2:
            if for_contact[0] in address_book.keys():
                address_book[for_contact[0]] = Phone.sanitize_phone_number(for_contact[1])
                hello_fun()
            else:
                print("This contact is missing, would you like to add it?")
                answer = input('Y/N ')
                if answer.upper() == "Y":
                    address_book[for_contact[0]] = Phone.sanitize_phone_number(for_contact[1])
                    hello_fun()
                else:
                    hello_fun()
        else:
            print("WRONG! You must enter the name and phone's number separated by a space")
            hello_fun()

    def find_contact(self, search_word):
        for key, value in address_book.items():
            if not search_word.isdigit():
                if key.find(search_word) != -1:
                    print(key, value)
            elif value.find(search_word) != -1:
                print(key, value)
        hello_fun()

    @staticmethod
    def delete_phone():
        try:
            name = input('...')
            del address_book[name]
            print(f'{name} successfully deleted')
            hello_fun()
        except KeyError:
            print('This contact does not exist')
            hello_fun()

    def iterator(self, item_number):
        counter = 0
        result = ""
        for key, value in address_book.items():
            result += str(key) + ": " + str(value) + "\n"
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ""
        yield result


class Record(Field):

    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        self.birthday = birthday
        if phones is None:
            self.phones = []
        else:
            self.phones = phones

    def days_to_birthday(self):
        if not self.birthday:
            return
        now = datetime.today()
        if (self.birthday(year=now.year) - now).days > 0:
            return (self.birthday(year=now.year) - now).days
        return (self.birthday(year=now.year + 1) - now).days


class Phone(Field):

    @staticmethod
    def sanitize_phone_number(phone):
        new_phone = re.sub(r'\D', "", phone)
        if len(new_phone) == 12:
            return '+' + new_phone
        else:
            return '+38' + new_phone

    @staticmethod
    def phone():
        try:
            name = input('...')
            print(address_book[name])
            hello_fun()
        except KeyError:
            print('This contact does not exist')
            hello_fun()


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%d%m%Y').date()


def hello_fun():
    print("How can I help you?")
    print(f"Choose command: {commands}")


def good_bye():
    print(f'Your finish address book {address_book}')
    print("Good bye!")


address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)
commands = ['add', 'change', 'phone', 'search', 'delete', 'show all', 'exit']
print('Hello!')
input_word = input()

while input_word.upper() not in ["GOOD BYE", "CLOSE", "EXIT"]:
    if input_word.upper() == 'HELLO':
        hello_fun()
    elif input_word.upper() == 'ADD':
        print("You must enter the name and phone's number separated by a space")
        contact = input('...')
        address_book.add_phone(contact)
    elif input_word.upper() == 'CHANGE':
        print("You must enter the name and phone's number separated by a space")
        contact = input('...')
        address_book.change_phone(contact)
    elif input_word.upper() == 'SHOW ALL' or input_word.upper() == 'SHOW':
        for page in address_book.iterator(2):
            print(page)
        hello_fun()
    elif input_word.upper() == 'PHONE':
        print("You must enter the name")
        Phone.phone()
    elif input_word.upper() == "SEARCH":
        search_world = input("Search word: ")
        address_book.find_contact(search_world)
    elif input_word.upper() == "DELETE":
        address_book.delete_phone()
    else:
        print(f"Choose command: {commands}")
    input_word = input()
dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
good_bye()
