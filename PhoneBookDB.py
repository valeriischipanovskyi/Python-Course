"""
Create
Read
Update
Delete
"""
import sqlite3
import PhoneBookAbc

class PhoneBook(PhoneBookAbc):
    PHONE_BOOK_FILE = 'phone_book.txt'

    def __iter__(self):
        for name, phone_number in self.phone_book.items():
            yield name, phone_number


    def load_dictionary(self):
        self.phone_book.clear()

        file = open(PhoneBook.PHONE_BOOK_FILE, 'r')
        for line in file.readlines():
            name, phone_number = line.strip().split()
            self.phone_book[name] = phone_number
        file.close()

    def create_phone_book(self):
        while True:
            if "Start":
                name = input("Enter name user: ")
                phone_number = input("Enter phone number: ")
                if name and phone_number:
                    with open(PhoneBook.PHONE_BOOK_FILE, 'a+t') as f:
                        f.write("{} {}\n".format(name, phone_number))
                    print("New user? Yes/No")
                    new_user = input('')
                    if new_user == "Yes":
                        continue
                    else:
                        break


    def read_phone_book(self):
        self.load_dictionary()
        with open(PhoneBook.PHONE_BOOK_FILE, 'a+t') as f:
            f.read()
        for name, phone_number in self.phone_book.items():
            print(name, " : ", phone_number)
            if len(self.phone_book) == 0:
                print('Not Search User name')


    def update_phone_book(self):
        self.load_dictionary()
        serch = input("Enter name to search for: ")
        if serch in self.phone_book.keys():
            print(serch, " : ", self.phone_book[serch])
        else:
            print("User not found")


    def delete_user_phone(self):
        self.load_dictionary()
        enter_delete_user = input("Remove Name and Number: ")
        if enter_delete_user in self.phone_book.keys():
            del self.phone_book[enter_delete_user]
            file = open(PhoneBook.PHONE_BOOK_FILE, 'w')
            for name, phone_number in self.phone_book.items():
                string = name + '\t' + phone_number + '\n'
                file.write(string)
            file.close()
            print('File is delete')
        else:
            print("User not found")

Book = PhoneBook()

while True:
    print("""Make your choice:
    1. Create
    2. Read
    3. Update
    4. Delete""")
    choice = input("")
    Book.choice_menu = {'Create': Book.create_phone_book,
                        'Read': Book.read_phone_book,
                        'Update': Book.update_phone_book,
                        'Delete': Book.delete_user_phone}
    if choice not in Book.choice_menu.keys():
        print("Enter you choice")
    else:
        Book.choice_menu[choice]()

class PhoneBookDB(PhoneBookAbc):

    def __iter__(self):
        for name, phone_number in self.phone_book.items():
            yield name, phone_number

conn = sqlite3.connect('dbphone.sqlite')

    def create_table(self):
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE dbphone("name varchar(30)", "phone_number varchar(20)"')
        conn.commit()


    def create_phone_book(self, name, phone_number):
        val_str = "'{}', '{}'".format(name, phone_number)
        sql_str = "INSERT INTO phone_book (name, Phone_number) VALUES ({});".format(val_str)
        conn.execute(sql_str)
        conn.commit()
        return conn.total_changes

    def read_phone_book(self):
        sql_str = "SELECT * from PHONE_BOOK"
        cursor = conn.execute(sql_str)
        rows = cursor.fetchall()
        return rows

    def update_phone_book(name, phone_number):
        val_str = "name='{}', Phone Number={}".format(name, phone_number)
        sql_str = "Update Phone Book set {} where name= ;".format(val_str)
        conn.execute(sql_str)
        conn.commit()
        return conn.total_changes

    def delete_user_phone(self, change_name):
        sql_str = "DELETE from PHONE_BOOK where Name={}".format(change_name)
        conn.execute(sql_str)
        conn.commit()
        return conn.total_changes

create_table()
