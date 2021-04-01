lixo1 = float(input("Por favor, digite o peso do primeiro lixo"))
lixo2 = float(input("Por favor, digite o peso do segundo lixo"))
lixo3 = float(input("Por favor, digite o peso do terceiro lixo"))

if lixo1 < lixo2 and lixo1 < lixo3:
    print("O primeiro lixo é o mais leve ")
else:
    if lixo2 < lixo1 and lixo2 < lixo3:
        print("o o segundo é mais leve")
    else:
        if lixo3 < lixo1 and lixo3 < lixo2:
            print("O terceiro lixo")
        else:
            print("Existem lixos com peso iguais")
