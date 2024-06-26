import os 
import time
import sys

os.system("cls || clear")

valor=float(input("Digite o valor do produto:"))
os.system("cls || clear")
print("1\t Pagamento a vista.")
print("2\t Pagamento parcelado.")
pag=int(input("Escolha a forma de pagamento.\n"))
match (pag):
    case 1:
      desc = valor*0.1
      valorfinal = valor - desc
      forma = "Pagamento a vista."
    case 2:
      os.system("cls || clear")
      parcela = int(input("Digite o numero de parcelas:"))
      valorparcela = valor/parcela
      forma = "Pagamento parcelado."
    case _:
      input("Opção escolhida invalida, selecione novamente.")
os.system   ("cls || clear") 
if pag == 1:
    print(f"Valor do produto: R${valor}")
    print(f"Forma de pagamento: {forma}")
    print(f"Desconto aplicado: {desc}")
    print(valorfinal)
elif pag == 2
else :
   print("Operação invalida.")
