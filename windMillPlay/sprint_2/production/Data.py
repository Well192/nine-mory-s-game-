import numpy as np


class Position:
    def __init__(self, x, y):
        self.empty = True
        self.x = int(x)
        self.y = int(y)
        self.id = 0  # id de una posicion sin ficha
        self.indicator = 0

    def in_the_radio(self, x, y):
        if np.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) < 10:
            return True
        return False

    def set_coor(self, x, y):
        self.x = x
        self.y = y


position_list = list()
position_list.append(Position(25, 25))
position_list.append(Position(350, 25))
position_list.append(Position(675, 25))
position_list.append(Position(675, 345))
position_list.append(Position(675, 675))
position_list.append(Position(350, 675))
position_list.append(Position(25, 675))
position_list.append(Position(25, 345))
position_list.append(Position(105, 105))
position_list.append(Position(350, 105))
position_list.append(Position(592, 105))
position_list.append(Position(592, 350))
position_list.append(Position(592, 592))
position_list.append(Position(350, 592))
position_list.append(Position(105, 592))
position_list.append(Position(105, 345))
position_list.append(Position(200, 200))
position_list.append(Position(350, 203))
position_list.append(Position(495, 203))
position_list.append(Position(495, 350))
position_list.append(Position(495, 495))
position_list.append(Position(350, 495))
position_list.append(Position(200, 495))
position_list.append(Position(200, 350))
