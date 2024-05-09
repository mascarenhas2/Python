import os

os.system("cls || clear")

somaGeral = 0
quantidadeGeral = 0
somaPares = 0
pares = 0
impares = 0

while True: 
    numero = int(input("Digite um numero:"))

    if numero > 0:
        somaGeral += numero
        quantidadeGeral += 1

        if numero % 2 == 0:
            somaPares += numero
            quantidadeGeral += 1

            if numero % 2 == 0:
                somaPares += numero
                pares += 1
            else:
                impares += 1
                