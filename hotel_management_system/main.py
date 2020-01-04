class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Person:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


class Account:
    def __init__(self, id, password, status, address):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__address = address

    def reset_password(self, password):
        self.__password = password


class Guest(Person):
    def __init__(self, name, email, phone):
        super().__init__(self, name, email, phone)

    def get_booking(self):
        pass


class Receptionist(Person):
    def __init__(self, name, email, phone):
        super().__init__(self, name, email, phone)

    def search_customer(self, customer):
        pass

    def register_customer(self, customer):
        pass

    def make_booking(self):
        pass


class HotelBranch:
    def __init__(self, name, address: object):
        self.__name = name
        self.__address = address

    def get_room(self):
        pass


class Hotel:
    def __init__(self, name, founded_year):
        self.__name = name
        self.__founded_year = founded_year
        self.__branches = []

    def add_branch(self, hotel_branch):
        self.__branches.append(hotel_branch)

    def remove_branch(self, hotel_branch):
        self.__branches.remove(hotel_branch)


class Room:
    def __init__(self, id, floor_no, style, status, price, keys: list):
        self.__id = id
        self.__floor_no = floor_no
        self.__style = style
        self.__status = status
        self.__price = price
        self.__keys = keys
        self.__check_in = None
        self.__check_out = None
        self.__is_free = True

    def update_checkout(self, checkout):
        self.__check_out = checkout

    def book_room(self):
        self.__is_free = False


class Booking:
    def __init__(self, booking_id, created_on, start_date, check_in, check_out,
                 no_of_days, status, customer: object):
        self.__booking_id = booking_id
        self.__created_on = created_on
        self.__start_date = start_date
        self.__check_in = check_in
        self.__check_out = check_out
        self.__no_of_days = no_of_days
        self.__status = status
        self.__rooms = []
        self.__customer = customer

    def cancel_booking(self):
        pass

    def add_room(self, room: object):
        self.__rooms.append(room)

    def remove_room(self, room: object):
        self.__rooms.remove(room)
