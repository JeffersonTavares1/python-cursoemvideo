

"""
\033[stylo; texto; fundoM

Branco = 30, 40
Vermelho = 31, 41
Verde  = 32, 42
Amarelo = 33, 43
Azul = 34, 44
Rosa = 35, 45
Azul claro = 36, 46
Sinza = 37, 47

Stylo = 0 none,  1 Bold,  4 Underline,  7 Inverter
"""

from colored import fg, bg, attr


print(f'{fg("#00005f")} Hello World !!! {attr("reset")}')

#fg() == titolo
#bg() == fundo
#attr() == fim?



bg() == fundo
#attr() == fim?



