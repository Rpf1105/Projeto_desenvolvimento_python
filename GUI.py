import tkinter as tk
from tkinter import font
from tkinter import ttk


class myApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("banco")
        container = tk.Frame(self)
        title = tk.Label(text="Banco de dados magico", font=tk.font.Font(family="Arial", weight="bold"))
        title.pack(side="top")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for f in (mainMenu, mainAluno, pageDisciplinas, pageInscricao):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showpage("mainMenu")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class mainMenu(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual informação você deseja ver")
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Alunos", command=lambda: control.showpage("mainAluno"))
        button1.pack(pady=10)
        button2 = tk.Button(self, text="Disciplinas", command=lambda: control.showpage("pageDisciplinas"))
        button2.pack(pady=10)
        button3 = tk.Button(self, text="Inscrições", command=lambda: control.showpage("pageInscricao"))
        button3.pack(pady=10)

#aluno
class mainAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        option = tk.StringVar(value="Inserir")
        insert = ["Inserir", "Alterar", "Deletar"]
        select = tk.OptionMenu(self, option, *insert)
        select.pack(side="top")
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()
        label = tk.Label(self, textvariable=option)
        label.pack(side="top", fill="x", pady=10)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for f in (insertAluno,):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showpage("insertAluno")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class insertAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        nome=tk.Entry()
        submit = tk.Button()
        nome.grid(row=0, column=0, sticky="n    ")
        submit.grid(row=1, column=0, sticky="n")

#disciplinas
class pageDisciplinas(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label = tk.Label(self, text="disciplinas")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()

class pageInscricao(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label = tk.Label(self, text="inscricao")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()

def init():
    app = myApp()
    app.mainloop()

init()

