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
else:
    if segundaFeira == tercaFeira or segundaFeira == quartaFeira:
        print("Empatou!!")
    else:
        if segundaFeira == quintaFeira or segundaFeira == sextaFeira:
            "Empatou!!"

if tercaFeira > segundaFeira and tercaFeira > quartaFeira:
    maisVotado = tercaFeira
    if tercaFeira > quintaFeira and tercaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Terça-feira", "\033[31m", tercaFeira, "votos")
        maisVotado = tercaFeira
else:
    if tercaFeira == segundaFeira or tercaFeira == quartaFeira:
        print("Empatou!!")
    else:
        if tercaFeira == quintaFeira or tercaFeira == sextaFeira:
            print("Empatou!!")

if quartaFeira > segundaFeira and quartaFeira > tercaFeira:
    maisVotado = quartaFeira
    if quartaFeira > quintaFeira and quartaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quarta-feira", "\033[31m", quartaFeira, "votos")
        maisVotado = quartaFeira
else:
    if quartaFeira == segundaFeira or quartaFeira == tercaFeira:
        print("Empatou!!")
    else:
        if quartaFeira == quintaFeira or quartaFeira == sextaFeira:
            print("Empatou!!")

if quintaFeira > segundaFeira and quintaFeira > tercaFeira:
    maisVotado = quartaFeira
    if quintaFeira > quartaFeira and quintaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quinta-feira", "\033[31m", quintaFeira, "votos")
        maisVotado = quartaFeira
else:
    if quintaFeira == segundaFeira or quintaFeira == tercaFeira:
        print("Empatou!!")
    else:
        if quintaFeira == quartaFeira or quintaFeira == sextaFeira:
            print("Empatou!!")

if sextaFeira > segundaFeira and sextaFeira > tercaFeira:
    maisVotado = sextaFeira
    if sextaFeira > quartaFeira and sextaFeira > quintaFeira:
        print("====================================")
        print("Mais votado: Sexta-feira", "\033[31m", sextaFeira, "votos")
        maisVotado = sextaFeira
else:
    if sextaFeira == segundaFeira or sextaFeira == tercaFeira:
        print("Votos iguaís sexta-feira")
    else:
        if sextaFeira == quartaFeira or sextaFeira == quintaFeira:
            print("Votos iguaís sexta-feira")

total = segundaFeira + tercaFeira + quartaFeira + quintaFeira + sextaFeira
print("\033[30m"+"\033[47m"+"Total de votos"+"\033[0;0m"+"\033[31m", total)
