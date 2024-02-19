n = int(input("coloque seu numero:"))
print("vc quer converter pra que tipo? \n[ 1 ] binario \n[ 2 ] octal \n[ 3 ] hexadecimal")
op = str(input("escolha uma opeção:")).strip()
if op == '1':
     print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif op == '2':
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif op == '3':
    print('{} convertido para hexadecimal {}'.format(n, hex(n)[2:]))
else:
    print('opeção invalida tente denovo')

