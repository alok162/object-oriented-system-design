from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


class Account:
    def __init__(self, id, password, status):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self, password):
        self.__password = password


class Employee(Person):
    def __init__(self, account: object, date_joined):
        self.__account = account
        self.__date_joined = date_joined


class Receptionist(Employee):
    def create_reservation(self):
        pass

    def search_customer(self):
        pass

    def register_customer(self):
        pass


class Manager(Employee):
    def add_employee(self):
        pass

    def delete_employee(self):
        pass


class Waiter(Employee):
    def __init__(self, waiter_id):
        self.__waiter_id = waiter_id
        self.__orders = []

    def take_order(self, order: object):
        self.__orders.append(order)

    def serve_order(self):
        pass


class Chef(Employee):
    def prepare_order(self, order: object):
        pass


class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Branch:
    def __init__(self, branch_name, address: object):
        self.__branch_name = branch_name
        self.__address = address


class Restaurant:
    def __init__(self, name, founded_year):
        self.__name = name
        self.__founded_year = founded_year
        self.__branches = []

    def add_branch(self, branch: object):
        self.__branches.append(branch)

    def close_branch(self, branch):
        self.__branches.remove(branch)


class Table:
    def __init__(self, table_id, max_capacity, location, seats: list):
        self.__table_id = table_id
        self.__max_capacity = max_capacity
        self.__seats = seats
        self.__is_free = True

    def book_table(self):
        self.__is_free = False


class Reservation:
    def __init__(self, id, booking_time, no_of_people, status, notes, checkin_time,
                 customer: object, table: object):
        self.__id = id
        self.__booking_time = booking_time
        self.__no_of_people = no_of_people
        self.__status = status
        self.__notes = notes
        self.__checkin_time = checkin_time
        self.__customer = customer
        self.__table = table

    def update_no_of_people(self, count):
        self.__no_of_people = count


################################
# restaurant menu
class MenuItem:
    def __init__(self, item_id, item_name, price, description):
        self.__item_id = item_id
        self.__item_name = item_name
        self.__price = price
        self.__description = description

    def update_price(self, price):
        self.__price = price


class MenuSection:
    def __init__(self, section_name, menu_items: list, description):
        self.__section_name = section_name
        self.__menu_items = menu_items
        self.__description = description

    def add_menu_item(self, item):
        self.__menu_items.append(item)

    def delete_menu_item(self, item):
        self.__menu_items.remove(item)


class Menu:
    def __init__(self, title, description, menu_sections: list):
        self.__title = title
        self.__description = description
        self.__menu_sections = menu_sections

    def add_menu_section(self, menu_section):
        self.__menu_sections.append(menu_section)

    def remove_menu_section(self, menu_section):
        self.__menu_sections.remove(menu_section)
