a = int(input("primeiro termo:"))
r = int(input("Razão da PA:"))
c = 1
p = a
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print("{}".format(a), end="")
        print("->", end="")
        a += r
        c += 1
    print("PAUSA")
    mais = int(input("quantos termos voce quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))