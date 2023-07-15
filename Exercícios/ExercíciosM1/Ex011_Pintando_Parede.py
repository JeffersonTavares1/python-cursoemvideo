#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Largura da parede? "))
autura = float(input("Aultuta da parede? "))

area = largura * autura

print("\nSua parede tem a dimensão de {}x{} e sua area e de {}m2°".format(largura, autura, area))

tinta = area / 2

print("Para pintar essa parede, voce precisara de {}l de tintas.".format(tinta))
