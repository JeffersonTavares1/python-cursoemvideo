"""Exercício Python 082: Crie um programa que vai 
ler vários números e colocar em uma lista. Depois 
disso, crie duas listas extras que vão conter apenas 
os valores pares e os valores impares digitados, 
respectivamente. Ao final, mostre o conteúdo das três 
listas geradas"""


Lista = []

while True:
    num = str(input("\nDigite um valor: [S]air: ")).strip().upper()
    if num.isdigit():
        Lista.append(int(num))
        print("Valor adicionado a Lista")
    elif num in "S":
        break
    else:
        print("ERRO, tente novamente...")
        continue
    
Par = []
Impar = []

for v in Lista:
    if v % 2 == 0:
        Par.append(v)
    else:
        Impar.append(v)

print(
f"\n{Lista = }"
f"\n{Par = }"
f"\n{Impar = }"
)




