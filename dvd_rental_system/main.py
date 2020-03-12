class DvdStatus:
    Available, Reserved = 0, 1

class DVD:
    def __init__(self, id, title, type, language, price):
        self.id = id
        self.title = title
        self.__language = language
        self.price = price
        self.type = type
    
class DvdItem(DVD):
    def __init__(self, id, title, type, language, duration, dvd_price, rent_price):
        self.__rent_price = rent_price
        self.__due_date = None
        self.__status = 0
        super().__init__(id, title, type, language, dvd_price, duration)
    
    def get_id(self):
        return self.id

    def get_status(self):
        return self.__status   
    
    def checkout_item(self):
        if self.__status == 1:
            return "already rented"
        self.__status = 1
        return "successfully rented"


class DvdLibrary:
    def __init__(self):
        self.__dvds = {}
    
    def add_dvd(self, dvd):
        dvd_id = dvd.get_id()
        if dvd_id in self.__dvds:
            return
        else:
            self.__dvds[dvd_id] = dvd
    
    def delete_dvd(self, dvd):
        dvd_id = dvd.get_id()
        if dvd_id not in self.__dvds:
            return
        del self.__dvds[dvd_id]

    def rent_dvd_to_customer(self, user, dvd_item):
        if dvd_item.get_status() == 0:
            dvd_item.checkout_item()
            user.payment()
            user.ordered()
    
    def check_for_fine(self):
        pass


class User:
    def __init__(self, id, name, address):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__total_dvd_rented = {}
    
    def get_id(self):
        return self.__id

    def payment(self):
        pass

    def ordered(self, book_item):
        self.__total_dvd_rented[book_item.get_id()] = book_item
    


class UserManager:
    def __init__(self):
        self.__users = {}
    
    def register_user(self, user):
        user_id = user.get_id()
        if user_id in self.__users:
            return "users already exist"
        self.__users[user_id] = user
        return "successfully registered"
    
    def delete_user(self, user):
        user_id = user.get_id()
        if user_id not in self.__users:
            return "users doesn't exist"
        del self.__users[user_id]
        return "successfully deleted"
    
    def find_user(self, id):
        if id in self.__users:
            return self.__users
        return "user doesn't exist"


class RentingSystem:
    def __init__(self):
        self.__dvd_library = DvdLibrary()
        self.__user_manager = UserManager()
    
    def get_dvd_library_obj(self):
        return self.__dvd_library
    
    def get_user_manager_obj(self):
        return self.__user_manager


if __name__ =='__main__':
    rent_system_obj = RentingSystem()

    user1 = User(1, "Alok", "address")
    user2 = User(2, "David", "address")
    user3 = User(3, "Mack", "address")

    rent_system_obj.get_user_manager_obj().register_user(user1)
    rent_system_obj.get_user_manager_obj().register_user(user1)
    rent_system_obj.get_user_manager_obj().register_user(user1)


    dvd1 = DvdItem(1, "AVENGER", "actions", "eng", 90, 2000, 100)
    dvd2 = DvdItem(2, "ANT MAN", "actions", "eng", 90, 1500, 80)
    dvd3 = DvdItem(3, "ANGRY BIRDS", "comedy",  "Hindi", 120, 1000, 50)

    rent_system_obj.get_dvd_library_obj().add_dvd(dvd1)
    rent_system_obj.get_dvd_library_obj().add_dvd(dvd2)
    rent_system_obj.get_dvd_library_obj().add_dvd(dvd3)

    # lent dvd
    rent_system_obj.get_dvd_library_obj().rent_dvd_to_customer(user1, dvd1)