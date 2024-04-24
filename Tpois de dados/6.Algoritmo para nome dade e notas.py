import os

os.system("cls || clear")

nome : str
idade: int
nota1 : float
nota2 : float
mediaA : float

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade"))
nota1 = float(input("Digite sua 1º nota"))
nota2 = float(input("Digite sua 2º nota"))

mediaA = (nota1 + nota2)/2

os.system("cls || clear")

print(f"Nome:{nome}")
print(f"idade:{idade}")
print(f"nota1:{nota1}")
print(f"nota2:{nota2}")
print(f"Media aritmética:{mediaA}")