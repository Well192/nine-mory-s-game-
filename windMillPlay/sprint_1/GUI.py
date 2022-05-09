from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Nine men's morris")

canvas = Canvas(root)

# primer cuadrado
canvas.create_line(30,20, 350, 20, fill='#332',width=3)
canvas.create_line(348, 20, 350,200000, fill='#332', width=3)
canvas.create_line(30,265, 350, 265, fill='#332',width=3)
canvas.create_line(30, 20, 350,200000, fill='#332', width=3)

# segundo cuadrado
canvas.create_line(60,50, 315, 50, fill='#332',width=3)
canvas.create_line(313, 50,  313,235, fill='#332', width=3)
canvas.create_line(60,235, 315, 235, fill='#332',width=3)
canvas.create_line(60, 50, 60,235, fill='#332', width=3)
#tercer cuadrado
canvas.create_line(100,80, 275, 80, fill='#332',width=3)
canvas.create_line(273, 80,  273,200, fill='#332', width=3)
canvas.create_line(100,200, 275, 200, fill='#332',width=3)
canvas.create_line(100, 80, 100,200, fill='#332', width=3)

#linea horizontal 1
canvas.create_line(30,142.5, 100, 142.5, fill='#332',width=3)
#linea horizontal 2
canvas.create_line(348,142.5, 274.5, 142.5, fill='#332',width=3)
#linea vertical  1
canvas.create_line(189, 20, 189,79, fill='#332', width=3)

#linea vertical 2
canvas.create_line(189, 265, 189,200, fill='#332', width=3)
#canvas.itemconfigure(id, fill='red', width=2)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
root.geometry("400x400")

img= ImageTk.PhotoImage(Image.open("piece.png"))
my_img = canvas.create_image(220,100,image=img)
img2= ImageTk.PhotoImage(Image.open("piece2.png"))
my_img2 = canvas.create_image(220,100,image=img)
canvas.create_image(345,140,anchor=NW,image=img)
canvas.create_image(345,140,anchor=NW,image=img2)

def move(e):
    global img
    img= ImageTk.PhotoImage(Image.open("piece.png"))
    my_img = canvas.create_image(e.x,e.y,image=img)
    img2= ImageTk.PhotoImage(Image.open("piece2.png"))
    my_img2 = canvas.create_image(e.x,e.y,image=img2)

    #canvas.create_image(342,15,anchor=NW,image=img)
    #canvas.create_image(95,195,anchor=NW,image=img)

canvas.bind('<B1-Motion>',move)
root.mainloop()