import numpy as np

class Position:
    def __init__(self, x, y, id):
        self.empty = True
        self.x = int(x)
        self.y = int(y)
        self.id = int(id)
        self.ficha = -1

    def in_the_radio(self, x, y):
        if np.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) < 20:
            return True
        return False

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
# Primer Cuadrado
position_list.append(Position(30, 30, 1))
position_list.append(Position(378, 30, 2))
position_list.append(Position(718, 30, 3))
position_list.append(Position(718, 377, 4))
position_list.append(Position(718, 720, 5))
position_list.append(Position(377, 720, 6))
position_list.append(Position(30, 720, 7))
position_list.append(Position(30, 377, 8))

# Segundo Cuadrado
position_list.append(Position(116, 116, 9))
position_list.append(Position(377, 116, 10))
position_list.append(Position(633, 116, 11))
position_list.append(Position(633, 377, 12))
position_list.append(Position(633, 633, 13))
position_list.append(Position(378, 633, 14))
position_list.append(Position(117, 633, 15))
position_list.append(Position(117, 377, 16))

# Tercer cuadrado
position_list.append(Position(218, 218, 17))
position_list.append(Position(377, 218, 18))
position_list.append(Position(530, 218, 19))
position_list.append(Position(530, 377, 20))
position_list.append(Position(530, 530, 21))
position_list.append(Position(377, 530, 22))
position_list.append(Position(218, 530, 23))
position_list.append(Position(218, 377, 24))