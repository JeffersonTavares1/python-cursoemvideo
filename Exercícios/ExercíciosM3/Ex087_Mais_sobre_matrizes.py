"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

from time import sleep


matriz = [[], [], []]

soma_pares = soma_3_coluna = mair_2_linha = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha},  {coluna}]: "))
        matriz[linha].append(valor)
        
        if valor % 2 == 0:  #A) A soma de todos os valores pares digitados.
            soma_pares += valor
        
print("一" * 23)
for linha in range(3):
    
    for coluna in range(3):
        print(f"[\x1b[38;5;124m{matriz[linha][coluna]:^5}\x1b[m]", end="    ", flush=True)
        sleep(0.3)
        if coluna == 2:  #B) A soma dos valores da terceira coluna.
            soma_3_coluna += matriz[linha][coluna]
            
        if linha == 1:  #C) O maior valor da segunda linha.
            if coluna == 0:
                mair_2_linha = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > mair_2_linha:
                    mair_2_linha = matriz[linha][coluna]
            
    print(f"linha {linha}")  #quebra o end="   "
    sleep(0.3)
            
print("一" * 23)
print(
f"A soma dos valores pares é {soma_pares}"
f"\nA soma do valores da 3ª coluna {soma_3_coluna}"
f"\nO maior valor da segunda linha é {mair_2_linha}"
)
