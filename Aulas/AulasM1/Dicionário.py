   


dado = dict()

#chave: valor

dado = {"nome": "Pedro", "idade": 25}
print(dado["nome"])

dado["sexo"] = "M"  #adiciona no final do dict se ja tive sexo ele substitui

del dado["idade"]  #removendo pela chave


filme = {"titulo": "star wars", "ano": 1977, "diretor": "George Lucas"}


print()
print(filme.values())  #mostra todos os valores
print(filme.keys())  #mostra todas as chaves
print(filme.items())  #mostra chave e valor


print()
for k, v in filme.items():
    print(f"O {k} é {v}")



pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}

print()
print(pessoas)

print()
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print()
for k in pessoas.keys():
    print(k)

print()
for v in pessoas.values():
    print(v)

print()
for k, v in pessoas.items():
    print(k, ":", v)
print()


#dict dentro de list:
    

brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print()

print(brasil[1])
print()

print(brasil[0]["uf"])  #rio de Janeiro
print()

print(brasil[1]["sigla"])  #SP
print()

#:一一一一一一一一一一一一一一一

estado = dict()
ptbr = list()

for cont in range(3):
    estado["uf"] = str(input("Unidade federativa? "))
    estado["sigla"] = str(input("Sigla do Estado? "))
    
    ptbr.append(estado.copy())
print(ptbr)

print()
for e in ptbr:
    print(f"{e}")
    
    for k, v in e.items():
        print(f"{k} = {v}")


  




operações_feitas

















