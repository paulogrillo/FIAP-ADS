class DiaSemanaVotacao:
    nome = ""
    total = 0

    def votacaoResult(self, diaSemanaVotacao): 
        diaSemanaMaximo = self.init("", 0)

        for diaSemana in diaSemanaVotacao:
            if(int(diaSemana.total) > int(diaSemanaMaximo.total)):
                diaSemanaMaximo = diaSemana 
        print(("Dia da semana:{}\n total mais votado: {}").format(diaSemanaMaximo.nome, diaSemanaMaximo.total))

    def init(self, nome, total):
        self.nome = nome
        self.total = total
        return self

class Assinatura:

    diaSemanaVotacao = [
        DiaSemanaVotacao().init("Segunda-feira", 0),
        DiaSemanaVotacao().init("Terca-feira", 0),
        DiaSemanaVotacao().init("Quarta-feira", 0),
        DiaSemanaVotacao().init("Quinta-feira", 0),
        DiaSemanaVotacao().init("Sexta-feira", 0),
    ]

    def init(self):
        for diaSemana in self.diaSemanaVotacao:
            valor = input(diaSemana.nome + ": total ->")
            diaSemana.total = valor

        for diaSemana in self.diaSemanaVotacao:
            print("nome: " + diaSemana.nome + " == total:" + diaSemana.total)          

        print("O mais votado é: ")
        DiaSemanaVotacao().votacaoResult(self.diaSemanaVotacao)

Assinatura().init()