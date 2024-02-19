soma = 0
soma2 = 0
mh = 0
nomev = ""
for p in range(1, 5):
    print( "------{}------".format(p))
    n = str(input("Nome:")).strip()
    I = int(input("Idade:"))
    s = str(input("Sexo [M/F]:")).upper()
    if I >= 0:
        soma += I
        div = soma / 4
    if p == 1 and s == "M":
       mh = I
       nomev = n
    if s == "M" and I > mh:
        mh = I
        nomev = n                       
    if s =="F" and I < 20:
        soma2 += 1
print("ao todo a media do grupo é {}".format(div))
print("o homen mais velho é {} e ele tem {} anos".format(nomev, mh))
print("ao todo tem {} mulheres com menos de 20 anos".format(soma2))





