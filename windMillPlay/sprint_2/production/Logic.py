from tkinter import *
from windMillPlay.sprint_2.production.Data import *


class WindMillPlayGame:
    def __init__(self):
        self.state = "Progreso"

    def posicionandoFicha(self, object, event):
        for i in position_list:
            if i.in_the_radio(event.x, event.y) and i.empty:
                i.empty = False
                if object.change:
                    object.a = PhotoImage(file="piece.png")
                    object.change = False
                else:
                    object.a = PhotoImage(file="piece2.png")
                    object.change = True
                    if object.count >= 4:
                        object.window.bind('<Button-1>', object.seleccionandoFicha)
                object.id = object.canvas.create_image(i.x, i.y, image=object.a)
                i.ficha = object.id
                object.lista.append([object.id, event.x, event.y])
                object.a.name = object.a.name + "1"
                object.count += 1
                self.volada()

    def volada(self):

        for i in position_list:
            if not i.empty:
                if i.id % 2 == 1:
                    if i.id == 1 or i.id == 9 or i.id == 17:
                        if position_list[i.id + 6].ficha % 2 == 0 and position_list[i.id + 5].ficha % 2 == 0:
                            print("volada 1")
                        if position_list[i.id + 6].ficha % 2 == 1 and position_list[i.id + 6].ficha != -1 and position_list[i.id + 5].ficha % 2 == 1 and position_list[i.id + 5].ficha != -1:
                            print("volada 2")
                    else:
                        if position_list[i.id-2].ficha % 2 == 0 and position_list[i.id-3].ficha % 2 == 0:
                            print("volada 3" )
                        if position_list[i.id-2].ficha % 2 == 1 and position_list[i.id-2].ficha != -1 and  position_list[i.id-3].ficha % 2 == 1 and position_list[i.id-3].ficha != -1 :
                            print("volada 4")
                if i.id % 2 == 0:
                    if i.id == 2 or i.id == 4 or i.id == 6 or i.id == 8:
                        if position_list[i.id + 7].ficha % 2 == 0 and position_list[i.id + 15].ficha % 2 == 0:
                            print("volada 5")
                        if position_list[i.id + 7].ficha % 2 == 1 and position_list[i.id + 7].ficha != -1 and position_list[i.id + 15].ficha % 2 == 1 and position_list[i.id + 15].ficha != -1:
                            print("volada 6")










