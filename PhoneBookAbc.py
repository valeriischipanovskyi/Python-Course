from abc import abstractmethod, ABCMeta
import sqlite3


class PhoneBookAbc(metaclass=ABCMeta):
    def __init__(self):
        self.phone_book = {}

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def load_dictionary(self):
        pass

    @abstractmethod
    def create_phone_book(self):
        pass

    @abstractmethod
    def read_phone_book(self):
        pass

    @abstractmethod
    def update_phone_book(self):
        pass

    @abstractmethod
    def delete_user_phone(self):
        pass

    @abstractmethod
    def connect_db(self):
        conn = sqlite3.connect('dbphone.sqlite')
        cursor = conn.cursor()
        cursor.execute('Create table dbphone(name varchar(30), phone_number varchar(20)')
        conn.commit()
