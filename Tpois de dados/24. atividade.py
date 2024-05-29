import os

os.system("cls || clear")

resultado = False

while True:
    os.system("cls || clear")

    a = int(input("Digite o primeiro numero: "))
    operador = input("Digite o operador: + - * /: ")
    b= int(input("Digite o segundo numero: "))

    match(operador):
        case '+':
            resultado = a+b
        case '-':
            resultado = a-b
        case '*':
            resultado = a*b
        case '/':
            resultado = a/b
        case _:
            print("Opção invalida")

print(f"Resultado: {resultado}")