import os 

os.system("cls || clear")

media = 0
soma = 0

for i in range (1,4):
    num = int(input(f"Digite a {i}º Nota:"))

    soma += num

media = soma / 3

if media >= 7:
    print("Aprovado")
elif media < 6.99:
    print("Recuperação")
else: 
    print("Reprovado")  

print(f"Sua media é: {media}")      