num1 = int(input('coloque o primeriro numero:'))
num2 = int(input('coloque o segundo numero'))
if num1 > num2:
    print('o numero {} é maior que o {}'.format(num1, num2))
elif num1 < num2:
    print('o numero {} é menor que {}'.format(num1, num2))
elif num1 == num2:
    print('os dois são iguais')
else:
    print('erro, tente denovo')