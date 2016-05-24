"""
Create
Read
Update
Delete
"""
with open('phone_book.txt', 'rt') as f:
    s = f.read()
phone_book = {}


def create_phone_book():
    while True:
        print("Click Start from editing or Exit from exit func")
        add = input()
        if add == "Start":
            name = input("Enter name user: ")
            phone_number = input("Enter phone number: ")
            if name and phone_number:
                with open('phone_book.txt', 'wt') as f:
                    f.write("{} []\n".format('name', phone_number))
            else:
                continue
        elif add == "Exit":
            break


def read_phone_book():
    while True:
            print("Click Start from editing or Exit from exit func")
            add = input()
            if add == "Start":
                try:
                    with open('phone_book.txt', 'rt') as f:
                        for i in f:
                          print(i[input('')])
                except ValueError:
                    print("Not Search User name")
                    continue
            elif add == "Exit":
                break


def update_phone_book():
    with open('phone_book.txt', 'rt') as f:
        for i in f:
            print(i[input('')])
    i.update(input(''))


def delete_user_phone():
    print("Choice del element:")
    with open('phone_book.txt', 'rt') as f:
        for i in f:
            print(i[input('')])
    if i['']:
        del i[input('')]
    elif print(i):
        del i[input('')]
    else:
        print(phone_book)


while True:
    print("""Make your choice:
    1. Create
    2. Read
    3. Update
    4. Delete""")
    choice = input("")
    choice_menu = {'Create': create_phone_book, 'Read': read_phone_book, 'Update': update_phone_book, 'Delete': delete_user_phone}
    choice_menu[choice]()

