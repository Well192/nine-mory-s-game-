from tkinter import *
from windMillPlay.sprint_2.production.Data import *

class WindMillPlayGame:
    def __init__(self):
        self.state= "Progreso"

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
                    if object.count >= 2:
                        object.window.bind('<Button-1>', object.seleccionandoFicha)

                object.id = object.canvas.create_image(i.x, i.y, image=object.a)
                object.lista.append([object.id,event.x,event.y])
                object.a.name = object.a.name + "1"
                object.count += 1
