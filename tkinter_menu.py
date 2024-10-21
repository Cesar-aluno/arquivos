from tkinter import *
import tkinter as tk

def vazio():
    print('')

aplicativo = tk.Tk()
aplicativo.title('Página de Menu!')
aplicativo.geometry("480x500")
aplicativo.configure(background='#ddf')

barraMenu = Menu(aplicativo)


menuComandos = Menu(barraMenu)
menuComandos.add_command(label='Novo', command=vazio)
menuComandos.add_command(label='Buscar', command=vazio)
menuComandos.add_command(label='Excluir', command=vazio)
menuComandos.add_separator()
menuComandos.add_command(label='Sair', command=aplicativo.quit)
barraMenu.add_cascade(label='Comandos', menu=menuComandos)

menuManutencao= Menu(aplicativo)
menuManutencao.add_command(label= 'Registro', command=vazio)
menuManutencao.add_cascade(label= 'Manutenção', menu= menuManutencao)
aplicativo.config(menu=barraMenu)
aplicativo.mainloop()
