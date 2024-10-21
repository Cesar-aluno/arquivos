from tkinter import *
import tkinter as tk
from tkinter import messagebox

def vazio():
    print('')

def programador():
    
    janelaProgramador = Toplevel()
    janelaProgramador.title("Dados do Programador")
    janelaProgramador.geometry("300x200")
    janelaProgramador.configure(background='#ddf')


    label_nome = Label(janelaProgramador, text="Nome: ", font=("Arial", 12), bg='#ddf')
    label_nome.pack(pady=10)

    label_idade = Label(janelaProgramador, text="Idade: ", font=("Arial", 12), bg='#ddf')
    label_idade.pack(pady=10)

    label_info = Label(janelaProgramador, text="By Cesar Menezes!", font=("Arial", 9), bg='#ddf').pack(side= tk.RIGHT)
    label_info.pack(pady=10)


    fechar_botao = Button(janelaProgramador, text="Fechar", command=janelaProgramador.destroy)
    fechar_botao.pack(pady=20)

aplicativo = tk.Tk()
aplicativo.title('Página de Menu!')
aplicativo.geometry("480x500")
aplicativo.configure(background='#ddf')

barraMenu = Menu(aplicativo)

menuComandos = Menu(barraMenu, tearoff=0)
menuComandos.add_command(label='Novo', command=vazio)
menuComandos.add_command(label='Buscar', command=vazio)
menuComandos.add_command(label='Excluir', command=vazio)
menuComandos.add_separator()
menuComandos.add_command(label='Fechar', command=aplicativo.quit)
barraMenu.add_cascade(label='Comandos', menu=menuComandos)

menuManutencao = Menu(aplicativo, tearoff=0)
menuManutencao.add_command(label='Registro', command=vazio)
barraMenu.add_cascade(label='Manutenção', menu=menuManutencao)

menuRelacionado = Menu(barraMenu, tearoff=0)
menuRelacionado.add_command(label='Arquivos', command=vazio)
barraMenu.add_cascade(label='Relacionado', menu=menuRelacionado)

menuRelatorios = Menu(barraMenu, tearoff=0)
menuRelatorios.add_command(label='Relatório 1', command=vazio)
menuRelatorios.add_command(label='Relatório 2', command=vazio)
menuRelatorios.add_command(label='Relatório 3', command=vazio)
barraMenu.add_cascade(label='Relatórios', menu=menuRelatorios)

menuInformacoes = Menu(barraMenu, tearoff=0)
menuInformacoes.add_command(label='Programa', command=vazio)
menuInformacoes.add_command(label='Programador', command=programador)
menuInformacoes.add_command(label='Sair', command=aplicativo.quit)
barraMenu.add_cascade(label='Informações', menu=menuInformacoes)

aplicativo.config(menu=barraMenu)
aplicativo.mainloop()
