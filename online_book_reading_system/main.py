
class User:

    def __init__(self, id, name, details):
        self.__id = id
        self.__name = name
        self.__details = details
    
    def renew_membership(self):
        pass

    def get_id(self):
        return self.__id

    def get_details(self):
        return self.__details
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
class Book:

    def __init__(self, book_id, details, title):
        self.__book_id = book_id
        self.__details = details
        self.__title = title
    
    def get_id(self):
        return self.__book_id
    
    def get_details(self):
        return self.__details
    
    def get_title(self):
        return self.__title
    
class Library:

    def __init__(self):
        self.__books = {}
    
    def add_book(self, book: object):
        if book.get_id() in self.__books:
            return 
        self.__books[book.get_id()] = book

    def remove_book(self, book: object):
        if book.get_id() in self.__books:
            del self.__books[book.get_id()]
            return 'book successfully deleted'
        return "book doesn't exist in database"

    def find_book(self, id):
        if id in self.__books:
            return self.__books[id] 
        

class Display:

    def __init__(self):
        self.__active_user = None
        self.__active_book = None
        self.__page_number = 0
    
    def turn_page_forward(self):
        self.__page_number += 1

    def turn_page_backward(self):
        self.__page_number -= 1
        
    def display_user(self, active_user):
        self.__active_user = active_user
    
    def display_book(self, active_book):
        self.__page_number = 0
        self.__active_book = active_book
        # refresh_page()
        # refresh_title()
        # refresh_details()

    
class UserManager:

    def __init__(self):
        self.__users = {}
    
    def register_user(self, user: object):
        if user.get_id() in self.__users:
            return "already has account"
        self.__users[user.get_id()] = user
        return "successfully registered"
    
    def remove_user(self, user: object):
        if user.get_id() in self.__users:
            del self.__users[user.get_id()]
            return "successfully deleted account"
        return "user doesn't exist in database"
    
    def find_user(self, id: int):
        if id in self.__users:
            return self.__users[id]
        else:
            return "user does not exist"

class OnlineReaderSystem:
    def __init__(self):
        self.__library_obj = Library()
        self.__display_obj = Display()
        self.__user_mngr_obj = UserManager()
        self.__active_book = None
        self.__active_user = None
    
    def get_library(self):
        return self.__library_obj
    
    def get_display_obj(self):
        return self.__display_obj
    
    def get_user_manager(self):
        return self.__user_mngr_obj
    
    def set_active_user(self, active_user: object):
        self.__active_user = active_user
        self.__display_obj.display_user(active_user)
    
    def get_active_user(self):
        return self.__active_user
    
    def set_active_book(self, active_book: object):
        self.__active_book = active_book
        self.__display_obj.display_book(active_book)
    
    def get_active_book(self):
        return self.__active_book



if __name__ == "__main__":

    online_reader_sys_obj = OnlineReaderSystem()
    # create book objects
    golang_book = Book(1, "Concurrency and parallelism", "Golang")
    python_book = Book(2, "Advance Python", "Python")
    ds_book = Book(3, "Data structure and algorithm", "DS")
    design_book = Book(4, "System Designing", "HLD & LLD")

    # add book objects into in memmory db
    online_reader_sys_obj.get_library().add_book(golang_book)
    online_reader_sys_obj.get_library().add_book(python_book)
    online_reader_sys_obj.get_library().add_book(ds_book)
    online_reader_sys_obj.get_library().add_book(design_book)

    # create user objects
    user1 = User(1, "", 'Peter')
    user2 = User(2, "", "Jack")
    user3 = User(3, "", "Ryan")
    # add user objects into in memory db
    online_reader_sys_obj.get_user_manager().register_user(user1)
    online_reader_sys_obj.get_user_manager().register_user(user2)
    online_reader_sys_obj.get_user_manager().register_user(user3)

    # set active user and active book
    online_reader_sys_obj.set_active_book(golang_book)
    online_reader_sys_obj.set_active_user(user1)
    # start reading book
    online_reader_sys_obj.get_display_obj().turn_page_forward()
    online_reader_sys_obj.get_display_obj().turn_page_forward()



