print('\033[32m'+'Tipos de assinaturas:')
print('-----------------------------')
print('\x1b[1;31m'+'1 = Assinatura Basica')
print('-----------------------------')
print('\x1b[1;31m'+'2 = Assinatura Silver')
print('-----------------------------')
print('\x1b[1;31m'+'3 = Assinatura Gold')
print('-----------------------------')
print('\x1b[1;31m'+'4 = Assinatura Platinum')
print('-----------------------------')

tipoDeAssinatura = int(input('\033[37m'+'Digite a assinatura:'))
faturamentoAnual = float(input('\033[32m'+'Digite o faturamento anual:'))

if tipoDeAssinatura == 1:
    print('\033[32m'+"Sua assinatura é", tipoDeAssinatura, "Basic:")
    print('\033[32m'+"Seu faturamento anual foi: ", faturamentoAnual)
    
    print('\033[31m'+'**Bônus**')
    print('R$', (faturamentoAnual * 0.3))

elif tipoDeAssinatura == 2:
    print('\033[32m'+"Sua assinatura é", tipoDeAssinatura, "Silver:")
    print('\033[32m'+"Seu faturamento anual foi: ", faturamentoAnual)
    print('\033[31m'+'**Bônus**')
    
    print('R$', (faturamentoAnual * 0.2))

elif tipoDeAssinatura == 3:
    print('\033[32m'+"Sua assinatura é", tipoDeAssinatura, "Gold:")
    print('\033[32m'+"Seu faturamento anual foi: ", faturamentoAnual)
    print('\033[31m'+'**Bônus**')
    
    print('R$', (faturamentoAnual * 0.1))

elif tipoDeAssinatura == 4:
    print('\033[32m'+"Sua assinatura é", tipoDeAssinatura, "Platinum:")
    print('\033[32m'+"Seu faturamento anual foi: ", faturamentoAnual)
    print('\033[31m'+'**Bônus**')
    
    print('R$', (faturamentoAnual * 0.05))
else:
    print('\x1b[1;31m'+'Preencha os dados corretamente!')