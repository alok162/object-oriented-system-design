from abc import ABC, abstractmethod


class Request:
    def __init__(self, request_time, floor_no, direction):
        self.__request_time = request_time
        self.__floor_no = floor_no
        self.__direction = direction


class User:
    def __init__(self, request: object):
        self.__requst = request

    def request(self):
        pass


class Status:
    def __init__(self, current_floor, direction, final_destination):
        self.__current_floor = current_floor
        self.__direction = direction
        self.__final_destination = final_destination


class ElevatorController:
    def __init__(self, elevator: object):
        self.__elevator = elevator

    def start_elevator(self):
        pass

    def shut_down_elevator(self):
        pass

    def reset_elevator(self):
        pass


class Elevator:
    def __init__(self, status):
        self.__stops = []
        self.__status = status

    def curr_floor(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def open_door(self):
        pass

    def close_door(self):
        pass

    def get_status(self):
        pass

    def update_intermediate_stop(self):
        pass


class Button(ABC):
    def __init__(self, direction):
        self.__direction = direction

    def place_request(self):
        pass


class FloorButton(Button):
    def __init__(self, direction):
        self.__direction = direction
        super().__init__(self, direction)

    def place_request(self):
        pass


class ElevatorButton(Button):
    def __init__(self, direction):
        self.__direction = direction
        super().__init__(self, direction)

    def place_request(self):
        pass
