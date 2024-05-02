import os

os.system("cls || clear")

num = int(input("Digite o numero:"))

for i in range (1, 11):
    print(f"{num} x {i} = {num * i}")