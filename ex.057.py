p = str(input("qual é o seu sexo biologico? \nresponda com [M/F]: ")).strip().upper() [0]
if p == "M":
    print("ok vc é um homen")
elif p == "F":
    print("ok vc é uma mulher")
else:
    while p not in "MF":
        print("é nessesario que responda a pergunta conforme os dados apresentados ")    
        p = str(input("faça novamente:")).strip().upper() [0]
        if p == "M":
            print("ok vc é um homen")
        elif p == "F":
            print("ok vc é uma mulher")
        
