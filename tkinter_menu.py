from tkinter import *
import tkinter as tk

def vazio():
    print('')

aplicativo = tk.Tk()
aplicativo.title('Página de Menu!')
aplicativo.geometry("480x500")
aplicativo.configure(background='#ddf')

barraMenu = Menu(aplicativo)

menuComandos = Menu(barraMenu, tearoff= 0)
menuComandos.add_command(label='Novo', command=vazio)
menuComandos.add_command(label='Buscar', command=vazio)
menuComandos.add_command(label='Excluir', command=vazio)
menuComandos.add_separator()
menuComandos.add_command(label='Sair', command=aplicativo.quit)
barraMenu.add_cascade(label='Comandos', menu=menuComandos)

menuManutencao= Menu(aplicativo, tearoff= 0)
menuManutencao.add_command(label= 'Registro', command=vazio)
barraMenu.add_cascade(label= 'Manutenção', menu= menuManutencao)

menuRelacionado= Menu(barraMenu, tearoff= 0)
menuRelacionado.add_command(label= 'Arquivos', command= vazio)
barraMenu.add_cascade(label= 'Relacionado', menu= menuRelacionado)

aplicativo.config(menu=barraMenu)
aplicativo.mainloop()
