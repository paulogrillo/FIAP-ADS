altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
imc = peso / altura**2

print('\033[32m' + '------------------------------')
print('\x1b[1m' + "Seu IMC é: ", imc)


if imc < 16:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Baixo peso Grau III")

elif imc < 17:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Baixo peso Grau II")

elif imc < 18.5:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Baixo peso Grau I")

elif imc < 25:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Peso ideal")

elif imc < 30:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Sobrepeso")

elif imc < 35:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Obesidade Grau I")

elif imc < 40:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Obesidade Grau II")

elif imc > 40:
    print('\x1b[1;31m' + '------------------------------')
    print('\033[34m' + 'Status atual: ')

    print('\033[37m' + "Obesidade Grau III")
