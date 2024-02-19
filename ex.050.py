soma = 0
cont = 0
for l in range(1, 7):
    n = int(input('digite o {} valor:'.format(l)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('vc informou {} numeros e a soma dos pares foram {}'.format(cont, soma))







