num = (int(input("digite um numero:"))), (int(input("digite um numero:"))), (int(input("digite um numero:"))), (int(input("digite um numero:")))
print(f"Os numeros digitados foram {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 foi digitado na possição {num.index(3)+ 1}")
else:
    print("o valor tres não foi digitado em nem uma possição")
print(f"os valores pares foram ", end= "")
for n in num:
    if n % 2 == 0:
        print(n, end=' ')