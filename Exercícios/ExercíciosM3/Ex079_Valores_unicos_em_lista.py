

valores = []

while True:
    num = int(input("\nDigite um valor: "))
    
    if num not in valores:
        valores.append(num)
        print("Adicionado com sucesso...")
    else:
        print("Valor duplicado, não Adicionado...")
    
    continuar = str(input("Quer continuar [S]im ou [N]ão: ")).strip().upper()
    if continuar == "N":
        break

valores.sort()
print(f"\nNumeros digitados em ordem crescente {valores}")
