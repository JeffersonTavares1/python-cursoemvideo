



teste = []

teste.append("Gustavo")
teste.append(40)
print(teste)
#teste == ['Gustavo', 40]


galera = []
galera.append(teste[:])
print(galera)
#galera == [['Gustavo', 40]]

"""
teste[0] = "Maria"
teste[1] = 22
galera.append(teste)  #sem [:] isso da errado... 
print(galera)
#[['Maria', 22], ['Maria', 22]]
"""

teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
#[['Gustavo', 40], ['Maria', 22]]


galera1 = [["João", 19], ["Tana", 33], ["Joaquim", 13]]

print(galera1)
#[['João', 19], ['Tana', 33], ['Joaquim', 13]]

print(galera1[0])
#["João", 19]

print(galera1[0][0])
#Joao

print(galera1[2][1])
#13

for pessoa in galera1:
    print(pessoa)
"""
['João', 19]
['Tana', 33]
['Joaquim', 13]
"""


for pessoa in galera1:
    print(pessoa[0])
"""
João
Tana
Joaquim
"""

for pessoa in galera1:
    print(pessoa[1])
"""
19
33
13
"""




galera2 = []
dado = []
totmaior = totmenor = 0

for cont in range(3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera2.append(dado[:])
    dado.clear()


print(galera2)

for p in galera2:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{p[0]} e Maior de idade")
        totmenor += 1

print(f"Temos {totmaior} Maiores de idade \
\nTemos {totmenor} Menores de idade")



















