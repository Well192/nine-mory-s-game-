import numpy as np

class Position:
    def __init__(self, x, y,indicator):
        self.empty = True
        self.x = int(x)
        self.y = int(y)
        self.id = 0
        self.indicator = int(indicator)

    def in_the_radio(self, x, y):
        if np.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) < 10:
            return True
        return False

    def set_coor(self, x, y):
        self.x = x
        self.y = y

    def get_indicator(self, x, y):
        if self.in_the_radio(x,y):
            return self.indicator


position_list = list()
#Primer Cuadrado
position_list.append(Position(25, 25,1))
position_list.append(Position(350, 25,0))
position_list.append(Position(675, 25,1))
position_list.append(Position(675, 345,0))
position_list.append(Position(675, 675,1))
position_list.append(Position(350, 675,0))
position_list.append(Position(25, 675,1))
position_list.append(Position(25, 345,0))

#Segundo Cuadrado
position_list.append(Position(105, 105, 0))
position_list.append(Position(350, 105, 1))
position_list.append(Position(592, 105,0))
position_list.append(Position(592, 350,1))
position_list.append(Position(592, 592,0))
position_list.append(Position(350, 592, 1))
position_list.append(Position(105, 592, 0))
position_list.append(Position(105, 345, 1))

#Tercer cuadrado
position_list.append(Position(200, 200, 1))
position_list.append(Position(350, 203, 0))
position_list.append(Position(495, 203, 1))
position_list.append(Position(495, 350, 0))
position_list.append(Position(495, 495, 1))
position_list.append(Position(350, 495, 0))
position_list.append(Position(200, 495, 1))
position_list.append(Position(200, 350, 0))
