from tkinter import *
from tkinter import StringVar



root = Tk()

root.title("Calculadora")

root.iconbitmap("Calculator_30001.ico")


def btn(num):
    global operador
    operador = operador + str(num)
    entrada.set(operador)


def resultado():
    global operador
    try:
        opera = str(eval(operador))
        entrada.set(opera)
    except:
        entrada.set("Error")
    operador = ""

def clear():
    global operador
    operador=("")
    entrada.set("0")

entrada = StringVar()
operador = ""

screen = Entry(root, borderwidth=3, font=('Arial', 20, "bold"), bd=4, bg="snow", justify="right", textvariable=entrada)
screen.grid(row=0, columnspan=6)

Button(root, text="1", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(1)).grid(
    row=1, column=0)
Button(root, text="2", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(2)).grid(
    row=1, column=1)
Button(root, text="3", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(3)).grid(
    row=1, column=2)

Button(root, text="4", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(4)).grid(
    row=2, column=0)
Button(root, text="5", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(5)).grid(
    row=2, column=1)
Button(root, text="6", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(6)).grid(
    row=2, column=2)

Button(root, text="7", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(7)).grid(
    row=3, column=0)
Button(root, text="8", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(8)).grid(
    row=3, column=1)
Button(root, text="9", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(9)).grid(
    row=3, column=2)

Button(root, text="^", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn()).grid(
    row=1, column=3)
Button(root, text="AC", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: clear()).grid(
    row=1, column=4)

Button(root, text="+", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("+")).grid(
    row=2, column=3)
Button(root, text="-", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("-")).grid(
    row=2, column=4)

Button(root, text="x", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("x")).grid(
    row=3, column=3)
Button(root, text="/", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("/")).grid(
    row=3, column=4)

Button(root, text="(", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("(")).grid(
    row=4, column=3)
Button(root, text=")", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn(")")).grid(
    row=4, column=4)

Button(root, text="=", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11),
       command=lambda: resultado()).grid(row=4, column=2)
Button(root, text="%", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn("%")).grid(
    row=4, column=1)
Button(root, text="←", width=5, height=2, bg="gray11", fg="white", font=('Arial', 11), command=lambda: btn).grid(row=4,
                                                                                                                 column=0)
root.mainloop()
