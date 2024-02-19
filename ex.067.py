print("para parar digite um numero negativo")
while True:
    n = int(input ("quer saber a tabua de que valor? "))
    if n <= -1:
        break
    for c in range (1,11):
        r = n * c
        print (f"{n} * {c} = {r}")
