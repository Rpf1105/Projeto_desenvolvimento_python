import tkinter as tk

root = tk.Tk()
root.title("Sistema de notas")
root.padx()
matricula = tk.Entry(root)
matricula.grid(row=0)
nome = tk.Entry(root)
nome.grid(row=1)

registrarnota = tk.Button(root, text="Registrar notas")
closeroot = tk.Button(root, text="Clique aqui para sair", command=root.destroy)


root.mainloop()