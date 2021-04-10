#2 – Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.
# Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.

##############  Requisitos   ####################
#Deve informar quantas transações realizou no dia
#Deve informar o valor de cada transação 
#Deve exibir no final o valor total gasto 
#Deve calcular média do valor de cada transação

nome_transacao_0 = str(input("Digite o nome da primeira transação:"))
valor_transacao_0 = float(input("Digite o valor da primeira transação:"))
if valor_transacao_0 <= 0:
    print("Insira um valor na transação!")
elif valor_transacao_0 > 0:
    print(nome_transacao_0, valor_transacao_0)
    contador = 1

nome_transacao_1 = str(input("Digite o nome da segunda transação:"))
valor_transacao_1 = float(input("Digite o valor da segunda transação:"))
if valor_transacao_1 <= 0:
    print("Inseira um valor na transação!")
elif valor_transacao_1 > 0:
    print(nome_transacao_1, valor_transacao_1)
    contador = 2

nome_transacao_2 = str(input("Digite o nome da terceira transação:"))
valor_transacao_2 = float(input("Digite o valor da terceira transação:"))
if valor_transacao_2 <= 0:
    print("Insira um valor na transação!")
elif valor_transacao_2 > 0:
    print(nome_transacao_2, valor_transacao_2)
    contador = 3

total = valor_transacao_0 + valor_transacao_1 + valor_transacao_2
media = total / 3

print("\x1b[1;31m", "##======##======##======##=======##====##", "\033[0;0m")

print("Número de transações:", contador)
print("Valor total gasto: R${:.2f}".format(total))
print("Valor médio das transações: R${:.2f}".format(media))

print("\033[0;0m")
print("Histórico de transações:")
print("ID 1", nome_transacao_0, "R$ {:.2f}".format(valor_transacao_0))
print("ID 2", nome_transacao_1, "R$ {:.2f}".format(valor_transacao_1))
print("ID 3", nome_transacao_2, "R$ {:.2f}".format(valor_transacao_2))
print("\x1b[1;31m")