import os
from dataclasses import dataclass
os.system("cls || clear")

#constante
QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str 
    idade: int
    peso: int
    altura: int
    sexo: str

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    peso = input("Digite sua altura: ")
    altura = input("Digite seu peso: ")
    sexo = input("Digite seu sexo: 'M' ou 'F': ")

    
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura, sexo = sexo)
    alunos.append(aluno) 
    sexo.upper()

os.system("cls || clear")
#Exibindo dados para o usuario 
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso:{aluno.peso}")
    print(f"Altura:{aluno.altura}")
    print(f"Sexo:{aluno.sexo}\n")
