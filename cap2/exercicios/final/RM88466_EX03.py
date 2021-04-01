segundaFeira = int(input("Digite os votos para Segunda-feira"))
tercaFeira = int(input("Digite os votos para Terça-feira"))
quartaFeira = int(input("Digite os votos para Quarta-feira"))
quintaFeira = int(input("Digite os votos para Quinta-feira"))
sextaFeira = int(input("Digite os votos para Sexta-feira"))

if segundaFeira > tercaFeira and segundaFeira > quartaFeira:
    print("Mais votado: Segunda-feira", segundaFeira)
    maisVotado = segundaFeira
    if segundaFeira > quartaFeira and segundaFeira > sextaFeira:
        maisVotado = segundaFeira
        print("Mais votado: Segunda-feira", segundaFeira)
elif tercaFeira > segundaFeira and tercaFeira > quartaFeira:
    print("Mais votado: Terca-feira", tercaFeira)
    maisVotado = tercaFeira
    if tercaFeira > quintaFeira and tercaFeira > sextaFeira:
        maisVotado = tercaFeira
        print("Maior", tercaFeira)
elif quartaFeira > segundaFeira and quartaFeira > tercaFeira:
    print("Mais votado: Quarta-feira", quartaFeira)
    maisVotado = quartaFeira
    if quartaFeira > quintaFeira and quartaFeira > sextaFeira:
        print("Mais votado: Quarta-feira", quartaFeira)
        maisVotado = quartaFeira

total = segundaFeira + tercaFeira + quartaFeira + quintaFeira + sextaFeira
print("Maid votado:", maisVotado)
print("Total de votos", total)
