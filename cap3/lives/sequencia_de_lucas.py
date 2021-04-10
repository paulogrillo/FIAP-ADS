#Fibonacci
#1, 2, 3, 5, 8, ...

#Sequencia de Lucas
# 1, 3, 4, 7, 11, ...
# Anterior1 + anterior2

#atual = anteior1 + anterior2
#anteior1 = anteior2
#anteior2 = atual

quantidade = int(input("Quantos números deseja exibir?"))
anterior1 = 1
anterior2 = 3
atual = 0

for volta in range(1, quantidade+1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    print(atual)