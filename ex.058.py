from random import randint
T = 1
print("escolha um nomero de 0 a 5 e eu tentarei adivinhar")
pc = randint(0, 5)
j = int(input("escolha um numero de 0 a 5:"))
if j == pc:
    T = 1
    print("vc acertou")
else:
    while pc != j:
        print("eita vc errou :( \neu pensei em {} e vc colocou {}".format(pc, j))
        print("vamos novamente")
        pc = randint(0, 5)
        j = int(input("escolha um numero de 0 a 5:"))
        T += 1
        if pc == j:
            print("vc acertou ")
print("sua tentativas foram {}".format(T))