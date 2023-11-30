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
            print("")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))

        case 2:
            print("")
            resp = int(input("Deseja continuar? (1-SIM / 0-NÃO)  "))
        case 3:
            print("")
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
