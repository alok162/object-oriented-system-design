from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Account:
    def __init__(self, acc_no, total_balance):
        self.__acc_no = acc_no
        self.__total_balance = total_balance

    def get_balance(self):
        return self.__total_balance


class SavingAccount(Account):
    def __init__(self, acc_no, total_balance):
        super().__init__(acc_no, total_balance)


class CurrentAccount(Account):
    def __init__(self, acc_no, total_balance):
        super().__init__(acc_no, total_balance)


class Card:
    def __init__(self, card_no, card_type, user_name, card_expiry, pin):
        self.__card_no = card_no
        self.__card_type = card_type
        self.__user_name = user_name
        self.__card_expiry = card_expiry
        self.__pin = pin


class Customer:
    def __init__(self, name, email, phone, address, status, account, card):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__status = status
        self.__account = account
        self.__card = card


class Bank:
    def __init__(self, name, bank_code):
        self.__name = name
        self.__bank_code = bank_code
        self.__atms = []

    def add_atm(self, atm):
        self.__atms.append(atm)

    def remove_atm(self, atm):
        self.__atms.remove(atm)


class ATM:
    def __init__(self, atm_id, address, cash_dispenser, keypad, screen, printer, cash_deposit):
        self.__atm_id = atm_id
        self.__address = address
        self.__cash_dispenser = cash_dispenser
        self.__keypad = keypad
        self.__screen = screen
        self.__printer = printer
        self.__cash_deposit = cash_deposit

    def authenticate_user(self):
        pass

    def make_transaction(self):
        pass


class CashDispenser:
    def can_dispense(self):
        pass

    def dispense_cash(self):
        pass


class Keypad:
    def input(self):
        pass


class Screen:
    def show_message(self):
        pass

    def transaction_type(self):
        pass


class Printer:
    pass


class Transaction(ABC):
    def __init__(self, transaction_id, created_at, status: object):
        self.__transaction_id = transaction_id
        self.__created_at = created_at
        self.__status = status

    def make_transaction(self):
        pass


class Transfer(Transaction):
    def __init__(self, sender_acc_id, reciever_acc_id):
        self.__sender_acc_id = sender_acc_id
        self.__reciever_acc_id = reciever_acc_id


class BalanceEnquiry(Transaction):
    def __init__(self, accound_id):
        self.__account_id = accound_id

    def get_balance(self):
        pass


class Withdraw(Transaction):
    def __init__(self, acc_id):
        self.__acc_id = acc_id

    def draw_amount(self):
        pass
