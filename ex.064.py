n = int(input("Digite um numero [para parrar digite 999]:"))
soma = cont = 0
while n != 999:
    cont += 1
    soma += n 
    n = int(input("Digite um numero [para parrar digite 999]:"))
print("vc digitou {} e a soma entre eles foi {}".format(cont,soma))
print("acabou")
