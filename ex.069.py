cont18 = conth = contm = contm20 = 0
while True:
    print("-" * 30)
    print("CADASTRE UM PESSOA")
    print("-" * 30)
    idade = int(input("Idade:"))
    if idade > 18:
        cont18 += 1
    sexo = " "
    while sexo not in "HM":
        sexo = str(input("Sexo [H/M]:")).strip().upper()[0]
        if sexo == "H":
            conth += 1
        elif sexo == "M":
            contm += 1
            if idade < 20:
                contm20 += 1
    print("-" * 30)
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [s/n]")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {cont18}")
print(f"Ao todo temos {conth} homens cadastrados")
print(f"Ao todo temos {contm} mulheres cadastradas")
print(f"E temos {contm20} com menos de 20 anos")


    