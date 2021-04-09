nome_transacao_0 = str(input("Digite o nome da primeira transação:"))
valor_transacao_0 = float(input("Digite o valor da primeira transação:"))

nome_transacao_1 = str(input("Digite o nome da segunda transação:"))
valor_transacao_1 = float(input("Digite o valor da segunda transação:"))

nome_transacao_2 = str(input("Digite o nome da terceira transação:"))
valor_transacao_2 = float(input("Digite o valor da terceira transação:"))

nome_transacao_3 = str(input("Digite o nome da quarta transação:"))
valor_transacao_3 = float(input("Digite o valor da quarta transação:"))

total = valor_transacao_0 + valor_transacao_2 + valor_transacao_3
media = total / 4

print("Total das transações: ", total)
print("Média das transações: ", media)

print("1° Transação: ", nome_transacao_0)
print("2° Transação: ", nome_transacao_1)
print("3° Transação: ", nome_transacao_2)
print("4° Transação: ", nome_transacao_3)