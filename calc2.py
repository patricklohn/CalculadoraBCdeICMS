import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculadora de tributos: ")
root.geometry("500x300+550+250")
root.minsize(500, 300)
root.maxsize(600, 800)

def calcBaseCalculo():
    try:
        val1v = value1.get()
        val2v = value2.get()
        
        val1 = float(val1v.replace(',','.'))
        val2 = float(val2v.replace(',','.'))

        if val1 == 0:
            label3 = tk.Label(root, text="Erro: O valor total dos produtos não pode ser zero.")
            label3.pack()
        else:
            result = 100 - ((val2 * 100) / val1)
            label4 = tk.Label(root, text=f'O valor de BC é de {result:.2f}')
            label4.pack()
    except ValueError:
        label3 = tk.Label(root, text="Erro: Entrada inválida. Digite apenas números.")
        label3.pack()


label1 = tk.Label(root, text="Coloque o valor total dos produtos com redução de BC: ")

label1.pack()
value1 = tk.Entry(root)
value1.pack()
label2 = tk.Label(root, text="Coloque o valor da BC do ICMS: ")
label2.pack()
value2 = tk.Entry(root)
value2.pack()

buttonCalcular = tk.Button(root, text="Calcular", command=calcBaseCalculo)
buttonCalcular.pack()

try:
    root.mainloop()
except Exception as e:
    print(f"Ocorreu um erro: {e}")