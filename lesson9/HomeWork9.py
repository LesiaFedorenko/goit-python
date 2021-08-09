import re

def hello_fun():
    print("How can I help you?")
    print("Choose: add, change, phone or show all")

def good_bye():
    print("Good bye!")

def show():
    print(f"Your phone's contacts {ph_dict}")
    hello_fun()

def input_error(func):
    def inner():
        try:
            return func()
        except IndexError:
            print("You must enter the name and phone's number separated by a space")
            add_func()
        except KeyError:
            print('This contact does not exist')
            print("Will you try to enter the name again?")
            again = input('Y/N ')
            if again.upper() == "Y":
                phone()
            else:
                hello_fun()
        except ValueError:
            print('Try again')
            hello_fun()
    return inner

@input_error
def add_func():
    for_contact = contact.split()

    if for_contact[0] not in ph_dict.keys():
        ph_dict[for_contact[0]] = sanitize_phone_number(contact.removeprefix(for_contact[0]+' '))
        hello_fun()
    else:
        print("This contact exists, you want to change the number?")
        answer = input('Y/N ')
        if answer.upper() == "Y":
            change_func()
        else:
            hello_fun()

@input_error
def change_func():
    for_contact = contact.split()

    if for_contact[0] in ph_dict.keys():
        ph_dict[for_contact[0]] = sanitize_phone_number(contact.removeprefix(for_contact[0]+' '))
        hello_fun()
    else:
        print("This contact is missing, would you like to add it?")
        answer = input('Y/N ')
        if answer.upper() == "Y":
            add_func()
        else:
            hello_fun()

@input_error
def phone():
    name = input('...')
    print(ph_dict[name])
    hello_fun()

def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if len(result) == 12:
            return '+' + result
        else:
            return '+38' + result

    return inner

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = re.sub(r'\D', "", phone)
    return new_phone

ph_dict = {}
print('Hello!')
input_word = input()

while input_word.upper() not in ["GOOD BYE", "CLOSE", "EXIT"]:
    if input_word.upper() == 'HELLO':
        hello_fun()
    elif input_word.upper() == 'ADD':
        print("You must enter the name and phone's number separated by a space")
        contact = input('...')
        add_func()
    elif input_word.upper() == 'CHANGE':
        print("You must enter the name and phone's number separated by a space")
        contact = input('...')
        change_func()
    elif input_word.upper() == 'SHOW ALL' or input_word.upper() == 'SHOW':
        show()
    elif input_word.upper() == 'PHONE':
        print("You must enter the name")
        phone()
    else:
        print("Choose: add, change, phone or show all")
    input_word = input()
good_bye()
