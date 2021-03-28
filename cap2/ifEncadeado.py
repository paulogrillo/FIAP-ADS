pontuacao = int(input('Informe a pontuação!'))

if pontuacao > 1000:
    print('Você ganhou 3gb de bônus!')
elif pontuacao > 500:
    print('Você ganhou 1,5gb de Bônus!')
elif pontuacao > 200:
    print('você gangou 500mb de bônus')
else:
    print('Você não ganhou nada.')