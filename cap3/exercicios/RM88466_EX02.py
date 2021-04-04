#2 – Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.

#Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.

#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.


#Deve informar quantas transações realizou no dia
#Deve informar o valor de cada transação 
#Deve exibir no final o valor total gasto 
#Deve calcular média do valor de cada transação

iniciar = input("Deseja iniciar? Digite (S) ")

if iniciar == "S":
    nome_transacao_0 = str(input("Digite o nome primeira transação:"))
    nova_transacao_0 = float(input("Digite o valor da primeira transação:"))
else:
    print("Que pena..")
nome_transacao_1 = str(input("Digite o nome da segunda transação:"))
nova_transacao_1 = float(input("Digite o valor da segunda transação:"))
continuar = input("Deseja continuar ? ")

if continuar == "S":
    nome_transacao_2 = str(input("Digite o nome da terceira transação:"))
    nova_transacao_2 = float(input("Digite o valor da terceira transação:"))
    total = nova_transacao_0 + nova_transacao_1 + nova_transacao_2
    print("Total das transações:", total)
    media = total / 3
    print(media)
    continuar = input("Deseja continuar ? ")
else:
    print("Fim")
    total = nova_transacao_0 + nova_transacao_1 + nova_transacao_2
    print("Total das transações:", total)
    media = total / 3
    print("Média", media)
