from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Account(ABC):
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


class Admin(Person):
    def __init__(self, id, name, phone, email, address: object, account: object):
        super().__init__(self, id, name, phone, email, address, account)

    def block_user(self):
        pass

    def un_block_user(self):
        pass

    def enable_page(self):
        pass

    def disable_page(self):
        pass


class User(Person):
    def __init__(self, id, name, phone, email, address: object, account: object,
                 date_joined, profile: object):
        self.__date_joined = date_joined
        self.__profile = profile
        self.__user_follows = {}
        self.__page_follows = {}
        self.__user_connections = {}
        self.__user_suggestion = {}
        self.__group_follows = {}
        self.__connection_invitations = {}
        self.__posts = []
        self.__pages = []
        super().__init__(self, id, name, phone, email, address, account)

    def send_message(self, message: object, reciever: object):
        pass

    def create_post(self, post: object):
        self.__posts.append(post)

    def send_connection(self):
        pass

    def delete_post(self, post: object):
        self.__posts.remove(post)

    def follow_page(self, page: object):
        self.__pages.append(page)

    def unfollow_page(self, page: object):
        self.__pages.remove(page)

    def follow_group(self, group: object):
        self.__group_follows.append(group)

    def unfollow_group(self, group: object):
        self.__group_follows.remove(group)


class ConnectionInvititation:
    pass


class Profile:
    def __init__(self, profile_pic, cover_photo, gender, work_experience: list,
                 education: list, places: list):
        self.__profile_pic = profile_pic
        self.__cover_photo = cover_photo
        self.__gender = gender
        self.__work_experience = []
        self.__educations = []
        self.__places = []

    def add_work_experience(self, work: object):
        self.__work_experience.append(work)

    def delete_work_experience(self, work: object):
        self.__work_experience.remove(work)

    def add_education(self, education: object):
        self.__educations.append(education)

    def delete_education(self, education: object):
        self.__educations.remove(education)

    def add_place(self, place: object):
        self.__places.append(place)

    def delete_place(self, place: object):
        self.__places.remove(place)


class Work:
    def __init__(self, title, company, address: object, start_date, end_date, description):
        self.__title = title
        self.__company = company
        self.__address = address
        self.__start_date = start_date
        self.__end_date = end_date
        self.__description = description


class Education:
    pass


class Place:
    pass


class Page:
    def __init__(self, id, page_name, description, type, users_count):
        self.__id = id
        self.__page_name = page_name
        self.__description = description
        self.__type = type
        self.__user_count = users_count


class Group:
    def __init__(self, id, name, created_at, description):
        self.__id = id
        self.__name = name
        self.__created_at = created_at
        self.__description = description
        self.__total_users = 0
        self.__users = []

    def add_user(self, user: object):
        self.__users.append(user)
        self.__total_users += 1

    def delete_user(self, user):
        self.__users.remove(user)

    def update_description(self, description):
        self.__description = description


class Post:
    def __init__(self, id, text, user: object):
        self.__id = id
        self.__user = user
        self.__like_count = 0
        self.__share_count = 0
        self.__comments = []
        self.__liked_user = []

    def add_comment(self, comment: object):
        self.__comments.append(comment)

    def delete_comment(self, comment: object):
        self.__comments.remove(comment)

    def like(self, user: object):
        self.__liked_user.append(user)
        self.__liked_user += 1

    def dislike(self, user: object):
        self.__liked_user.remove(user)
        self.__like_count -= 1


class Comment:
    def __init__(self, id, like_count, text, user: object):
        self.__id = id
        self.__like_count = like_count
        self.__text = text
        self.__user = user


class Message:
    def __init__(self, msg_id, msg_body, media):
        self.__msg_id = msg_id
        self.__msg_body = msg_id
        self.__media = media
        self.__recipients = []

    def add_recipient(self, recipient):
        self.__recipients.append(recipient)

    def delete_recipient(self, recipient):
        self.__recipients.remove(recipient)
