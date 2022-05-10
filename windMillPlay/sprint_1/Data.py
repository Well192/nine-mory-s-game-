from tkinter import *

class Ficha:
    def __init__(self, tipo):
        self.image_path = "vacio.png"
        if int(tipo) == 1:
            self.image_path = "piece.png"
        elif int(tipo) == 2:
            self.image_path = "piece2.png"

ficha_list=list()
ficha_list.append(Ficha(1))
ficha_list.append(Ficha(2))
ficha_list.append(Ficha(0))

class Position:
    def __init__(self, x, y, ficha):
        self.x = int(x)
        self.y = int(y)
        self.ficha = ficha

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

position_list=list()
position_list.append(Position(30, 20, Ficha(0)))
position_list.append(Position(190, 20, Ficha(0)))
position_list.append(Position(350, 20, Ficha(0)))
position_list.append(Position(350, 145, Ficha(0)))
position_list.append(Position(350, 265, Ficha(0)))
position_list.append(Position(190, 265, Ficha(0)))
position_list.append(Position(30, 265, Ficha(0)))
position_list.append(Position(30, 140,Ficha(0)))
position_list.append(Position(60, 50, Ficha(0)))
position_list.append(Position(315, 50, Ficha(0)))
position_list.append(Position(315, 145, Ficha(0)))
position_list.append(Position(315, 235, Ficha(0)))
position_list.append(Position(190, 235, Ficha(0)))
position_list.append(Position(60, 235, Ficha(0)))
position_list.append(Position(60, 145, Ficha(0)))
position_list.append(Position(100, 80, Ficha(0)))
position_list.append(Position(190, 80, Ficha(0)))
position_list.append(Position(275, 80, Ficha(0)))
position_list.append(Position(275, 145, Ficha(0)))
position_list.append(Position(275, 200, Ficha(0)))
position_list.append(Position(190, 200, Ficha(0)))
position_list.append(Position(100, 200, Ficha(0)))
position_list.append(Position(100, 145, Ficha(0)))

