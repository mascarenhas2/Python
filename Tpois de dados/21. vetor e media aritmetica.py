import os

os.system("cls || clear")


notas = []
soma = 0
media = 0
for i in range(3):
    nota = float(input("Digite sua nota:"))
    notas.append(nota)
    soma += nota
media = soma / 3
for i in range(3):
    print(f"Nota: {notas[i]}")

print(f"Média: {media}")
