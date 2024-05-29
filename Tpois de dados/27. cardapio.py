import os

os.system("cls || clear")

while True:
    print("=== Menu ===")
    print("1- Picanha - 25,00 R$ ")
    print("2 - Lasanha - 20,00 R$")
    print("3 - Strogonoff - 18,00 R$")
    print("4 - Bife acebolado - 15,00R$")
    print("5 - Pão com ovo - 5,00R$")
    op = int(input("Digite a comida que deseja:"))

    match(op):
        case 1:
            print("1- Picanha - 25,00 R$ ")
            break
        case 2:
            print("2 - Lasanha - 20,00 R$")
            break
        case 3:
            print("3 - Strogonoff - 18,00 R$")
            break
        case 4:
            print("4 - Bife acebolado - 15,00R$")
            break
        case 5:
            print("5 - Pão com ovo - 5,00R$")
            break
        case _:
            os.system("cls || clear")