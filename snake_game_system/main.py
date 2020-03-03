from random import randrange

class Direction:
    DIRECTION_NONE = 0
    DIRECTION_LEFT = -1
    DIRECTION_RIGHT = 1
    DIRECTION_UP = -2
    DIRECTION_DOWN = 2

class CellType:
    EMPTY = 0
    SNAKE_NODE = 1
    FOOD = 2

class Cell:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__type = CellType.EMPTY
    
    def get_cell_type(self):
        return self.__type
    
    def set_cell_type(self, cell_type):
        self.__type = cell_type
    
    def get_row(self):
        return self.__row

    def set_row(self):
        return self.__col

class Board:
    def __init__(self, row_count, col_count):
        self.__row_count = row_count
        self.__col_count = col_count
        self.__cells = [[0 for i in range(self.__row_count)] for j in range(self.__col_count)]

        for row in range(self.__row_count):
            for col in range(self, self.__col_count):
                self.__cells = Cell(row, col)
    
    def generate_food(self):
        row = randrange(0, 9)
        col = randrange(0, 9)
        self.__cells[row][col] = Cell.set_cell_type(CellType.FOOD)
        print("food generated at ", row, col)
    
    def get_cell(self, row, col):
        self.__cells[row][col]


class Game:
    def __init__(self, snake, board):
        self.__snake = snake
        self.__board = board
        self.__game_over = False
        self.__direction = Direction.DIRECTION_RIGHT

    def get_snake(self):
        return Snake
    
    def update(self):
        print('updating game')
        if not self.__game_over:
            if self.__direction != Direction.DIRECTION_NONE:
                next_cell = self.get_next_cell(self.__snake.get_head())
                if self.__snake.check_crash(next_cell):
                    self.__direction = Direction.DIRECTION_NONE
                    self.__game_over = True
                else:
                    self.__snake.move_next(next_cell)
                    if next_cell.get_cell_type() == "FOOD":
                        self.__snake.grow(next_cell)
                        self.__board.generate_food()
            
    def get_next_cell(self, current_position):
        row = current_position.get_row()
        col = current_position.get_col()
        if direction == DIRECTION_RIGHT:
            col += 1
        if direction == DIRECTION_LEFT:
            col -= 1
        if direction == DIRECTION_UP:
            row -= 1
        if direction == DIRECTION_DOWN:
            row += 1
        return self.__board.get_cell(row, col)

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

class Snake:
    def __init__(self, init_pos):
        self.__init_pos = init_pos
        self.__head = LinkedList(self.__init_pos)

    def check_crash(self, next_cell):
        cell = self.__init_pos
        while cell:
            if cell == next_cell:
                return True
            cell = cell.next
        return False
    
    def get_head(self):
        return self.__head

    def grow(self, next_cell):
        next_cell.next = self.__head
        self.__head = next_cell
        
    
    def move_next(self, next_cell):
        # tail = 
        pass

if __name__ == "__main__":
    print("going to start game")
    board_obj = Board(10, 10)
    cell_obj = Cell(0, 0)
    snake_obj = Snake(cell_obj)
    game_obj = Game(cell_obj, board_obj)
    game_obj.game_over = False
