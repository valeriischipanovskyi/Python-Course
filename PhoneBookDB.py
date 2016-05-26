import sqlite3


class PhoneBookDB:

    conn = sqlite3.connect('dbphone.sqlite')

    def __init__(self):
        self.phone_book = {}

    def __iter__(self):
        for name, phone_number in self.phone_book.items():
            yield name, phone_number

    def load_dictionary(self):
        pass


    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE dbphone(name varchar(30), phone_number varchar(20))')
        self.conn.commit()

    def create_phone_book(self):
        while True:
            if "Start":
                name = input("Enter name user: ")
                phone_number = input("Enter phone number: ")
                if name and phone_number:
                    val_str = "'{}', '{}'".format(name, phone_number)
                    sql_str = "INSERT INTO dbphone (name, Phone_number) VALUES ({});".format(val_str)
                    self.conn.execute(sql_str)
                    self.conn.commit()
                    print("New user? Yes/No")
                    new_user = input('')
                    if new_user == "Yes":
                        continue
                    else:
                        break
                    # return self.conn.total_changes

    def read_phone_book(self):
        sql_str = "SELECT * from dbphone"
        cursor = self.conn.execute(sql_str)
        rows = cursor.fetchall()

        return print(rows)

    def update_phone_book(self):
        name = input("Enter name user: ")
        phone_number = input("Enter phone number: ")
        val_str = "'{}', '{}'".format(name, phone_number)
        print(val_str)
        sql_str = "UPDATE dbphone SET (name, phone_number) WHERE name={}".format(val_str)
        self.conn.execute(sql_str)
        self.conn.commit()
        # return self.conn.total_changes

    def delete_user_phone(self,):
        name = input("Enter change name")
        sql_str = "DELETE FROM dbphone WHERE name='{}'".format(name)
        self.conn.execute(sql_str)
        self.conn.commit()
        # return self.conn.total_changes

Create = PhoneBookDB()

while True:
    print("""Make your choice:
    0. Ctable
    1. Create
    2. Read
    3. Update
    4. Delete""")
    choice = input("")
    choice_menu = {'Ctable': Create.create_table,
                   'Create': Create.create_phone_book,
                   'Read': Create.read_phone_book,
                   'Update': Create.update_phone_book,
                   'Delete': Create.delete_user_phone}
    if choice not in choice_menu.keys():
        print("Enter you choice")
    else:
        choice_menu[choice]()

