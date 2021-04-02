segundaFeira = int(input("\033[0;0m"+"Digite os votos para Segunda-feira: "))
tercaFeira = int(input("Digite os votos para Terça-feira: "))
quartaFeira = int(input("Digite os votos para Quarta-feira: "))
quintaFeira = int(input("Digite os votos para Quinta-feira: "))
sextaFeira = int(input("Digite os votos para Sexta-feira: "))

if segundaFeira > tercaFeira and segundaFeira > quartaFeira:
    maisVotado = segundaFeira
    if segundaFeira > quartaFeira and segundaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Segunda-feira", "\033[31m", segundaFeira, "votos")
        maisVotado = segundaFeira

if tercaFeira > segundaFeira and tercaFeira > quartaFeira:
    maisVotado = tercaFeira
    if tercaFeira > quintaFeira and tercaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Terça-feira", "\033[31m", tercaFeira, "votos")
        maisVotado = tercaFeira
if quartaFeira > segundaFeira and quartaFeira > tercaFeira:
    maisVotado = quartaFeira
    if quartaFeira > quintaFeira and quartaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quarta-feira", "\033[31m", quartaFeira, "votos")
        maisVotado = quartaFeira

if quintaFeira > segundaFeira and quintaFeira > tercaFeira:
    maisVotado = quartaFeira
    if quintaFeira > quartaFeira and quintaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quinta-feira", "\033[31m", quintaFeira, "votos")
        maisVotado = quartaFeira

if sextaFeira > segundaFeira and sextaFeira > tercaFeira:
    maisVotado = sextaFeira
    if sextaFeira > quartaFeira and sextaFeira > quintaFeira:
        print("====================================")
        print("Mais votado: Sexta-feira", "\033[31m", sextaFeira, "votos")
        maisVotado = sextaFeira

total = segundaFeira + tercaFeira + quartaFeira + quintaFeira + sextaFeira
print("\033[30m"+"\033[47m"+"Total de votos"+"\033[0;0m"+"\033[31m", total)
