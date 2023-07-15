

"""
frase =
[C] [u] [r] [s] [o]  [ ]  [e] [m]  [  ]  [V] [í] [d] [e] [o]  [  ]  [P] [y] [t]  [h] [o] [n]
 0    1   2   3   4    5   6    7     8     9 10 11 12 13  14 15 16 17 18 19 20  #indese das letras

 fatiamento: [do : ate : pulando]
     frase[9] == >>> V
     frase[9 : 13] >>> Vide
     frase[9 : 20 : 2 ] >>> VdoPto
     
     frase[:5] >>> Curso
     frase[15 :] >>> Python
     frase[9 : : 3] >>> VePh
---------------------------------



#Análise:
    len(frase) >>> 21 <contar a contidade de caracteres da variável>
    frase.count("o") >>> 3 <"conta a contidade de letras o" pode pasar o intervalo ("o", 0, 13) >>> 2
    frase.find("deo") >>> 11 <mostra a posição onde está "deo" na variável> retorna -1 se nao encontrar.
    "Curso" in frase >>> True <pesquisa uma frase na variável, retorna True ou False.>
    frase.isdigit() >>> saber se só tem números int na variável. True e false
    frase.startswith("s") >>> saber se o texto começa com "s"
    frase.endswith("s") >>> saber se o texto termina com "s"


#Transformação:
    frase.replace("Python", "Android") >>> <Procura por Python e troca por Android> obs:
    frase.upper() >>> <bota toda letras em maiusculo>
    frase.lower() >>> <botar toda letras em minúscula
    frase.capitalise() >>> <joga todos as letras em minúsculo menos a primeira letra>
    frase.title() >>> <joga todos começos de letras em maiusculo>
    frase.zfill(20) >>> preencher o começo com 0 ate atingir o número de caracteres passados no parâmetro. (20)
    frase:
        [ ] [ ] [ ] [A] [p] [e] [n] [d] [a] [ ] [P] [y] [t]  [h] [o] [n] [ ]  [ ]   [ ]
         0  1 2   3   4    5   6    7   8   9 10 11 12 13 14 15 16 17 18
     
    frase.strip() >>> <remove todos espaços no começo e no final da frase>
    frase.rstrip() >>> <remover os últimos espaços>
    frase.lstrip() >>> <remover do começo>
    
#Divisão de frase:
    frase =
        [C] [u] [r] [s] [o]  [ ]  [e] [m]  [  ]  [V] [í] [d] [e] [o]  [  ]  [P] [y] [t] [h] [o] [n]
          0   1   2   3   4   5    6    7     8     9 10 11 12 13  14 15 16 1718 19 20  #indese das letras

    frase.split() <onde tiver espaço ele vai criar uma divisão e cada frase dividida vai ter seu indese começando com 0 na lista>
             ---lista-----‐---------------------‐------‐--------‐-‐----‐-------------------‐-------‐-----------------------------
    >>> | [C] [u] [r] [s] [o]  |   [e] [m]  |   [V] [í] [d] [e] [o]  |  [P] [y] [t] [h] [o] [n] |
            |  0    1   2   3   4   |    0    1    |    0    1   2  3   4    |   0    1  2   3   4    5   |  #indese das letras
             ---------‐---0-------‐--------------1---------‐----------2--------------------‐-------‐----3-----------------
    
    
#Junção:
    "_".join(frase) <junto toda frase separada e bota _ no lugar>
    >>> Curso_em_Video_Python
            0123456789*+*+*+*+*+*+
"""




#Pratica:

frase = "CursO em Video Python"

print(frase.count("o")) #>>> 2
print(frase.upper().count("O")) #>>> 3

print(len(frase)) #>>> 21



frase = "   CursO em Video Python   "

print(len(frase)) #>>> 27
print(len(frase.strip())) #>>> 21



frase = "CursO em Video Python"

print(frase.replace("Python", "Android")) #>>> "CursO em Video Android" 
print(frase) #>>> "CursO em Video Python" <replace não muda a variedade, so retorna a frase modificada.

print("CursO" in frase) #>>> True
print(frase.find("CursO")) #>>> 0 <mostra a posição. se retorna -1 e porque não tem>


#                                                 0          1         2            3
print(frase.split()) #>>> ['CursO', 'em', 'Video', 'Python']
#                                                                           3
dividido = frase.split()
print(dividido[0]) #>>> CursO
print(dividido[2] [3]) #>>> e <no índice 2 da lista, mostra o que ta no inde 3 da frase>













