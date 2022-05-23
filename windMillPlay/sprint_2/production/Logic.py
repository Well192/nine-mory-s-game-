from tkinter import *
from windMillPlay.sprint_2.production.Data import *


class WindMillPlayGame:
    def __init__(self):
        self.state = "Progreso"
        self.voladas = list()

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
                    if object.count >= 7:
                        object.window.bind('<Button-1>', object.seleccionandoFicha)
                object.id = object.canvas.create_image(i.x, i.y, image=object.a)
                i.ficha = object.id

                object.lista.append([object.id, event.x, event.y])
                object.a.name = object.a.name + "1"
                object.count += 1

                flagito = self.volada(i.ficha)
                if flagito:
                    object.window.bind('<Button-1>', object.quitada)


    def volada(self,flag):
        for i in position_list:
            if not i.empty:
                if i.id % 2 == 1:
                    if i.id == 1 or i.id == 9 or i.id == 17:
                        if position_list[i.id + 6].ficha % 2 == 0 and position_list[i.id + 5].ficha % 2 == 0 and position_list[i.id-1].ficha % 2 == 0 and \
                                (position_list[i.id + 6].ficha == flag or position_list[i.id + 5].ficha == flag or position_list[i.id-1].ficha == flag):
                            return True
                        if position_list[i.id + 6].ficha % 2 == 1 and position_list[i.id + 6].ficha != -1 and position_list[i.id-1].ficha % 2 == 1 and position_list[i.id + 5].ficha % 2 == 1 and position_list[i.id + 5].ficha != -1 and \
                                (position_list[i.id + 6].ficha == flag or position_list[i.id + 5].ficha == flag or position_list[i.id-1].ficha == flag):
                            return True
                    else:
                        if position_list[i.id-2].ficha % 2 == 0 and position_list[i.id-3].ficha % 2 == 0 and position_list[i.id-1].ficha % 2 == 0 and \
                                (position_list[i.id -1].ficha == flag or position_list[i.id-2].ficha == flag or position_list[i.id-3].ficha == flag):
                            return True
                        if position_list[i.id-2].ficha % 2 == 1 and position_list[i.id-2].ficha != -1 and position_list[i.id-3].ficha % 2 == 1 and position_list[i.id-1].ficha % 2 == 1 and position_list[i.id-3].ficha != -1 and \
                                (position_list[i.id -1].ficha == flag or position_list[i.id-2].ficha == flag or position_list[i.id-3].ficha == flag):
                            return True

                if i.id % 2 == 0:
                    if i.id == 2 or i.id == 4 or i.id == 6 or i.id == 8:
                        if position_list[i.id + 7].ficha % 2 == 0 and position_list[i.id + 15].ficha % 2 == 0 and position_list[i.id-1].ficha % 2 == 0 and \
                                (position_list[i.id + 7].ficha == flag or position_list[i.id + 15].ficha == flag or position_list[i.id-1].ficha == flag):
                            return True
                        if position_list[i.id + 7].ficha % 2 == 1 and position_list[i.id + 7].ficha != -1 and position_list[i.id-1].ficha % 2 == 1 and position_list[i.id + 15].ficha % 2 == 1 and position_list[i.id + 15].ficha != -1 and \
                                (position_list[i.id + 7].ficha == flag or position_list[i.id + 15].ficha == flag or position_list[i.id-1].ficha == flag):
                            return True
        return False










