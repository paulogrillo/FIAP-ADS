valor_compra = float(input("Digite o valor da sua compra: "))
tipo_cliente = input("Informe o tipo do cliente: ")


if "normal" == tipo_cliente.lower():
    if valor_compra < 1000:
        total = valor_compra * 0.97
    elif valor_compra < 2000:
        total = valor_compra * 0.96
    else:
        total = valor_compra * 0.95
elif "vip" == tipo_cliente.lower():
    if valor_compra < 1000:
        total = valor_compra * 0.95
    elif valor_compra < 2000:
        total = valor_compra * 0.93
    else:
        total = valor_compra * 0.92
elif "vip premium" == tipo_cliente.lower():
    if valor_compra < 1000:
        total = valor_compra * 0.09
    elif valor_compra < 2000:
        total = valor_compra * 0.85
    else:
        total = valor_compra * 0.80
else:
    print("O tipo de usuário não foi reconhecido.")

print("Valor da compra é R${} \t Por ser um cliente {}, foi concedido um desconto e o total será R$ {}".format(valor_compra, tipo_cliente, total))