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

    def allowed_positions(self):
        if self.indicator == 1:
            return [2,8]
        if self.indicator == 2:
            return [1,2]
        if self.indicator == 3:
            return [2,4]
        if self.indicator == 4:
            return [3,5,12]
        if self.indicator == 5:
            return [4,6]
        if self.indicator == 6:
            return [5,7,14]
        if self.indicator == 7:
            return [6,8]
        if self.indicator == 8:
            return [1,16,7]
        if self.indicator == 9:
            return [10,16]
        if self.indicator == 10:
            return [2,9,11,18]
        if self.indicator == 11:
            return [10,12]
        if self.indicator == 12:
            return [4,11,20,13]
        if self.indicator == 13:
            return [12,14]
        if self.indicator == 14:
            return [13,15,22]
        if self.indicator == 15:
            return [16,14]
        if self.indicator == 16:
            return [8,9,15,24]
        if self.indicator == 17:
            return [18,24]
        if self.indicator == 18:
            return [10,17,19]
        if self.indicator == 19:
            return [18, 20]
        if self.indicator == 20:
            return [12,19,21]
        if self.indicator == 21:
            return [20,22]
        if self.indicator == 22:
            return [14,21,23]
        if self.indicator == 23:
            return [24,22]
        if self.indicator == 24:
            return [23, 17, 16]

position_list = list()
#Primer Cuadrado
position_list.append(Position(25, 25,1))
position_list.append(Position(350, 25,2))
position_list.append(Position(675, 25,3))
position_list.append(Position(675, 345,4))
position_list.append(Position(675, 675,5))
position_list.append(Position(350, 675,6))
position_list.append(Position(25, 675,7))
position_list.append(Position(25, 345,8))

#Segundo Cuadrado
position_list.append(Position(105, 105, 9))
position_list.append(Position(350, 105, 10))
position_list.append(Position(592, 105,11))
position_list.append(Position(592, 350,12))
position_list.append(Position(592, 592,13))
position_list.append(Position(350, 592, 14))
position_list.append(Position(105, 592, 15))
position_list.append(Position(105, 345, 16))

#Tercer cuadrado
position_list.append(Position(200, 200, 17))
position_list.append(Position(350, 203, 18))
position_list.append(Position(495, 203, 19))
position_list.append(Position(495, 350, 20))
position_list.append(Position(495, 495, 21))
position_list.append(Position(350, 495, 22))
position_list.append(Position(200, 495, 23))
position_list.append(Position(200, 350, 24))
