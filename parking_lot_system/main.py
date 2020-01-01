from abc import ABC, abstractmethod


class VehicleType():
    MOTORBIKE, CAR, TRUCK = 1, 2, 3


class ParkingSpotType:
    motor_bike_spot, car_spot, truck_spot = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, email, phone, address):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address


class Vehicle(ABC):
    def __init__(self, vehicle_no, vehicle_type, ticket=None):
        self.__vehicle_no = vehicle_no
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket


class Car(Vehicle):
    def __init__(self, vehicle_no, ticket):
        super().__init__(vehicle_no, VehicleType.CAR, ticket)


class MotorBike(Vehicle):
    def __init__(self, vehicle_no, ticket):
        super().__init__(vehicle_no, VehicleType.MOTORBIKE, ticket)


class Truck(Vehicle):
    def __init__(self, vehicle_no, ticket):
        super().__init__(vehicle_no, VehicleType.TRUCK, ticket)


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True


class TruckSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(self, number, ParkingSpotType.truck_spot)


class CarSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.car_spot)


class MotorBikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(self, number, ParkingSpotType.motor_bike_spot)


class ParkingFloor(ABC):
    def __init__(self, floor_no):
        self.__floor_no = floor_no
        self.__motor_bike_spots = {}
        self.__car_spots = {}
        self.__truck_spots = {}

    def add_parking_spot(self, spot):
        switcher = {
            ParkingSpotType.motor_bike_spot: self.__motor_bike_spots.put(spot.get_number(), spot),
            ParkingSpotType.car_spot: self.__car_spots.put(spot.get_number(), spot),
            ParkingSpotType.truck_spot: self.__car_spots.put(
                spot.get_number(), spot)
        }

    def assign_vehicle_to_spot(self, vehicle: object, spot: object):
        spot.assign_vehicle(vehicle)
