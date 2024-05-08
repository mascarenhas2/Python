import os
os.system("cls || clear")

nota = float(input("Digite a nota:"))

 while True:
   nota = int(input("Digite a nota: "))

 if nota < 0 or nota > 10:
   print("Nota invalida. A nota deve estar entre 0 e 10. Por favor, tente novamente.")
 else:
   print("Nota valida:", nota)
break