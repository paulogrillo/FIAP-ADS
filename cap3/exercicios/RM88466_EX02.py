#2 – Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.

#Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.

#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.


#Deve informar quantas transações realizou no dia
#Deve informar o valor de cada transação 
#Deve exibir no final o valor total gasto 
#Deve calcular média do valor de cada transação

nome_transacao_0 = str(input("Digite o nome da primeira transação:"))
valor_transacao_0 = float(input("Digite o valor da primeira transação:"))
breakContinue = input("Nova transação(S) Encerrar(N)")

if breakContinue == "S":
    nome_transacao_1 = str(input("Digite o valor da segunda transação:"))
    valor_transacao_1 = float(input("Digite o nome da segunda transação:"))
elif breakContinue == "N":
    total = valor_transacao_0 + valor_transacao_1
    print("Total das transações:")
    print("R$", total)