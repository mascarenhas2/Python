import os 

os.system ("cls || clear")

while True:
    numero = int(input("Digite um dia da semana de 1 a 7: "))

    match(numero):
        case 1:
            print("Domingo na fé de cristo \n Final de semana.")
            break
        case 2:
            print("Segunda feira de cristo. \n Dia de semana.")
            break
        case 3:
            print("Terça na fé de abraão. \n Dia de semana.")
            break
        case 4:
            print("Quarta na paz do pai. \n Dia de semana.")
            break
        case 5:
            print("Quinta na mão do senhor. \n Dia de semana.")
            break
        case 6:
            print("Sexta feira dos oprimidos. \n Dia de semana.")
        case 7:
            print("Sabado, dia de paz e felicidade. \n Final de semana.")

        case _:
            input("Opção invalida")
            