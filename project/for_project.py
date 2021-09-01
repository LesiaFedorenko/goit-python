from collections import UserDict
from datetime import timedelta, date, datetime
import re
import pickle
import time


class Name:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print("Incorrect name!")

    def __str__(self):
        return f"{self.__name}"


class Phone:
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        if re.search("(^\+?(38)?0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7}$)", re.sub(r'\D', "", phone)):
            if len(re.sub(r'\D', "", phone)) == 12:
                self.__phone = '+' + re.sub(r'\D', "", phone)
            else:
                self.__phone = '+38' + re.sub(r'\D', "", phone)

        else:
            print(
                "The phone is not saved because it has an incorrect format\nTry to edit like the example: +38(***)*******")

    def __str__(self):
        return f"{self.__phone}"


class Email:
    def __init__(self, email):
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email == "-" or re.search("^[\w\.-]+@[\w\.-]+(\.[\w]+)+", email):
            self.__email = email
        else:
            print("The email is not saved because it has an incorrect format \nTry to edit like the example: *****@***.***")

    def __str__(self):
        return f"{self.__email}"


class Birthday:
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        try:
            if birthday == "-" or time.strptime(birthday, '%d/%m/%Y'):
                self.__birthday = birthday
        except ValueError:
            print('The date is not saved because it has an incorrect format \nTry to edit like the example: DD/MM/YYYY')

    def __str__(self):
        return f"{self.__birthday}"


class Address:
    def __init__(self, address):
        self.address = address
        self.__address = address

    def __str__(self):
        return f"{','.join(self.__address).title()}"


class Record:
    def __init__(self, name, phone, email, birthday, address):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.address = Address(address)

    def __str__(self):
        return f"{self.phone},{self.email},{self.birthday},{self.address}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.__str__()] = record

    def find_contact(self, name):
        for key, value in self.data.items():
            if str(name) == str(key):
                print(f"{key}: {value}")

    def del_contact(self, name):
        try:
            question= input("Are you sure?: Y/N ").lower()
            if question=='y':
                self.data.pop(name)
                print(f'{name} was deleted successfully')
        except KeyError:
            print('This contact does not exist in database')

    def edit_contact(self, name):
        print(self.data[name])
        edit_option = input("Enter an editable option (phone, email, birthday or address) and changed information:").lower()
        sep_edit_option = edit_option.split(" ")
        data = str(self.data[name]).split(',')
        if sep_edit_option[0] == 'phone':
            data[0] = sep_edit_option[1]
            AddressBook.add_record(self, Record(name, data[0], data[1], data[2], data[3:]))
        if sep_edit_option[0] == 'email':
            data[1] = sep_edit_option[1]
            AddressBook.add_record(self, Record(name, data[0], data[1], data[2], data[3:]))
        if sep_edit_option[0] == 'birthday':
            data[2] = sep_edit_option[1]
            AddressBook.add_record(self, Record(name, data[0], data[1], data[2], data[3:]))
        if sep_edit_option[0] == 'address':
            data[3] = sep_edit_option[1:]
            AddressBook.add_record(self, Record(name, data[0], data[1], data[2], data[3:]))

    def days_to_birthday(self, number_days):
        EndDate = date.today() + timedelta(days=number_days)
        list = []
        try:
            for key, val in self.data.items():
                result = re.search(r"\d{1,2}\/\d{1,2}\/\d{4}", str(val)).group()
                if datetime.strptime(result, "%d/%m/%Y").month == EndDate.month and datetime.strptime(result,
                                                                                                      "%d/%m/%Y").day == EndDate.day:
                    list.append({str(key): str(val)})
        except AttributeError:
            pass
        return list

    def __str__(self):
        print(f'Total contacts: {len(self.data)}')
        for key, val in self.data.items():
            print(f'{str(key)}:{str(val)}'.removesuffix(','))


def main():
    try:
        with open("data_test.bin", "rb") as f:
            address_book = pickle.load(f)
    except FileNotFoundError:
        address_book = AddressBook()
    while True:
        command = input("Command: ").lower()
        sep_command = command.split(" ")
        if sep_command[0] == "add" and sep_command[1] == "contact" and len(sep_command) > 2:
            address_book.add_record(
                Record(
                    sep_command[2].title(),
                    sep_command[3],
                    sep_command[4] if len(sep_command) > 4 else "-",
                    sep_command[5] if len(sep_command) > 5 else "-",
                    sep_command[6:] if len(sep_command) > 6 else "-"
                )
            )
        elif sep_command[0] == "show" and sep_command[1] == "all":
            address_book.__str__()

        elif sep_command[0] == "show" and sep_command[1] == "birthday":
            print(address_book.days_to_birthday(int(sep_command[2])))

        elif sep_command[0] == "edit" and sep_command[1] == "contact":
            address_book.edit_contact(sep_command[2].title())

        elif sep_command[0] == "delete" and sep_command[1] == "contact":
            address_book.del_contact(sep_command[2].title())

        elif sep_command[0] == "show" and sep_command[1] == "contact":
            address_book.find_contact(sep_command[2].title())

        elif sep_command[0] in ["close", "exit", "."]:
            with open("data_test.bin", "wb") as f:
                pickle.dump(address_book, f)
            print("Good bye!")
            break


if __name__ == '__main__':
    main()
