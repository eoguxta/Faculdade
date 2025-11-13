import tkinter as tk

def calcular():
    try:
        a = float(altura.get()) / 100
        p = float(peso.get())
        imc = p / (a * a)
        texto = f"IMC: {imc:.2f}"

        if imc < 18.5:
            texto += "\nMagreza"
        elif imc < 25:
            texto += "\nNormal"
        elif imc < 30:
            texto += "\nSobrepeso"
        elif imc < 40:
            texto += "\nObesidade"
        else:
            texto += "\nObesidade Grave"

        resultado["text"] = texto
    except:
        resultado["text"] = "Erro nos valores"

def limpar():
    nome.delete(0, tk.END)
    ender.delete(0, tk.END)
    altura.delete(0, tk.END)
    peso.delete(0, tk.END)
    resultado["text"] = ""

def sair():
    tela.destroy()


tela = tk.Tk()
tela.title("IMC")
tela.geometry("700x400")

frame = tk.Frame(tela)
frame.pack(fill="both", expand=True, padx=10, pady=10)

titulo = tk.Label(frame, text="CÁLCULO DO IMC - ÍNDICE DE MASSA CORPORAL", font=("Arial", 14))
titulo.place(x=10, y=10)

tk.Label(frame, text="NOME DO PACIENTE:").place(x=10, y=50)
nome = tk.Entry(frame, width=35)
nome.place(x=150, y=50)

tk.Label(frame, text="ENDEREÇO COMPLETO:").place(x=10, y=90)
ender = tk.Entry(frame, width=35)
ender.place(x=150, y=90)

tk.Label(frame, text="ALTURA (CM)").place(x=10, y=130)
altura = tk.Entry(frame, width=35)
altura.place(x=150, y=130)

tk.Label(frame, text="PESO (KG)").place(x=10, y=170)
peso = tk.Entry(frame, width=35)
peso.place(x=150, y=170)

resultado = tk.Label(frame, text="RESULTADO", bd=1, relief="solid", width=30, height=10)
resultado.place(x=440, y=130)

tk.Button(frame, text="Calcular", width=15, command=calcular).place(x=50, y=325)
tk.Button(frame, text="Reiniciar", width=15, command=limpar).place(x=285, y=325)
tk.Button(frame, text="Sair", width=15, command=sair).place(x=510, y=325)

tela.mainloop()
