import os
from dataclasses import dataclass
os.system("cls || clear")

QTD_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    num_pag: int
    preco: int

livros = []

for i in range(QTD_LIVROS):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Informe o autor: ")
    num_pag = input("Quantidade de paginas: ")
    preco = input("Digite o preço: ")

    livro = Livro(titulo = titulo, autor = autor, num_pag = num_pag, preco = preco )
    livros.append(livro)

os.system("cls || clear")

for livro in livros:
    print(f"Título:{livro.titulo}")
    print(f"Autor:{livro.autor}")
    print(f"Quantidade de paginas:{livro.num_pag}")
    print(f"Preco:{livro.preco}\n")