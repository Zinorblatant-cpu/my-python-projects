
def titulo():
    print("Me de cordenadas e te mostrarei em que quadrante estão")

def codigo():
    num = int(input("Me de um valor de X :"))
    num_1 = int(input("Me de um valor de Y :"))

    if num > 0 and num_1 > 0:
        print("O seu ponto esta no Primeiro Quadrante")
    elif num < 0 and num_1 > 0:
        print("O seu ponto esta no Segundo Quadrante")
    elif num > 0 and num_1 < 0:
        print("O seu ponto esta no Terceiro Quadrante")
    elif num < 0 and num_1 < 0:
        print("O seu ponto esta no Quarto Quadrante")

def main():
    titulo()
    codigo()
if __name__ == '__main__':
    main()
