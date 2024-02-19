from random  import randint
cont = 0
while True:
    n = int(input("escolha um numero:"))
    pc = randint(0, 10)
    soma = pc + n
    p = " "
    while p not in "PpIi" :
        p = str(input("voce quer par ou impar? [P/I]")).strip().upper()[0]
    print(f"vc jogou {n} e o computador jogou {pc} a soma da {soma}")
    print("deu par" if soma % 2 == 0 else "deu impar")
    if p == "P":
        if soma % 2 == 0:
            print("VOCE VENCEU")
            print("vamos continuar!!")
            cont += 1
        else:
            print("voce perdeu :(")
            break
    if p == "I":
        if soma % 2 == 1:
            print("VOCE VENCEU")
            print("vamos continuar!!")
            cont += 1
        else:
            print("voce perdeu :(")
            break    
print(f"voce venceu consetivamente {cont}")
