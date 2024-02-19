n1 = int(input("Escolha um numero:"))
n2 = int(input("Escolha outro numero:"))
p = 0
while p != 6:
    print("[ 1 ] SOMAR \n[ 2 ] SUBITRAIR \n[ 3 ] DIVIDIR \n[ 4 ] MULTIPLIAR \n[ 5 ] NOVOS NUMEROS \n[ 6 ] SAIR")
    p = int(input(">>>> Qual a sua escolha?"))
    if p == 1:
        n3 = n1 + n2
        print("a soma de {} + {} é igual a {}".format(n1, n2, n3))
    if p == 2:
        n3 = n1 - n2
        print("a subtração  de {} - {} é igual a  {}".format(n1, n2, n3))
    if p == 3:
        n3 = n1 / n2
        print("a divição de {} / {} é igual a  {}".format(n1, n2, n3))
    if p == 4:
        n3 = n1 * n2
        print("a multiplicação de {} * {} é igual a {}".format(n1, n2, n3))
    if p == 5:
        n1 = int(input("Escolha um numero:"))
        n2 = int(input("Escolha um numero:"))
print("Obrigado volte sempre !!")