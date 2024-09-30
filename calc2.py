import tkinter as tk
from tkinter import ttk

def opcoesCalculo():
    limpar_tela()

    buttonDescobrirReducao = ttk.Button(root, text="Descobrir base de cálculo", command=descobrirReducao)
    buttonDescobrirReducao.pack(pady=10)

    buttonCalcReducao = ttk.Button(root, text="Calcular ICMS", command=calcReducao)
    buttonCalcReducao.pack(pady=10)

def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()

def calcReducao():
    limpar_tela()
    label1 = ttk.Label(root, text="Coloque o valor total das notas:")
    label1.pack(pady=5)
    
    value1 = ttk.Entry(root)
    value1.pack(pady=5)
    
    label2 = ttk.Label(root, text="Coloque a redução da base de cálculo (%)")
    label2.pack(pady=5)
    
    value2 = ttk.Entry(root)
    value2.pack(pady=5)
    
    buttonCalcular = ttk.Button(root, text="Calcular", command=lambda: calcBaseCalculo(value1, value2))
    buttonCalcular.pack(pady=10)

def calcBaseCalculo(value1, value2):
    try:
        val1 = float(value1.get().replace(',', '.'))
        val2 = float(value2.get().replace(',', '.'))

        if val1 == 0:
            raise ValueError("O valor total não pode ser zero")
        else:
            result = val1 - val1 * (val2 / 100)
            resultImposto = result * (12 / 100)

            label3 = ttk.Label(root, text=f'A base de cálculo seria R${result:.2f} e o ICMS R${resultImposto:.2f}')
            label3.pack(pady=10)
    except ValueError as e:
        label3 = ttk.Label(root, text=f"Erro: {str(e)}")
        label3.pack(pady=10)

    buttonLimpar = ttk.Button(root, text="Limpar", command=opcoesCalculo)
    buttonLimpar.pack(pady=10)

def descobrirReducao():
    limpar_tela()
    
    label1 = ttk.Label(root, text="Coloque o valor total dos produtos:")
    label1.pack(pady=5)
    
    value1 = ttk.Entry(root)
    value1.pack(pady=5)
    
    label2 = ttk.Label(root, text="Coloque o valor da base de cálculo com a redução aplicada")
    label2.pack(pady=5)
    
    value2 = ttk.Entry(root)
    value2.pack(pady=5)
    
    buttonCalcular = ttk.Button(root, text="Calcular", command=lambda: calcularReducao(value1, value2))
    buttonCalcular.pack(pady=10)

def calcularReducao(value1, value2):
    try:
        val1 = float(value1.get().replace(',', '.'))
        val2 = float(value2.get().replace(',', '.'))

        if val1 == 0:
            raise ValueError("O valor total não pode ser zero")
        else:
            result = 100 - ((val2 * 100) / val1)
            label3 = ttk.Label(root, text=f'O percentual da redução é de: {result:.2f}%')
            label3.pack(pady=10)
    except ValueError as e:
        label3 = ttk.Label(root, text=f"Erro: {str(e)}")
        label3.pack(pady=10)

    buttonLimpar = ttk.Button(root, text="Limpar", command=opcoesCalculo)
    buttonLimpar.pack(pady=10)

def adicionar_scrollbar():
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

root = tk.Tk()
root.title("Calculadora Contábil")
root.geometry("500x400+550+250")
root.minsize(500, 400)
root.maxsize(600, 800)

opcoesCalculo()

adicionar_scrollbar()

try:
    root.mainloop()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
