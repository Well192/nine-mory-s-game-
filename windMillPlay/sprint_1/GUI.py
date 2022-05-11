from tkinter import *
from Data import *
from Logic import *

class WindMillPlay:
    def __init__(self):
        self.window = Tk()
        self.window.title('windMillPlay')
        self.window.geometry("400x400")
        self.canvas = Canvas(self.window)
        self.change = True
        self.count = 0  # contador de fichas

        # primer cuadrado
        self.canvas.create_line(30, 20, 350, 20, fill='#332', width=3)
        self.canvas.create_line(348, 20, 350, 200000, fill='#332', width=3)
        self.canvas.create_line(30, 265, 350, 265, fill='#332', width=3)
        self.canvas.create_line(30, 20, 350, 200000, fill='#332', width=3)

        # segundo cuadrado
        self.canvas.create_line(60, 50, 315, 50, fill='#332', width=3)
        self.canvas.create_line(313, 50, 313, 235, fill='#332', width=3)
        self.canvas.create_line(60, 235, 315, 235, fill='#332', width=3)
        self.canvas.create_line(60, 50, 60, 235, fill='#332', width=3)

        # tercer cuadrado
        self.canvas.create_line(100, 80, 275, 80, fill='#332', width=3)
        self.canvas.create_line(273, 80, 273, 200, fill='#332', width=3)
        self.canvas.create_line(100, 200, 275, 200, fill='#332', width=3)
        self.canvas.create_line(100, 80, 100, 200, fill='#332', width=3)

        # linea horizontal 1
        self.canvas.create_line(30, 142.5, 100, 142.5, fill='#332', width=3)

        # linea horizontal 2
        self.canvas.create_line(348, 142.5, 274.5, 142.5, fill='#332', width=3)

        # linea vertical  1
        self.canvas.create_line(189, 20, 189, 79, fill='#332', width=3)

        # linea vertical 2
        self.canvas.create_line(189, 265, 189, 200, fill='#332', width=3)
        self.canvas.grid(column=0, row=0, sticky="N, W, E, S")

        self.lista = list()

        self.window.bind('<Button-1>', self.start)

    def moviendoFicha(self, e):
        if self.change:
            print(e.x, e.y)
            #print("soy el blanco")
        else:
            print(e.x, e.y)

    def start(self,e):
        posicionandoFicha(self,e)


    def mainloop(self):
        self.window.mainloop()

milisInstance = WindMillPlay()
milisInstance.mainloop()