numex = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze ou catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print("-" * 100)
print("me fale numeros de 0 a 20 que escreverie eles por extenso pra voce!!!")
print("-" * 100)
while True:
    n = int(input("Qual numero vc quer escrito por extenso?:"))
    if n <= 20:
        break
    print("Tente novamente mas digitando numeros entre 0 a 20")
print(f"Voce digitou o numero {numex[n]} :)")