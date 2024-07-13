import tkinter
from tkinter import *

main = Tk()
main.title("Calculator")
main.geometry('570x600+100+200')
main.resizable(False,False)
main.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    res.config(text=equation)

def clear():
    global equation
    equation = ""
    res.config(text=equation)

def clear_entry():
    global equation
    equation = equation[:-1]
    res.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation = ""
    res.config(text=result)

res= Label(main,width=25,height=2,text="",font=("arial",30))
res.pack()

Button(main,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#808080",command=lambda: clear()).place(x=10,y=100)
Button(main,text="CE", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#808080",command=lambda: clear_entry()).place(x=150,y=100)
Button(main,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#FFA500",command=lambda: show("/")).place(x=290,y=100)
Button(main,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#FFA500",command=lambda: show("*")).place(x=430,y=100)

Button(main,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
Button(main,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(main,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
Button(main,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#FFA500",command=lambda: show("-")).place(x=430,y=200)

Button(main,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
Button(main,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(main,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(main,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#FFA500",command=lambda: show("+")).place(x=430,y=300)

Button(main,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
Button(main,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(main,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(main,text="0", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)

Button(main,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#808080",command=lambda: show("%")).place(x=150,y=500)
Button(main,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#808080",command=lambda: show(".")).place(x=290,y=500)
Button(main,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#FF0000",command=lambda: calculate()).place(x=430,y=400)

main.mainloop()
