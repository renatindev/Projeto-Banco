
#Funções

#Analisa se o usuário quer continuar usando o programa..
def ContinuaOperações():
         res = input("Deseja fazer mais operações(S/N)?\n")
         res = res.lower()
         if res == "sim" or res == "s" :
            print ("OK!\n")
         elif res == 'não' or res == 'n' or res == 'nao':
            print("OK! Volte Sempre!.")
            exit()
         else:
             print("Opção inválida. Voltando para o Menu...")

#Apresenta o programa e coleta o nome.
def Entrada():
        print("*****Bem-Vindo ao Banco Do Junior!*****\n")
        nome = input("Digite seu nome: ") 
        nome = nome.capitalize()
        return nome

#Apresenta o Menu, dá diversas opções ao usuário de operações bancarias.
def Menu():
        nome = Entrada()
        saldo,cont_S,cont_D,Soma_D,Soma_S = 0,0,0,0,0
        resposta = input(f"\nOlá {nome}, você deseja ver o Menu de operações?(S/N): ")
        resposta = resposta.lower()

        while resposta == "s" or resposta == "sim":

            print(f"\nEscolha uma das operações abaixo:\n")
            menu = int(input("Digite '1' para Saldo.\nDigite '2' para Saque.\nDigite '3' para Depósito.\nDigite '4' para Estatísticas.\nDigite '0' para fechar o programa.\n"))

            if menu == 1 :
                print(f"Seu saldo é: R$ {saldo}\n")
                ContinuaOperações()
                

            elif menu == 2 :
                saque = float(input("Saque:\nDigite qual valor você deseja sacar?.. Ou digite '0' para voltar para o Menu. "))
                if saque <= saldo and saque > 0:
                    saldo = saldo - saque
                    print(f"\nSaque de R${saque} efetuado com sucesso!!\n")
                    cont_S += 1
                    Soma_S += saque
                    ContinuaOperações()

                elif saque == 0:
                    print("OK, Redirecionando...") 
                else:
                    print("\nValor inválido ou Insuficiente!!!\n")

            elif menu == 3:
                deposito = float(input("Depósito:\nDigite o valor que você irá depositar:... Ou digite '0' para voltar para o Menu. "))
                if deposito > 0 :
                    saldo = deposito+saldo
                    print(f"\nDepósito de R${deposito} realizado com sucesso!!\n")
                    cont_D += 1
                    Soma_D += deposito
                    ContinuaOperações()

                elif deposito == 0:
                    print("OK, Redirecionando...")
                else:
                    print("\nValor inválido!!\n")

            elif menu == 4:
                print(f"Estatísticas:\n\nDepositos Realizados: {cont_D}\nSaques Realizados: {cont_S}\nSoma dos Depósitos: R${Soma_D}\nSoma dos Saques: R${Soma_S}\n")
                ContinuaOperações()

            elif menu == 0:
                print("OK! Volte Sempre!.")
                exit()

            else:
                print("\nOpção inválida \n!")

        print("OK. Volte Sempre!!...")

Menu()