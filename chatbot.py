import os


def processar_resposta(pergunta, nome):
    if pergunta == "1":
        print(f"{os.linesep}{nome}, Filme: 1 - TROLLS 3 - JUNTOS NOVAMENTE (Sala 1){os.linesep}Filme 2 - FIVE NIGHTS AT FREDDYS - O PESADELO SEM FIM (Sala2){os.linesep}")
    elif pergunta == "2":
        print(f"{os.linesep}{nome}, Sala 1: 14:00 / 19:00{os.linesep}Sala 2: 15:00 / 20:00{os.linesep}")
    elif pergunta == "3":
        print(f"{os.linesep}{nome}, Qual tipo de ingresso você deseja saber o valor?{os.linesep}")
    elif pergunta == "4":
        print(f"{os.linesep}{nome}, O valor do ingresso interio é: R$ 30 + taxas!{os.linesep}")
    elif pergunta == "5":
        print(f"{os.linesep}{nome}, O valor do ingresso para meia entrada é: R$ 15 + taxas!{os.linesep}")
    elif pergunta == "6":
        print(f"{os.linesep}{nome}, Que pena que deseja sair, mas se você teve todas as suas perguntas respondidas, agradeço por ter utilizado nosso chat, abraços! (❁´◡`❁){os.linesep}")
    else:
        print("Digite apenas as opções 1, 2, 3, 4, 5 ou 6!")    

def start():
    #apresentando o chat
    print("Seja bem-vinda(o) ao chat. ")
    nome = input("Por favor, digite seu nome para comerçarmos: ")
    email = input("Por favor, digite seu email para que possamos entrar em contato, caso for necessário: ")
    print(nome, "! Como posso lhe auxiliar hoje? ")
    
    while True: 
        #menu de opções
        pergunta = input(f"O que você gostaria de saber?{os.linesep}[1] - Gostaria de saber os filmes que estão em cartaz hoje?{os.linesep}[2] - Horários de hoje para os filmes{os.linesep}[3] - Valor do ingresso inteira ou meia entrada?{os.linesep}[4] - Interia!{os.linesep}[5] - Meia Entrada!{os.linesep}[6] - SAIR!{os.linesep}")

        #receber a resposta
        processar_resposta(pergunta, nome)
     


if __name__ == '__main__':
    start()
