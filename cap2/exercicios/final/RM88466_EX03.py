segundaFeira = int(input("\033[0;0m"+"Digite os votos para Segunda-feira: "))
tercaFeira = int(input("Digite os votos para Terça-feira: "))
quartaFeira = int(input("Digite os votos para Quarta-feira: "))
quintaFeira = int(input("Digite os votos para Quinta-feira: "))
sextaFeira = int(input("Digite os votos para Sexta-feira: "))

if segundaFeira > tercaFeira and segundaFeira > quartaFeira and segundaFeira > quartaFeira and          segundaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Segunda-feira:", "\033[31m", segundaFeira, "votos")

elif tercaFeira > segundaFeira and tercaFeira > quartaFeira and tercaFeira > quintaFeira and tercaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Terça-feira:", "\033[31m", tercaFeira, "votos")

elif quartaFeira > segundaFeira and quartaFeira > tercaFeira and quartaFeira > quintaFeira and quartaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quarta-feira:", "\033[31m", quartaFeira, "votos")

elif quintaFeira > segundaFeira and quintaFeira > tercaFeira and quintaFeira > quartaFeira and quintaFeira > sextaFeira:
        print("====================================")
        print("Mais votado: Quinta-feira:", "\033[31m", quintaFeira, "votos")

elif sextaFeira > segundaFeira and sextaFeira > tercaFeira and sextaFeira > quartaFeira and sextaFeira > quintaFeira:
        print("====================================")
        print("Mais votado: Sexta-feira:", "\033[31m", sextaFeira, "votos")
else:
    print("Empate")

total = segundaFeira + tercaFeira + quartaFeira + quintaFeira + sextaFeira
print("\033[30m"+"\033[47m"+"Total de votos:"+"\033[0;0m"+"\033[31m", total)
