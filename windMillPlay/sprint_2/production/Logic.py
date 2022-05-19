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
                self.volada(i.get_id(i.x, i.y), object)

    def volada(self, id_pos, object):
        print("id: ", id_pos)
        print(position_list[id_pos-1].ficha)

        if id_pos % 2 == 1:
            if id_pos == 1 or id_pos == 9 or id_pos == 17:
                if position_list[id_pos + 6].ficha % 2 == 0 and position_list[id_pos + 5].ficha % 2 == 0:
                    print("volada")
            else:
                if position_list[id_pos-2].ficha % 2 == 0 and position_list[id_pos-3].ficha % 2 == 0:
                    print("volada")








