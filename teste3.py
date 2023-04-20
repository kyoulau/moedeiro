#Variaveis
usuario = ""
cedulas = ""
moedas = ""
controle_de_estoque = ""
moeda_quantidade_005 = 0
moeda_quantidade_10 = 200
moeda_quantidade_25 = 200
moeda_quantidade_50 = 100
moeda_quantidade_1 = 100
cedula_quantidade_2 = 50
cedula_quantidade_5 = 50
cedula_quantidade_10 = 50
cedula_quantidade_20 = 0
cedula_quantidade_50 = 0
pagamento = 0
quantidade_coca = 40

contador_moeda_quantidade_005 = 0
contador_moeda_quantidade_10 = 0
contador_moeda_quantidade_25 = 0
contador_moeda_quantidade_50 = 0
contador_moeda_quantidade_1 = 0
contador_cedula_quantidade_2 = 0
contador_cedula_quantidade_5 = 0
contador_cedula_quantidade_10 = 0
contador_cedula_quantidade_20 = 0
contador_cedula_quantidade_50 = 0

print("================================================================================================================")
print("                                       Máquina de Refrigerante                                                  ")
print("================================================================================================================")
print("                                       Selecione seu Perfil                                                     ")
print("================================================================================================================")

while usuario != "0":
    usuario = int(input("1 - Administrador\n2 - Consumidor\nDigite o número do seu usuário:"))

    if usuario == 1:
        senha = str(input("Insira a senha:"))
        if senha == "administrador321":
            print("================================================================================================================")
            print("                                       ACESSO PERMITIDO                                                         ")
            print("================================================================================================================\n")
            print("QUANTIDADE DE MOEDAS\n"
            "R$ 0,05 =" ,moeda_quantidade_005,
            "\nR$ 0,10 =" ,moeda_quantidade_10,
            "\nR$ 0,25 =" ,moeda_quantidade_25,
            "\nR$ 0.50 =",moeda_quantidade_50,
            "\nQUANTIDADE DE CÉDULAS"
            "\nR$ 1,00 =" ,moeda_quantidade_1,
            "\nR$ 2,00 =" ,cedula_quantidade_2,
            "\nR$ 5,00 =" ,cedula_quantidade_5,
            "\nR$ 10,00=" ,cedula_quantidade_10,
            "\nR$ 20,00 =" ,cedula_quantidade_20,
            "\nR$ 50,00 =",cedula_quantidade_50)

            print("Unidades Disponiveis na Máquina = ", quantidade_coca)

            while controle_de_estoque !="0":
                controle_de_estoque = int(input("1 - Adicionar Bebida\n2 - Retirar Bebida\n3 - Voltar para a página de usuário\nDigite a o número da ação que você deseja realizar:"))
                if controle_de_estoque ==1:
                    adicao_bebida = int(input("Digite o número de bebidas que você quer adicionar:"))
                    quantidade_coca=quantidade_coca+adicao_bebida
                elif controle_de_estoque==2:
                    retirar_bebida = int(input("Digite o número de bebidas que você quer retirar:"))
                    if retirar_bebida>quantidade_coca:
                        print("NÃO TEM COCA O SUFICIENTE!")
                    else:
                        quantidade_coca=quantidade_coca-retirar_bebida
                elif controle_de_estoque==3: 
                    break
                else:
                    print("Digite apenas as opções válidas.")
        else:
            print("Senha incorreta. Tente novamente")

    elif usuario == 2:
        if quantidade_coca<=0:
             print("NÃO TEM BEBIDA")
        else:
            print("================================================================================================================")
            print("                                             OPÇÕES DE BEBIDA                                                   ")
            print("================================================================================================================")
            print("Coca-cola: R$6,00 Reais")

            while cedulas != "0":
                print("========== Pagamento Cédulas ==========")
                cedulas = float(input("1 - R$ 2,00 \n2 - R$ 5,00 \n3 - R$ 10,00 \n4 - R$ 20,00 \n5 - R$ 50,00 \n6 - Pagamento em Moedas\n Selecione a opção do valor da cédula que você deseja inserir: "))
                if cedulas == 1:
                    contador_cedula_quantidade_2 += 1
                    cedula_quantidade_2 += contador_cedula_quantidade_2
                    pagamento = pagamento + 2
                elif cedulas == 2:
                    contador_cedula_quantidade_5 += 1
                    cedula_quantidade_5 += contador_cedula_quantidade_5
                    pagamento = pagamento + 5
                elif cedulas == 3:
                    contador_cedula_quantidade_10 += 1
                    cedula_quantidade_10 += contador_cedula_quantidade_10
                    pagamento = pagamento + 10
                elif cedulas == 4:
                    contador_cedula_quantidade_20+= 1
                    cedula_quantidade_20 += contador_cedula_quantidade_20
                    pagamento = pagamento + 20
                elif cedulas == 5:
                    contador_cedula_quantidade_50 += 1
                    cedula_quantidade_50 += contador_cedula_quantidade_50
                    pagamento = pagamento + 50
                    
                elif cedulas == 6:
                    break
                else:
                    print("Digite apenas as opções existentes.")

            while moedas != "0":
                print("========== Pagamento Moedas ==========")
                moedas = float(input(
                    "1 - 0.05 centavos\n2 - 0.10 centavos\n3 - 0.25 centavos\n4 - 0.50 centavos \n5 - 1.0 real\n6 - finalizar compra\nDigite o tipo de moeda que deseja inserir:"))
                if moedas == 1:
                    moeda_quantidade_005 += 1
                    moeda_quantidade_005+=contador_moeda_quantidade_005
                    pagamento = pagamento + 0.05

                elif moedas == 2:
                    moeda_quantidade_10 += 1
                    moeda_quantidade_10+=contador_moeda_quantidade_10
                    pagamento = pagamento + 0.10
                elif moedas == 3:
                    moeda_quantidade_25 += 1
                    moeda_quantidade_25+=contador_moeda_quantidade_25
                    pagamento = pagamento + 0.25
                elif moedas == 4:
                    moeda_quantidade_50 += 1
                    moeda_quantidade_50+=contador_moeda_quantidade_50
                    pagamento = pagamento + 0.50
                elif moedas == 5:
                    moeda_quantidade_1 += 1
                    moeda_quantidade_1+=contador_moeda_quantidade_1
                    pagamento = pagamento + 1.0
                elif moedas == 6:
                    break
                else:
                    print("Digite apenas as opções existentes.")
        if pagamento < 6:
            print("Pagamento Indefinido, faltam", (6 - pagamento), "reais\nDevolver dinheiro")
            cedula_quantidade_2-=contador_cedula_quantidade_2
            cedula_quantidade_5-=contador_cedula_quantidade_5
            cedula_quantidade_10-=contador_cedula_quantidade_10
            cedula_quantidade_20-=contador_cedula_quantidade_20
            cedula_quantidade_50-=contador_cedula_quantidade_50
            moeda_quantidade_005-=contador_moeda_quantidade_005
            moeda_quantidade_10-=contador_moeda_quantidade_10
            moeda_quantidade_25-=contador_moeda_quantidade_25
            moeda_quantidade_50-=contador_moeda_quantidade_50
            moeda_quantidade_1-=contador_moeda_quantidade_1

        else:
                    valor = 6
                    troco = pagamento - valor

                    if cedula_quantidade_50>troco//50:
                        print("Quantidade de notas de 50 reais: ",troco//50)
                        cedula_quantidade_50 = cedula_quantidade_50-(troco//50)
                        troco=troco%50

                        if cedula_quantidade_20>troco//20:
                            print("Quantidade de notas de 20 reais: ",troco//20)
                            cedula_quantidade_20 = cedula_quantidade_20-(troco//20)
                            troco=troco%20     
                            
                            if cedula_quantidade_10>troco//10:
                                print("Quantidade de notas de 10 reais: ",troco//10)
                                cedula_quantidade_10 = cedula_quantidade_10-(troco//10)
                                troco=troco%10
                                
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5

                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                            else:
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5

                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                        else:
                            if cedula_quantidade_10>troco//10:
                                print("Quantidade de notas de 10 reais: ",troco//10)
                                cedula_quantidade_10 = cedula_quantidade_10-(troco//10)
                                troco=troco%10
                                
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                            else:
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                    else:
                        if cedula_quantidade_20>troco//20:
                            print("Quantidade de notas de 20 reais: ",troco//20)
                            cedula_quantidade_20 = cedula_quantidade_20-(troco//20)
                            troco=troco%20     
                            
                            if cedula_quantidade_10>troco//10:
                                print("Quantidade de notas de 10 reais: ",troco//10)
                                cedula_quantidade_10 = cedula_quantidade_10-(troco//10)
                                troco=troco%10
                                
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5

                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                            else:
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5

                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2

                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1

                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50

                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25

                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10

                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)

                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")

                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                        else:
                            if cedula_quantidade_10>troco//10:
                                print("Quantidade de notas de 10 reais: ",troco//10)
                                cedula_quantidade_10 = cedula_quantidade_10-(troco//10)
                                troco=troco%10
                                
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                            else:
                                if cedula_quantidade_5>troco//5:
                                    print("Quantidade de notas de 5 reais: ",troco//5)
                                    cedula_quantidade_5 = cedula_quantidade_5-(troco//5)
                                    troco=troco%5
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                else:
                                    if cedula_quantidade_2>troco//2:
                                        print("Quantidade de notas de 2 reais: ",troco//2)
                                        cedula_quantidade_2 = cedula_quantidade_2-(troco//2)
                                        troco=troco%2
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                    else:
                                        if moeda_quantidade_1>troco//1:
                                            print("Quantidade de moedas de 1 real: ",troco//1)
                                            moeda_quantidade_1 = moeda_quantidade_1-(troco//1)
                                            troco=troco%1
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                        else:
                                            if moeda_quantidade_50>troco//0.50:
                                                print("Quantidade de moedas de 50 centavos: ",troco//0.50)
                                                moeda_quantidade_50 = moeda_quantidade_50-(troco//0.50)
                                                troco=troco%0.50
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                            else:
                                                if moeda_quantidade_25>troco//0.25:
                                                    print("Quantidade de moedas de 25 centavos: ",troco//0.25)
                                                    moeda_quantidade_25 = moeda_quantidade_25-(troco//0.25)
                                                    troco=troco%0.25
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                else:
                                                    if moeda_quantidade_10>troco//0.10:
                                                        print("Quantidade de moedas de 10 centavos: ",troco//0.10)
                                                        moeda_quantidade_10 = moeda_quantidade_10-(troco//0.10)
                                                        troco=troco%0.10
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                    
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                    else:
                                                        if moeda_quantidade_005>troco//0.05:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro")
                                                            else:
                                                                print("Quantidade de moedas de 5 centavos: ",troco//0.05)
                                                                moeda_quantidade_005 = moeda_quantidade_005-(troco//0.05)
                                                                                                            
                                                        else:
                                                            if troco%0.05 !=0:
                                                                print("Não há troco suficiente na máquina. devolver dinheiro") 

                    print("Liberar bebida")
                    quantidade_coca=quantidade_coca-1
    else:
        print(" Insira opções válidas!")
