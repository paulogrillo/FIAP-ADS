numero = int(input("Digite um número para a tabuada"))

i = 1

while(i <= 10):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    i = i + 1