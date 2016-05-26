import view
import db_model

view.print_title()
phones = db_model.Phones()


while True:
    s = view.get_action()
    if s in 'qQ':
        phones.save()
        break
    elif s == 'c':
        name = view.get_name()
        phone = view.get_phone()
        try:
            phones.add_contact(name, phone)
        except ValueError, IndexError:
            view.print_message('Name exists')
        except db_model.db.exc.IntegrityError:
            view.print_message("Name doesn't exist")
    elif s == 'l':
        if phones.get_contacts():
            view.print_message(phones.get_contacts())
        else:
            view.print_message('Base is empty')
    elif s == 'f':
        name = view.get_name()
        try:
            view.print_message(phones.get_contact(name))
        except ValueError:
            view.print_message("Name doesn't exist")
        except IndexError:
            view.print_message("Name doesn't exist")
    elif s == 'd':
        name = view.get_name()
        try:
            phones.delete_contact(name)
        except ValueError:
            view.print_message("Name doesn't exist")
        except IndexError:
            view.print_message("Name doesn't exist")
    elif s == 'u':
        name = view.get_name()
        phone = view.get_phone()
        try:
            phones.update_contact(name, phone) 
        except ValueError:
            view.print_message("Name doesn't exist")
        except IndexError:
            view.print_message("Name doesn't exist")
