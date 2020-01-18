class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Account:
    def __init__(self, user_name, password, acc_status, address: object):
        self.__user_name = user_name
        self.__password = password
        self.__acc_status = acc_status
        self.__address = address

    def reset_password(self, password):
        self.__password = password


class Employee:
    def __init__(self, account: object, date_joined):
        self.__account = account
        self.__date_joined = date_joined


class Respondant(Employee):

    def __init__(self):
        self.__is_free = True

    def is_free(self):
        return self.__is_free

    def take_call(self):
        self.__is_free = False

    def endup_call(self):
        self.__is_free = True

    def escelate_call(self):
        # escalate to manager
        pass


class Manager(Employee):
    def __init__(self):
        self.__respondants = []
        self.__is_free = True

    def is_free(self):
        return self.__is_free

    def take_call(self):
        self.__is_free = False

    def endup_call(self):
        self.__is_free = True

    def add_respondant(self, respondant: object):
        self.__respondants.append(respondant)

    def remove_respondant(self, respondant: object):
        self.__respondants.remove(respondant)

    def escelate_call(self):
        # escalate to director
        pass


class Director(Employee):
    def __init__(self):
        self.__is_free = True
        self.__managers = []

    def is_free(self):
        return self.__is_free

    def take_call(self):
        self.__is_free = False

    def endup_call(self):
        self.__is_free = True

    def add_manager(self, manager: object):
        self.__managers.append(manager)

    def remove_manager(self, manager: object):
        self.__managers.remove(manager)
