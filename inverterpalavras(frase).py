def inverter_palavras(frase):
    return ' '.join(p[::-1] for p in frase.split())

texto = input("Digite uma frase: ")
print(inverter_palavras(texto))