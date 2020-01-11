from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person(ABC):
    def __init__(self, name, phone, email, address):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address


class Account(ABC):
    def __init__(self, user_name, password, acc_status, person):
        self.__user_name = user_name
        self.__password = password
        self.__acc_status = acc_status
        self.__person = person

    def reset_password(self, password):
        self.__password = password


class Admin(Person):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_movie(self, movie):
        pass

    def remove_movie(self, movie):
        pass

    def block_user(self, user):
        pass

    def un_block_user(self, user):
        pass


class User(Person):
    def __init__(self):
        self.__bookings = []

    def create_booking(self, booking):
        self.__bookings.append(booking)

    def list_booking(self):
        return self.__bookings


class Show:
    def __init__(self, show_id, date_time, start_time, end_time, movie: object):
        self.__show_id = id
        self.__date_time = date_time
        self.__start_time = start_time
        self.__end_time = end_time
        self.__movie = movie


class Movie:
    def __init__(self, title, description, duration, language, release_date, country, genre, shows: list):
        self.__title = title
        self.__description = description
        self.__duration = duration
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre
        self.__shows = shows

    def get_all_show(self):
        return self.__shows


class Booking:
    def __init__(self, id, booking_time, status, show: object):
        self.__id = id
        self.__no_of_seats = 0
        self.__booking_time = booking_time
        self.__status = status
        self.__show = show
        self.__seats = []
        self.__payment = None

    def choose_seat(self, seat: object):
        self.__seats.append(seat)

    def cancel(self):
        pass

    def make_payment(self, payment: object):
        self.__payment = payment


class Payment:
    def __init__(self, transaction_id, amount, created_on, status):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__created_on = created_on
        self.__status = status


class CinemaHall:
    def __init__(self, name, no_of_seats, seats: list, shows: list):
        self.__name = name
        self.__no_of_seats = no_of_seats
        self.__seats = seats
        self.__shows = shows


class Cinema:
    def __init__(self, name, total_hall, address, halls: list):
        self.__name = name
        self.__total_hall = total_hall
        self.___address = address
        self.__halls = halls
