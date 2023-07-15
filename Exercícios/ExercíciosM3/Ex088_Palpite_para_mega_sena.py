

filme = {"titulo":"star wars",
               "ano":1977,
               "diretor":"George Lucas",
               "+":"56"
}


print(filme.values())  #mostrar todos valores
print()
print(filme.keys())  #mostra os nomes das chaves
print()
print(filme.items())  #mostra tudo chaves e valores
print()

for k, v, in filme.items():
    print(f"{k} = {v}")


#一一一一一一一一一一一一一一一一
pessoas = {
"nome": "gustavo", "sexo": "M", "idade": 22
}


print(pessoas)
print()
print(pessoas["nome"])
print(pessoas["idade"])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

print("\n\n")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print("\n\n")
for k in pessoas.keys():
    print(k)


del pessoas["sexo"]  #apagar intem
print(pessoas.items())
print()
pessoas["nome"] = "Leadro"  #trocando valor, gustavo vai ser Leandro agora

pessoas["peso"] = 98.5  #se não tive peso ele adicionar se tiver substitue
print(pessoas.items())
print("\n\n")
#-一一一一一一一一一一一一一一一一一

brasil = list()

estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0])
print(brasil[1])
print()

print(brasil[0]["uf"])
print()
print(brasil[1]["sigla"])
print()
#一一一一一一一一一一一一一


estado = dict()
brasil1 = list()

for c in range(3):
    estado["uf"] = str(input("Unidade federativa"))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil1.append(estado.copy())  #copiar o conteúdo de estado pea dentro da lista

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} =  {v}.")



































