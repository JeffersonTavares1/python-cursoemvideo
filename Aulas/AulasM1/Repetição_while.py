

#for serve só quando seio o limite de repetição
for c in range(1, 10):
    print(c)
print("fim")


#while serve quando não sei o limite de repetição e
#e quando seio o limite
c = 1
while c < 10:
    print(c)
    c += 1 #c = c + 1
print("fim")
#---------–--------

for c in range(1, 5):
    n = int(input("Digite um valor: "))
print("fim")


n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("fim")



r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar [S/N]: ")).strip().upper()
print("fim")


n = 1
par = impar = 0
while n != 0:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    n = int(input("Digite um valor: "))
    
print("Você digitou {} número pares e {} número ímpares".format(impar, par))



#BREAK:
#--------–------------------




























