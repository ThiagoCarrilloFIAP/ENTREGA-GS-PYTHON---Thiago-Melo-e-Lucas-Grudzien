resp = 1
lista_cadastros = []

while (resp != 0):
    print("Bem vindo ao Programa de Tecnologia e Prevenção no SUS:")
    print("1- Conheça o programa e nossa ideia")
    print("2- Entenda nossa motivação")
    print("3- Confira se você pode se beneficiar com o programa")
    print("4- Faça um pré-cadastro")
    print("5- Encerrar programa")
    opcao = int(input("Digite a opção desejada (1-5): "))
    match opcao:
        case 1:
            print(" A solução proposta visa enfrentar o desafio do uso inadequado do SUS, priorizando a medicina preventiva para otimizar o maior sistema de saúde público universal e gratuito do mundo. "
                  "\n Um aplicativo educativo incentiva a adesão a consultas preventivas, recompensando os pacientes. \nIntegrado a um componente de análise de dados, o projeto busca alocar recursos de maneira eficiente,"
                  "\n considerando o retorno econômico superior da prevenção.")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))

        case 2:
            print("O SUS, como o maior sistema de saúde público universal e gratuito do mundo, enfrenta constantes pressões devido à demanda crescente e limitações orçamentárias. "
                  "\nA motivação reside na busca por uma solução inovadora que não apenas promova a conscientização sobre a importância da prevenção em saúde, mas também otimize a alocação de recursos, "
                  "\ncontribuindo assim para a sustentabilidade financeira a longo prazo do SUS. "
                  "\nEm resumo, a motivação para criar o programa é impulsionada pela necessidade de superar desafios financeiros, aproveitando a eficácia comprovada da medicina preventiva e adotando abordagens modernas, "
                  "\n como a tecnologia de aplicativos e análise de dados, para melhorar a eficiência operacional do sistema de saúde.")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))
        case 3:
            print("A abrangência do projeto se estende a diferentes grupos demográficos, visando a promoção da saúde e o enfrentamento dos desafios específicos enfrentados por diferentes faixas etárias."
            "\nEntre os principais beneficiários, destacam-se crianças até 12 anos, idosos e gestantes, para os quais o aplicativo educativo e de lembretes apresenta soluções adaptadas às necessidades específicas "
            "de cada grupo.")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))
        case 4:
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            telefone = int(input("Digite o seu telefone: "))
            idade = int(input("Digite a sua idade: "))
            genero = input("Informe seu gênero (Feminino, Masculino ou Outros): ")
            lista_cadastros.append({"Nome": nome, "Email": email, "Telefone": telefone, "Idade" : idade, "Gênero" : genero})
            print(lista_cadastros)
            print("\nPré-cadastro realizado com sucesso!")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))
        case 5:
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))
            break
        case _:
            print("\nOpção inválida! Favor escolher uma opção entre 1-6.\n")
