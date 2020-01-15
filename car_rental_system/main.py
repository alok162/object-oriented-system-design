from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Account:
    def __init__(self, user_name, password, acc_status):
        self.__user_name = user_name
        self.__password = password
        self.__acc_status = acc_status

    def reset_password(self, password):
        self.__password = password


class Person(ABC):
    def __init__(self, id, name, phone, email, address: object, account: object):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__account = account
        self.__id = id


class Customer(Person):
    def __init__(self, id, name, phone, email, address, account):
        self.__total_vehicle_reserved = []
        super().__init__(self, id, name, phone, email, address, account)

    def create_reservation(self, booking: object):
        self.__total_vehicle_reserved.append(booking)

    def cancel_reservation(self, booking):
        self.__total_vehicle_reserved.remove(booking)


class Vehicle(ABC):
    def __init__(self, vehicle_number, capacity, status: object, manufact_year, model, mileage, type):
        self.__vehicle_number = vehicle_number
        self.__capacity = capacity
        self.__status = status
        self.__manufact_year = manufact_year
        self.__model = model
        self.__mileage = mileage
        self.__type = type

    def reserve_vehicle(self):
        pass

    def return_vehicle(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_number, capacity, status, manufact_year, model, mileage):
        super().__init__(self, vehicle_number, capacity,
                         status, manufact_year, model, type_car)


class Truck(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Booking:
    def __init__(self, booking_no, customer: object, vehicle: object, created_at, status, return_date, pickup_location, drop_location):
        self.__booking_no = booking_no
        self.__customer = customer
        self.__vehicle = vehicle
        self.__created_at = created_at
        self.__status = status
        self.__return_date = return_date
        self.__pickup_location = pickup_location
        self.__drop_location = drop_location
        self.__payment = None

    def make_payment(self, payment: object):
        self.__payment = payment


class Payment:
    def __init__(self, transaction_id, created_at, status, amount):
        self.__transaction_id = transaction_id
        self.__created_at = created_at
        self.__status = status
        self.__amount = amount
