import os

os.system("cls || clear")

print("\n=== Solicitando dados ===")
pesoMorangos = float(input("Digite o peso de morangos(em kg):"))
pesoMacas = float(input("Digite o peso de maçãs(em kg):"))

if pesoMorangos > 25:
    precoMorango = 2.50
else :
     precoMorango = 2.50

if pesoMacas < 5:
     precoMaca = 1.50
else:
     precoMaca = 1.50

pesoTotal= pesoMorangos + pesoMacas
subTotal = (precoMorango * pesoMorangos) +(precoMaca * pesoMacas)

if pesoTotal > 8 or subTotal > 25:
     desconto = subTotal * 0.10
else:
     desconto = 0

totalPagar = subTotal - desconto

print ("\n===Exibindo resultados ===")
print (f"Peso de morangos (em kg):{pesoMorangos}")
print (f"Peso de maçãs (em kg):{pesoMacas}")
print (f"Soma dos pesos (em kg):{pesoTotal}")
print (f"Subtotal:R$ {subtotal:.2f}")
print (f"Total a pagar: R${totalPagar:.2f}")
