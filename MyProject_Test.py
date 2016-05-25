"""
Create
Read
Update
Delete
"""
phone_book = {}
PHONE_BOOK_FILE = 'phone_book.txt'

def load():
    phone_book.clear()

    file = open(PHONE_BOOK_FILE, 'r')
    for line in file.readline():
        name, phone_number = line.strip().split(':')
        phone_book[name] = phone_number
    file.close()

# def create_phone_book():
#     while True:
#         if "Start":
#             name = input("Enter name user: ")
#             phone_number = input("Enter phone number: ")
#             if name and phone_number:
#                 with open(PHONE_BOOK_FILE, 'a+t') as f:
#                     f.write("{} {}\n".format(name, phone_number))
#                 print("New user?")
#                 new_user = input('')
#                 if new_user == "Yes":
#                     continue
#                 else:
#                     break


def create_phone_book():
    file = open(PHONE_BOOK_FILE, 'r')
    for line in file.readline():
        name, phone_number = line.strip().split()
        phone_book[name] = phone_number
    file.close()
    name = input("Enter name user: ")
    phone_number = input("Enter phone number: ")
    new_user = name + '\t' + phone_number + '\n'

    file = open(PHONE_BOOK_FILE, 'a')
    file.write(new_user)
    file.close()


def read_phone_book():
    file = open(PHONE_BOOK_FILE, 'r')
    for line in file.readline():
        name, phone_number = line.strip().split()
        phone_book[name] = phone_number
    file.close()

    for name, phone_number in phone_book.items():
        print(name, " : ", phone_number)
        if len(phone_book) == 0:
            print('Not Search User name')


def update_phone_book():
    file = open(PHONE_BOOK_FILE, 'r')
    for line in file.readline():
        name, phone_number = line.strip().split()
        phone_book[name] = phone_number
    file.close()
    serch = input("Enter name to search for: ")
    if serch in phone_book.keys():
        print(serch, " : ", phone_book[serch])
    else:
        print("User not found")


def delete_user_phone():
    file = open(PHONE_BOOK_FILE, 'r')
    for line in file.readline():
        name, phone_number = line.strip().split(':')
        phone_book[name] = phone_number
    file.close()

    enter_delete_user = input("Remove Name and Number: ")
    if enter_delete_user in phone_book.keys():
        del phone_book[enter_delete_user]
        file = open(PHONE_BOOK_FILE, 'w')
        for name, phone_number in phone_book.items():
            string = name + '\t' + phone_number + '\n'
            file.write(string)
        file.close()
        print('File is delete')
    else:
        print("User not found")

while True:
    print("""Make your choice:
    1. Create
    2. Read
    3. Update
    4. Delete""")
    choice = input("")
    choice_menu = {'Create': create_phone_book, 'Read': read_phone_book, 'Update': update_phone_book, 'Delete': delete_user_phone}
    choice_menu[choice]()
