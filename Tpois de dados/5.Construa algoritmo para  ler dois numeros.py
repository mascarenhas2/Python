import os

os.system("cls || clear")

num1 : int
num2 : int
soma : int
multiplicacao : int
divisao : float
subtracao : float

num1 = int(input("Digite o 1º numero:"))
num2 = int(input("Digite o 2º numero:"))

soma = num1 + num2
multiplicacao = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2

print (f"1º numero:{num1}")
print (f"2º numero:{num2}")
print (f"Soma:{soma}")
print (f"Multiplicação:{multiplicacao}")
print (f"Divisão:{divisao}")
print (f"Subtração:{subtracao}")