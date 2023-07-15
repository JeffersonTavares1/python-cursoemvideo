#

"""
import <usar para importa tudo da biblioteca>
from math import sqrt <usar from para importa so uma fuçao na biblioteca>
from math import sqrt, pow <usar virgula para importa 2 fuçao na biblioteca>

"""


#----------------------------
#MATH:
"""
math <biblioteca de matematica no python>
    ceil(num) <usar para aredondar um numero flotuante pra cima>
    floor(num) <usar para aredondar um numero flotuante para baixo>
    trunc(num) <usar para eliminar da virgula pra frente sem aredondar o numero>
    pow(num) <fuciona de forma cemeliante aos 2 **>
    sqrt(num) <usar para calcular raiz quadrada>
    factorial <usar para calcular fatorial>
    hypot(co, ca) <calcular a hipotenusa < (co ** 2 + ca ** 2) ** (1/2)
    #---<usar para calculo de seno, cossano, tangente.
    sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))
    #----
    
    
"""

#RANDOM
"""
random <biblioteca para usar numeros aleatorios
    random() <gera numeros floatuantes entre 0 e 1> #0.3528306983961
    randint(1, 10) <gera numeros aleatorios inteiros informado dentro do (de 1, ate 10)>
    choices() #<usar para fazer uma escolha aleatoria em uma lista>
    shuffle #<usar para embaralhar a ondem de itens em uma lista. nao precisa atribuir a uma variável pra funcionar>
    
    
"""

#TIME
"""
time <biblioteca para alterar o tempo
    sleep(3) <congela o tempo de execução do código a cima dele por 3 segundos nesse caso>
"""

#DETETIME
"""
datetime <biblioteca para trabalhar com datas>
    date.today().year <pega o ano atual>
    
    
    
"""

#----------------------‐---------






#PRATICA:

"""#ex 1
import math

num = int(input("Digite um numero: ")) #29

raiz = math.sqrt(num) #<5.31>

print("A raiz de {} e igial a {:.2f}".format(num, math.ceil(raiz))) #<ceil fez aredondar pra 6>
"""

"""#ex2
from math import sqrt, ceil

num = int(input("Digite um numero: ")) #29

raiz = sqrt(num) #<5.31>

print("A raiz de {} e igial a {:.2f}".format(num, ceil(raiz))) #<ceil fez aredondar pra 6>
"""

"""
import random

num = random.random()
print(num) #0.9422757186360866

num = random.randint(1, 10)
print(num) #6
"""

import emoji

print(emoji.emojize("Olá, Mundo :thumbs_up:"))
:"))
