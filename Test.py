"""
Create
Read
Update
Delete
"""
phone_book = {}

while True:
    print("Make your choice:\n1. Create\n2. Read\n3. Update\n4. Delete")
    choice = input('')
    if choice == "Create":
        def create_phone_book():
            while True:
                print("Click Start from editing or Exit from Exit func")
                add = input()
                if add == "Start":
                    name = input("Enter name user: ")
                    phone_number = input("Enter phone number: ")
                    if name and phone_number:
                        phone_book[name] = phone_number
                    else:
                        continue
                elif add == "Exit":
                    break

    elif choice == "Read":
        def read_phone_book():
            print(phone_book)
    elif choice == "Update":
        def update_phone_book():
            phone_book.update(input(''))
    elif choice == "Delete":
        def delete_user_phone():
            del phone_book[input('')]
else:
    print("Make choice")

