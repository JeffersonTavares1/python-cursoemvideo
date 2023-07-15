"""Python 073: Crie uma tupla preenchida com os 20 
primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Corinthians."""

times = ("América-MG", "Athletico-PR", "Atlético-MG", 
"Bahia", "Botafogo", "Corinthians", "Coritiba", "Cruzeiro", 
"Cuiabá", "Flamengo", "Fluminense",  "Fortaleza", 
"Goiás", "Grêmio", "Internacional", "Palmeiras", 
"Bragantino", "Santos", "São Paulo", "Vasco da Gama")

print("\nOs 5 primeiros colocados:") #times[0: 5]
print("一" * 20)
for cont in range(0, 5):
    print("{}ª Posição:  {}".format(cont +1, times[cont]))
print("一" * 20)

print("\nOs 4 últimos colocados:") #times[-4:]
print("一" * 20)
for cont in range(len(times) -1, len(times) - 5, -1):
    print("{}ª Posição:  {}".format(cont +1, times[cont]))

print("一" * 20)
print("\nTimes em ordem alfabética:") 
print("一" * 20)
for cont in range(0, len(times)):
    print(sorted(times)[cont])
print("一" * 20)

print("Corinthians está na {}ª Posição".format(times.index("Corinthians") +1))
print("一" * 20)



"""
for c, time in enumerate(times):
   if c <= 4: # enquanto c 0 <= a 4 mostra time
       print(c +1, time)
       
   elif c > len(times) -5:  #enquanto 0 > 15 mostra time: exp: print(c, ">", len(times) -5)
       print(c +1, time)
"""
