procurando = int(input("qual numero você quer encontrar na sequencia de lucas ?"))

achei = False
anterior1 = 1
anterior2 = 3
atual = 0

while(not achei):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual

    if (procurando == atual):
        print("encontrei o número.. ")
        achei = True
    