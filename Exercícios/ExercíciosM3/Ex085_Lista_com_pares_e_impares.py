"""Exercício Python 085: Crie um programa onde o usuário 
possa digitar sete valores numéricos e cadastre-os em 
uma lista única que mantenha separados os valores 
pares e impares. No final, mostre os valores pares 
e impares em ordem crescente."""


dados = [[], []]

for c in range(7):
    print("一" * 10)
    valor = int(input(f"{c +1}° Valor: "))
    
    if valor % 2 == 1:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
    
print("一" * 10)
dados[0].sort(reverse=True)
dados[1].sort(reverse=True)

print(
f"Impares: {dados[0]}"
f"\nPares: {dados[1]}"
)
[0].append(valor)
        else:
            dados[1].append(valor)
    
print("一" * 10)
dados[0].sort(reverse=True)
dados[1].sort(reverse=True)

print(
f"Impares: {dados[0]}"
f"\nPares: {dados[1]}"
)
"
)
