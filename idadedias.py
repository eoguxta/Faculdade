idade_dias = int(input("Digite sua idade em dias: "))

anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30

print("Sua idade é:" ,anos, "anos" ,meses, "meses" ,dias, "dias")