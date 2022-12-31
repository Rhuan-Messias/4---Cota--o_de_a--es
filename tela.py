import tkinter as tk
from tkinter import ttk
from busca_preços import * 


screen = tk.Tk()
screen.title('Preço Dos Meus Fundos Imobiliários')
screen.geometry('1280x800')
texto_1 = tk.Label(screen,text='INTERFACE GRÁFICA PARA USUÁRIOS')
texto_1.grid(column=0,row=0,padx=10,pady=10)
button_1 = tk.Button(screen,text='Clique para ver o gráfico de Barras',command=valores_fii)
button_1.grid(column=0,row=1,padx=10,pady=10)

retorno_interesses_0 = tk.Label(screen,text=' ')
retorno_interesses_0.grid(column=0,row=2,padx=5,pady=5)
retorno_interesses_1 = tk.Label(screen,text=' ')
retorno_interesses_1.grid(column=1,row=2,padx=5,pady=5)
retorno_interesses_2 = tk.Label(screen,text=' ')
retorno_interesses_2.grid(column=2,row=2,padx=5,pady=5)
retorno_interesses_3 = tk.Label(screen,text=' ')
retorno_interesses_3.grid(column=3,row=2,padx=5,pady=5)

screen.mainloop()