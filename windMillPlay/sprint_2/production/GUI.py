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
        self.count = 0  # contador de fichas
        self.image_tablero = PhotoImage(file='tablero.png')
        self.tablero = self.canvas.create_image(0, 0, image=self.image_tablero, anchor=NW)
        self.canvas.pack(expand=False)
        self.lista = list()
        self.deli = 0
        self.window.bind('<Button-1>', self.start)

    def start(self, e):
        game = WindMillPlayGame()
        #print(e.x, " ", e.y)
        game.posicionandoFicha(self, e)

    def moviendoFicha(self, e):
        #print(self.lista)
        if self.change:
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 10):
                    self.position = i
                    self.window.bind("<Button-1>", self.eliminando)
                    #self.change = False
                else:
                    print("Elige una ficha válida")
            print("Turno blanco")
        else:
            for i in self.lista:
                if (np.sqrt((i[1] - e.x) ** 2 + (i[2] - e.y) ** 2) < 10):
                    self.position = i
                    self.window.bind("<Button-1>", self.eliminando)
                    #self.change = True
                else:
                    print("Elige una ficha válida")
            print("Turno negro")

    def eliminando(self, e):
        if self.validatePosition(e.x, e.y, self.position[1], self.position[2]):
            if self.change:
                self.a = PhotoImage(file="piece.png")
                self.change= False
                self.id = self.canvas.create_image(e.x, e.y, image=self.a)
                self.lista.append([self.id, e.x, e.y])
                self.a.name = self.a.name + "1"
                self.count += 1
                self.canvas.delete(self.position[0])
                self.lista.remove(self.position)
            else:
                self.a = PhotoImage(file="piece2.png")
                self.change= True
                self.id = self.canvas.create_image(e.x, e.y, image=self.a)
                self.lista.append([self.id, e.x, e.y])
                self.a.name = self.a.name + "1"
                self.count += 1
                self.canvas.delete(self.position[0])
                self.lista.remove(self.position)

            #print(self.change)
            self.window.bind("<Button-1>", self.moviendoFicha)
        else:
            print("Movimiento no válido")

    def validatePosition(self, x, y, ficha_x, ficha_y): #Recibe las coordenadas dónde se quiere mover y recibe las coordenadas de la ficha que quiere mover
        isValid = False
        #Verificar si  el lugar dónde quiero ubicar la ficha es un vértice
        for i in position_list:
            if i.in_the_radio(x, y) and i.empty == True:
                isValid = True
                break
        for j in position_list:
            if j.in_the_radio(ficha_x, ficha_y):
                isValid = True
                break
        adyacentes = j.allowed_positions()
        if isValid:
            for k in adyacentes:
                if i.indicator == k:
                    return isValid

        #if (np.sqrt(np.abs((ficha_x - i.x + ficha_y - i.y))) < 10) and isValid:
        #    return isValid
        isValid = False
        return isValid

    def mainloop(self):
        self.window.mainloop()


milisInstance = WindMillPlay()
milisInstance.mainloop()
