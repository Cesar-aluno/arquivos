from tkinter import *
import tkinter as tk

aplicativo = tk.Tk()
aplicativo.title('Página de Menu!')
aplicativo.geometry("480x500")
aplicativo.configure(background='#ddf')


Label(aplicativo, text='label', background='#dfc', foreground='#007').place(width=110, height=25, x=20, y=15, anchor='w')
barra = Entry(aplicativo)
barra.place(width=105, height=30, x=20, y=45)

Label(aplicativo, text='label', background='#ddc', foreground='#007').place(width=110, height=25, x=20, y=15, anchor='w')
barra = Entry(aplicativo)
barra.place(width=105, height=30, x=20, y=45)


aplicativo.mainloop()
