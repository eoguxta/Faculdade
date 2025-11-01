import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    print("\nOs valores formam um triângulo!")
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"A área do triângulo é: {area:.2f}")
else:
    print("\nOs valores NÃO formam um triângulo.")
    print(f"Valores informados: a = {a}, b = {b}, c = {c}")