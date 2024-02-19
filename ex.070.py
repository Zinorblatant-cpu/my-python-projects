total = maior = menor = cont = totmil = 0
barato = " "
caro = " "
while True:
    produ = str(input("Nome Do Produto:"))
    v = float(input("Preço: R$"))
    cont += 1
    total += v
    if v > 1000:
        totmil += 1
    if cont == 1:
        maior = menor = v
        barato = caro = produ
    else:
        if v > menor:
            maior = v
            caro = produ
        elif v < menor:
            menor = v   
            barato = produ
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]:")).strip().upper()[0]
    if continuar == "N":
        break
print(f"A soma total dos preços deram R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000")
print(f"O produto mais caro foi {caro}")
print(f"O produto mais barato foi {barato}")
