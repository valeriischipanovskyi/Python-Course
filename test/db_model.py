from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.dat'
db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(12))
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __repr__(self):
        return '<Account %s: %s>' % (self.name, self.phone)

        
class Phones(object):
    
    def __init__(self, db=db):
        self.db = db


    def add_contact(self, name, phone):
        acc = Account(name, phone)
        self.db.session.add(acc)
        self.db.session.commit()

    def get_contacts(self):
        return '\n'.join([a.__repr__() for a in Account.query.all()])

    def get_contact(self, name):
        return Account.query.filter_by(name=name)[0]

    def delete_contact(self, name):
        Account.query.filter_by(name=name).delete()
        self.db.session.commit()
            
    def update_contact(self, name, phone):
        acc = Account.query.filter_by(name=name)[0]
        acc.phone = phone
        self.db.session.commit()

    def save(self):
        pass
