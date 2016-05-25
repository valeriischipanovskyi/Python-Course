from abc import abstractmethod, ABCMeta



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
        pass
