from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, zip_code, state, country):
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__state = state
        self.__country = country


class Person:
    def __init__(self, name, email, phone, address):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address


class Spot:
    def __init__(self, x, y, piece: object):
        self.__x = x
        self.__y = y
        self.__piece = piece

    def get_piece(self):
        return self.__piece

    def set_piece(self, piece: object):
        self.__piece = piece

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Piece(ABC):
    def __init__(self, white):
        self.__white = white
        self.__killed = False

    def is_killed(self):
        return self.__killed

    def set_killed(self):
        self.__killed = True

    def can_move(self, board: object, start: object, end: object):
        pass


class Knight(Piece):
    def __init__(self, white):
        self.__white = white
        self.__castling = False
        super().__init__(self, white)

    def can_move(self, board: object, start: object, end: object):
        if end.is_white() == self.__white:
            return False

        x = abs(start.get_x() - end.get_x())
        y = abs(start.get_y() - end.get_y())
        return x*y == 2


class King(Piece):
    def __init__(self, white):
        self.__white = white
        self.__castling = False
        super().__init__(self, white)

    def is_castling(self):
        return self.__castling

    def set_castling_done(self):
        self.__castling = True

    def can_move(self, board: object, start: object, end: object):
        if end.is_white() == self.__white:
            return False

        x = abs(start.get_x() - end.get_x())
        y = abs(start.get_y() - end.get_y())
        if x + y == 1:
            return True


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Pawn(Piece):
    pass


class Board:
    def __init__(self):
        self.__spots = [[]]
        self.reset_board()

    def reset_board(self):
        # initialize white peices
        self.__spots[0][0] = Spot(0, 0, Rook(True))
        self.__spots[0][1] = Spot(0, 1, Knight(True))
        self.__spots[0][2] = Spot(0, 2, Bishop(True))
        self.__spots[1][0] = Spot(1, 0, Pawn(True))
        # and so on...........

        # initialize black peices
        self.__spots[0][0] = Spot(0, 0, Rook(False))
        self.__spots[0][1] = Spot(0, 1, Knight(False))
        self.__spots[0][2] = Spot(0, 2, Bishop(False))
        self.__spots[1][0] = Spot(1, 0, Pawn(False))
        # and so on........

        # initialize remaining spots without any pieces
        for i in range(2, 6):
            for j in range(8):
                self.__spots[i][j] = Spot(i, j, None)


class Move:
    def __init__(self, player: object, start, end):
        self.__player = player
        self.__start = start
        self.__end = end
        self.__piece_moved = start.get_piece()


class Player:
    def __init__(self, white_side, address: object):
        self.__white_side = white_side
        self.__address = address

    def is_white_side(self):
        return self.__white_side
