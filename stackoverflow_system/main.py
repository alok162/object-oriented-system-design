from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Account(ABC):
    def __init__(self, user_name, password, acc_status, address, email, phone, reputation):
        self.__user_name = user_name
        self.__password = password
        self.__acc_status = acc_status
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__reputation = reputation

    def reset_password(self, password):
        self.__password = password


class Member:
    def __init__(self, account):
        self.__account = account

    def get_reputation(self):
        pass

    def get_email(self):
        pass

    def post_quetion(self):
        pass


class Admin(Member):
    def __init__(self, member_account: object):
        super().__init__(self, member_account)

    def block_member(self):
        pass

    def un_block_member(self):
        pass


class Notification:
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    def send_notification(self):
        pass


class Quetion:
    def __init__(self, title: str, description: str, view_count: int,
                 creation_time, update_time, asking_member):
        self.__title = title
        self.__description = description
        self.__view_count = view_count
        self.__creation_time = creation_time
        self.__update_time = update_time
        self.__asking_member = asking_member
        self.__comments = comments
        self.__answers = answers

    def add_comment(self, comment):
        self.__comments.append(comment)


class Comments:
    def __init__(self, text, creation_time, asking_member):
        self.__text = text
        self.__creation_time = creation_time
        self.__asking_member = asking_member


class Answer:
    def __init__(self, ans_text: str, accepted: bool, up_vote_count: int,
                 down_vote_count: int, creation_time, post_member: object):
        self.__ans_text = ans_text
        self.__accepted = accepted
        self.__up_vote_count = up_vote_count
        self.__down_vote_count = down_vote_count
        self.__creation_time = creation_time
        self.__post_member = post_member
