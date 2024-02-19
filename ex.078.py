lista = []
menor = 0
maior = 0
for cont in range(0, 5):
    lista.append(int(input("digite um valor:")))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f"vc digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} na possição", end="")
for c, v in enumerate(lista):
     if v == maior:
         print(f" {v}")
print(f"O menor valor digitado foi {menor} na possição", end="")
for c, v in enumerate(lista):
    if v == menor:
        print(f" {v}")
