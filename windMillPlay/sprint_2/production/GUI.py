from windMillPlay.sprint_2.production.Logic import *
import numpy as np


class WindMillPlay:
    def __init__(self):
        self.window = Tk()
        self.window.title('windMillPlay')
        self.window.geometry("750x750")
        self.canvas = Canvas(self.window, height=750, width=750)
        self.state = True
        self.change = True
        self.count = 0
        self.image_tablero = PhotoImage(file="tablero.png")
        self.tablero = self.canvas.create_image(0, 0, image=self.image_tablero, anchor=NW)
        self.lista = list()
        self.window.bind('<Button-1>', self.start)
        self.canvas.pack(expand=False)
        self.countPar = 0
        self.countImpar = 0

    def start(self, e):
        self.game = WindMillPlayGame()
        self.game.posicionandoFicha(self, e)

    def seleccionandoFicha(self, e):
        if self.change:
            print("==================Turno blanco======================")
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 20) and i[0] % 2 == 0:
                    self.position = i
                    self.window.bind("<Button-1>", self.moviendoFicha)
        else:
            print("=====================Turno negro=========================")
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 20) and i[0] % 2 != 0:
                    self.position = i
                    self.window.bind("<Button-1>", self.moviendoFicha)

    def moviendoFicha(self, e):
        global posi2, posi
        if self.validatePosition(e.x, e.y, self.position[1], self.position[2]):
            for j in position_list:
                if j.in_the_radio(self.position[1], self.position[2]):  # Ubica la posición de la ficha
                    posi = j
                if j.in_the_radio(e.x, e.y):  # Ubica la posición de la nueva posición
                    posi2 = j
            if self.change:
                self.a = PhotoImage(file="piece.png")
                self.change = False
            else:
                self.a = PhotoImage(file="piece2.png")
                self.change = True

            self.id = self.canvas.create_image(posi2.x, posi2.y, image=self.a)
            self.lista.append([self.id, e.x, e.y])
            self.a.name = self.a.name + "1"
            self.canvas.delete(self.position[0])
            self.lista.remove(self.position)
            posi.ficha = -1
            posi2.ficha = self.id
            posi.empty = True
            posi2.empty = False

        else:
            print("Movimiento no válido")

        self.window.bind("<Button-1>", self.seleccionandoFicha)
        if self.game.volada(self.id):
            print("volada")
            self.window.bind("<Button-1>", self.quitada)

    def validatePosition(self, x, y, ficha_x, ficha_y):
        # Recibe las coordenadas dónde se quiere mover y recibe las coordenadas de la ficha que quiere mover
        global posicion_ficha, posicion2
        isValid = False
        isDefined = False
        # Verificar si  el lugar dónde quiero ubicar la ficha es un intersección
        for i in position_list:
            if i.in_the_radio(ficha_x, ficha_y):
                posicion_ficha = i
                isDefined = True
            if i.in_the_radio(x, y) and i.empty:
                posicion2 = i
                isValid = True

        if isDefined == False:
            return isValid

        adyacentes = posicion_ficha.allowed_positions()


        if posicion2 == None:
            isValid = False
            return isValid

        for k in adyacentes:
            if k == posicion2.id and isValid:
                return isValid

        isValid = False
        return isValid

    def quitada(self, e):
        if not self.change:
            print("==================QUITA UNA FICHA NEGRA======================")
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 20) and i[0] % 2 != 0:
                    self.canvas.delete(i[0])
                    self.lista.remove(i)
                    self.canvas.delete(i[0])
                    self.countImpar -= 1

            for i in position_list:
                if (i.in_the_radio(e.x, e.y)):
                    i.empty = True
                    i.ficha = -1
        else:
            print("=====================QUITA UNA FICHA BLANCA=========================")
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 20) and i[0] % 2 == 0:
                    self.canvas.delete(i[0])
                    self.lista.remove(i)
                    self.canvas.delete(i[0])
                    self.countPar -= 1

            for i in position_list:
                if (i.in_the_radio(e.x, e.y)):
                    i.empty = True
                    i.ficha = -1

        if self.count >= 16:
            for i in self.lista:
                if (i[0] % 2 == 0):
                    if (self.countPar < 3):
                        print("Ganó el negro")
                        break
                else:
                    if (self.countImpar < 3):
                        print("Ganó el blanco")
                        break
            self.window.bind("<Button-1>", self.seleccionandoFicha)
        else:
            self.window.bind("<Button-1>", self.start)

    def mainloop(self):
        self.window.mainloop()


milisInstance = WindMillPlay()
milisInstance.mainloop()
