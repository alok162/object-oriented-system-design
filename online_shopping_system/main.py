from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Account(ABC):
    def __init__(self, id, name, password, email, phone, address, acc_status, ):
        self.__id = id
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__name = name
        self.__password = password
        self.__acc_status = acc_status
        self.__bank_cards = []

    def reset_password(self, password):
        self.__password = password


class Customer:
    def __init__(self, account: object):
        self.__account = account
        self.__carts = []
        self.__orders = []

    def add_item_to_cart(self, item):
        self.__carts.append(item)

    def delete_item_from_cart(self, item):
        self.__carts.remove(item)

    def add_order(self, order):
        self.__orders.append(order)


class ProductCategory:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description


class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.__rating = rating
        self.__review = review
        self.__reviewer = reviewer


class Product:
    def __init__(self, id, name, description, price, product_category, seller):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__product_category = product_category
        self.__reviews = []
        self.__total_count = 0
        self.__seller = seller

    def add_review(self, review: object):
        self.__reviews.append(review)

    def delete_review(self, review: object):
        self.__reviews.remove(review)

    def add_product(self):
        self.__total_count += 1

    def update_price(self, price):
        self.__price = price


class CartItem:
    def __init__(self, product_id, price):
        self.__product_id = product_id
        self.__price = price
        self.__quantity = 1

    def add_quantity(self):
        self.__quantity += 1

    def delete_quantity(self):
        self.__quantity -= 1


class ShoppingCart:
    def __init__(self, cart_item: object):
        self.__cart_items = cart_item

    def add_item(self, cart_item):
        self.__cart_items.append(cart_item)

    def delete_item(self, cart_item):
        self.__cart_items.remove(cart_item)

    def add_quantity(self, cart_item: object):
        cart_item.add_quantity()

    def delete_quantity(self, cart_item: object):
        cart_item.delete_quantity()

    def checkout(self):
        pass


class Order:
    def __init__(self, order_number, status: object, order_date):
        self.__order_number = order_number
        self.__status = status
        self.__order_date = order_date

    def make_payment(self, payment):
        pass

    def show_status(self):
        return self.__status

    def shipment(self):
        pass


class ShipmentLog:
    def __init__(self, shipment_id, status: object):
        self.__shipment_id = shipment_id
        self.__status = status


class Shipment:
    def __init__(self, ship_id, ship_date, arrival_date):
        self.__ship_id = ship_id
        self.__ship_date = ship_date
        self.__ship_log = None

    def add_ship_log(self, log):
        self.__ship_log = log


class Notification:
    def __init__(self, notification_id, created_at, content):
        self.__id = notification_id
        self.__created_at = created_at
        self.__content = content

    def send_notification(self, user):
        pass
