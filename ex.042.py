a = int(input('primero segmento:'))
b = int(input('segundo segmento:'))
c = int(input('terceiro segmento'))
if a < b + c and b < c + a and a < c + b:
    print('é um triangulo, e ele pode forma um triangulo ',end='')
    if a == b and b == a:
       print('equilatero')
    elif a != b and b != c and a != c:
        print('equilatero')
    else:
        print('isosceles')
else:
    print('não forma um triangulo')




