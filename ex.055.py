maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("peso da {} pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("o maior pesso foi {}Kg".format(maior))
print("o menor pesso foi {}Kg".format(menor))
