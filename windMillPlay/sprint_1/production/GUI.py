from windMillPlay.sprint_1.production.Logic import *
import numpy as np


class WindMillPlay:
    def __init__(self):
        self.window = Tk()
        self.window.title('windMillPlay')
        self.window.geometry("400x400")
        self.canvas = Canvas(self.window)
        self.state = True
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
        self.deli = 0
        self.window.bind('<Button-1>', self.start)

    def start(self,e):
        game = WindMillPlayGame()
        game.posicionandoFicha(self,e)

    def moviendoFicha(self, e):
        if self.change:
            for i in self.lista:
                if (np.sqrt((i[1]-e.x)**2 + (i[2]-e.y)**2) < 4) and (i[0]%2!=0):
                    self.position = i
                    self.window.bind("<Button-1>",self.eliminando)
                    self.change = False
        else:
            self.change = True

    def eliminando(self,e):
        if self.validatePosition(e.x, e.y, self.position[1], self.position[2]):
            self.a = PhotoImage(file="piece.png")
            self.id = self.canvas.create_image(e.x, e.y, image=self.a)
            self.lista.append([self.id, e.x, e.y])
            self.change = False
            self.a.name = self.a.name + "1"
            self.count += 1

            self.canvas.delete(self.position[0])
        else:
            print("Movimiento inválido, seleccione otra posición")

    def validatePosition(self, x, y, ficha_x, ficha_y):
        flag = False
        pos = Position(0,0)
        for i in position_list:
            if i.in_the_radio(x,y) and i.empty == True:
                flag = True
                print("Hola")
                break
        if(np.sqrt((ficha_x-i.x)**2) < 4 or np.sqrt((ficha_y-i.y)**2) < 4) and flag:
            print("Chau")
            return True
        return False

    def mainloop(self):
        self.window.mainloop()


milisInstance = WindMillPlay()
milisInstance.mainloop()