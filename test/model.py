import pickle


class Phones(object):

    def __init__(self):
        try:
            with open('phones.txt', 'r') as f:
                self.contacts = pickle.load(f)
        except:
            self.contacts = {}

    
    def save(self):
        with open('phones.txt', 'w') as f:
            pickle.dump(self.contacts, f)


    def fail_if_exists(self, name):
        if name in self.contacts:
            raise ValueError
    
    
    def fail_if_doesnt_exist(self, name):
        if name not in self.contacts:
            raise ValueError
    
    
    def add_contact(self, name, phone):
        self.fail_if_exists(name)
        self.contacts[name] = phone


    def get_contacts(self):
        return '\n'.join(["%s: %s" % (name, self.contacts[name]) for name in sorted(self.contacts.keys())])


    def get_contact(self, name):
        self.fail_if_doesnt_exist(name)
        return self.contacts[name]


    def delete_contact(self, name):
        self.fail_if_doesnt_exist(name)    
        del(self.contacts[name])
            

    def update_contact(self, name, phone):
        self.fail_if_doesnt_exist(name)    
        self.contacts[name] = phone
