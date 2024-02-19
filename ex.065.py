resp = "S"
soma = quant = meidia = maior = menor = 0
while resp in "Ss":
    n = int(input("Digite um numero:"))    
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Quer continuar? [s/n]:")).upper().strip()[0]
media = soma / quant 
print(f"vc digitou {quant} e a media foi {media}")
print("o maior numero foi {} e o menor foi {}".format(maior, menor))

