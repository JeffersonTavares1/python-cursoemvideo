"""Exercício Python #062​ - Super Progressão 
Aritmética v3.0, Exercício Python 062: Melhore o 
DESAFIO 061, perguntando para o usuário se ele 
quer mostrar mais alguns termos. O programa
 encerrará quando ele disser que quer mostrar 0 termos."""


print("=" * 17)
print("GERADOR DE PA")
print("=" * 17)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print("{} → ".format(termo), end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))
)
    










































