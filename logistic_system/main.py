class User:
    def __init__(self, name, email, phone):
        self.name = name
        self. email = email
        self.phone = phone


class Product:
    def __init__(self, name, price, weight, height, width):
        self.name = name
        self.price = price
        self.weight = weight
        self.height = height
        self.width = width


class Location:
    def __init__(self, building, area, city, state, country, pin_code):
        self.building = building
        self.street = street
        self.city = city
        self.country = country
        self, pin_code = pin_code


class Order:
    def __init__(self, user, location, product, payment_details):
        self.user = user
        self.location = location
        self.product = product
        self.payment_details = payment_details


class PaymentDetails:
    def __init__(self, ammount, payment_mode, card_number=None, payment_status):
        self.ammount = ammount
        self.payment_mode = payment_mode
        self.card_number = card_number
        self.payment_status = payment_status


class LogisticSystem:
    def __init__(self):
        self.orders = self.users = []

    def take_order(self, order):
        self.orders.append(order)
        print('your order has been placed')

    def registering_new_user(self, user):
        print('registering a new user into data base')
        self.users.append(user)

    def process_order(self, order):
        print('processin an order')


if __name__ == '__main__':

    log_sys_obj = LogisticSystem()
    usr_obj = User('Alok', 'alokchoudhary162@gmail.com', 8148510823)

    list_item = []
    prod_obj1 = Product('Iphone 11', '58000', 300, 2, 5)
    prod_obj2 = Product('Macbook pro', '120000', 1500, 3, 14)
    list_item.append(prod_obj1)
    list_item.append(prod_obj2)

    loc_obj = Location('MF 19/12, Canara bank apartment',
                       'BTM 2nd Stage', 'Bangalore', 'Karnataka', 'India', '560076')

    pay_obj = PaymentDetails(
        200000, 'credit card payment', '123456789', 'Success')

    order_obj = Order(usr_obj, loc_obj, list_item, pay_obj)
    # registering a new user
    log_sys_obj.registering_new_user(usr_obj)
    log_sys_obj.take_order(order_obj)
    log_sys_obj.process_order(order_obj)
