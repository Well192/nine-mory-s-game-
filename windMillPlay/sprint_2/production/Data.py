import numpy as np

class Position:
    def __init__(self, x, y,id):
        self.empty = True
        self.x = int(x)
        self.y = int(y)
        self.id = int(id)

    def in_the_radio(self, x, y):
        if np.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) < 10:
            return True
        return False

    def set_coor(self, x, y):
        self.x = x
        self.y = y

    def get_id(self, x, y):
        if self.in_the_radio(x,y):
            return self.id

    def allowed_positions(self):
        if self.id == 1:
            return [2, 8]
        if self.id == 2:
            return [1, 3, 10]
        if self.id == 3:
            return [2, 4]
        if self.id == 4:
            return [3, 5, 12]
        if self.id == 5:
            return [4, 6]
        if self.id == 6:
            return [5, 7, 14]
        if self.id == 7:
            return [6, 8]
        if self.id == 8:
            return [1, 7, 16]
        if self.id == 9:
            return [10, 16]
        if self.id == 10:
            return [2, 9, 11, 18]
        if self.id == 11:
            return [10, 12]
        if self.id == 12:
            return [4, 11, 13, 20]
        if self.id == 13:
            return [12, 14]
        if self.id == 14:
            return [6, 13, 15, 22]
        if self.id == 15:
            return [14, 16]
        if self.id == 16:
            return [8, 9, 15, 24]
        if self.id == 17:
            return [18, 24]
        if self.id == 18:
            return [10, 17, 19]
        if self.id == 19:
            return [18, 20]
        if self.id == 20:
            return [12, 19, 21]
        if self.id == 21:
            return [20, 22]
        if self.id == 22:
            return [14, 21, 23]
        if self.id == 23:
            return [22, 24]
        if self.id == 24:
            return [16, 17, 23]

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
