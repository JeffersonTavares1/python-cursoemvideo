from datetime import date
from time import sleep
import os

operador = "+"
simbolos = ["+", "-", "×", "÷", "××", "/", "%"]
car = ["C", "A", "R", "R", "E", "G", "A", "N", "D", "O"]

while True:
    print("一" * 20)
    print("Hora:        |Data:       \n\n" + "一" * 13)
    print("\x1b[1m\x1b[38;5;57m•\t                 Tabuada v.01\x1b[m")
    print("" + "一" * 12)
    print("一" * 20)
    
    tab = "Entra"
    while not (tab.isnumeric() or "." in tab):
        print("\x1b[1m\x1b[38;5;57m•    VALOR DA TABUADA?\x1b[m\n" + ("一" * 10))
        tab = str(input("|            ")).strip().upper()
        print("一" * 20)
    
    print(""" \x1b[1m\x1b[38;5;36m[    0    ]   ADIÇÃO
   [    1    ]   SUBTRAÇÃO
   [    2    ]   MULTIPLICAÇÃO
   [    3    ]   DIVISÃO
   [    4    ]   POTÊNCIA
   
   [    5    ]   DIVISÃO INTEIRA
   [    6    ]   RESTO DA DIVISÃO
   
   [    S    ]   SAIR\x1b[m""")
    print("一" * 20)
    
    op = "Entra"
    while op not in "0123456S":
        print("\x1b[1m\x1b[38;5;57m•     SUA ESCOLHA?\x1b[m\n" + ("一" * 8))
        op = str(input("|            ")).strip().upper()[0]
        print("一" * 20)
    for c in range(0, len(car)):
            print("\x1b[7m\x1b[48;5;57m {}\x1b[m".format(car[c]), end=" ", flush=True)
            sleep(0.1)
    
    
    if op in "0123456":
        operador = simbolos[int(op)]
        os.system("clear") #limpa o terminal
        
        #一一一一一一一一 convertendo de str pra número... 
        if "." in tab:
            tab = float(tab)
        else:
            tab = int(tab)
        #一一一一一一一一
        print("一" * 20)
        while op != "N":
            
            print("\x1b[1m\x1b[38;5;57m•   COMEÇO DA TABUADA?\x1b[m\n" + ("一" * 10))
            do = int(input("|            "))
            print("一" * 20)
            print("\x1b[1m\x1b[38;5;57m•     FINAL DA TABUADA?\x1b[m\n" + ("一" * 10))
            ate = int(input("|            "))
            os.system("clear") #limpa o terminal
            
            print(("一" * 20) + "\n")
            for cont in range(do, ate + 1):
                if "+" in operador:
                    soma = tab + cont
                    
                elif "-" in operador:
                    soma = tab - cont
                    
                elif "×" in operador:
                    soma = tab * cont
                    
                elif "÷" in operador:
                    soma = tab / cont
                    
                elif "××" in operador:
                    soma = tab ** cont
                    
                elif "/" in operador:
                    soma = tab // cont
                    
                elif "%" in operador:
                    soma = tab % cont
                    
                print("{:^4} {} {:^4} = {:^4}".format(tab, operador, cont, soma))
            print("\n" + "一" * 20)
            
            op = "Entra"
            while op not in "SN":
                print("\x1b[1m\x1b[38;5;57m•    Quer Continuar? [S/N]\x1b[m\n" + ("一" * 10))
                op = str(input("|            ")).strip().upper()[0]
                print("一" * 20)
                
            for c in range(0, len(car)):
                print("\x1b[7m\x1b[48;5;57m {}\x1b[m".format(car[c]), end=" ", flush=True)
                sleep(0.1)
            os.system("clear") #limpa o terminal
        
    
    elif op == "S":
        #Sair do código
        print("\n\n" + ("一" * 20))
        print("\x1b[1m\x1b[38;5;3mSaiu ↘! ... \x1b[m")
        print("一" * 20)
        sleep(1.5)
        os.system("clear")
        break
