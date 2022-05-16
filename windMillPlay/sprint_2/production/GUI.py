from windMillPlay.sprint_2.production.Logic import *
import numpy as np

class WindMillPlay:
    def __init__(self):
        self.window = Tk()
        self.window.title('windMillPlay')
        self.window.geometry("850x850")
        self.canvas = Canvas(self.window, height=750, width=750)
        self.state = True
        self.change = True
        self.count = 0
        self.image_tablero = PhotoImage(file='tablero.png')
        self.tablero = self.canvas.create_image(0, 0, image=self.image_tablero, anchor=NW)
        self.canvas.pack(expand=False)
        self.lista = list()
        self.window.bind('<Button-1>', self.start)

    def start(self, e):
        game = WindMillPlayGame()
        game.posicionandoFicha(self, e)

    def seleccionandoFicha(self, e):
        if self.change:
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 10) and i[0]%2 ==0:
                    self.position = i
                    self.window.bind("<Button-1>", self.moviendoFicha)
                else:
                    print("Elige una ficha amarilla")
            print("==================Turno blanco======================")
        else:
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 10) and i[0]%2 != 0:
                    self.position = i
                    self.window.bind("<Button-1>", self.moviendoFicha)
                else:
                    print("Elige una ficha negra")
            print("=====================Turno negro=========================")

    def moviendoFicha(self, e):
        global posi2, posi
        if self.validatePosition(e.x, e.y, self.position[1], self.position[2]):
            for j in position_list:
                if j.in_the_radio(self.position[1], self.position[2]): #Ubica la posición de la ficha
                    posi = j
                if j.in_the_radio(e.x,e.y): #Ubica la posición de la nueva posición
                    posi2 = j

            if self.change:
                self.a = PhotoImage(file="piece.png")
                self.change= False
            else:
                self.a = PhotoImage(file="piece2.png")
                self.change= True

            self.id = self.canvas.create_image(posi2.x, posi2.y, image=self.a)
            self.lista.append([self.id, e.x, e.y])
            self.a.name = self.a.name + "1"
            self.canvas.delete(self.position[0])
            self.lista.remove(self.position)

            posi.empty = True
            posi2.empty = False

        else:
            print("Movimiento no válido")

        self.window.bind("<Button-1>", self.seleccionandoFicha)
    def validatePosition(self, x, y, ficha_x, ficha_y):
        #Recibe las coordenadas dónde se quiere mover y recibe las coordenadas de la ficha que quiere mover
        global posicion_ficha, posicion2
        isValid = False
        #Verificar si  el lugar dónde quiero ubicar la ficha es un intersección
        for i in position_list:
            if i.in_the_radio(ficha_x, ficha_y):
                posicion_ficha = i
            if i.in_the_radio(x, y) and i.empty:
                posicion2 = i
                isValid = True

        adyacentes = posicion_ficha.allowed_positions()

        for k in adyacentes:
            if k == posicion2.indicator and isValid:
                return isValid

        isValid = False
        return isValid

    def mainloop(self):
        self.window.mainloop()

milisInstance = WindMillPlay()
milisInstance.mainloop()