import os
from time import sleep
import datetime


#printar o menu incial 
def menu():
    print()
    print("Banco FEI")
    print("1 - Novo cliente")
    print("2 - Apaga cliente")
    print("3 - Débito")
    print("4 - Depósito")
    print("5 - Extrato")
    print("6 - Transferência entre contas")
    print("7 - Simule um investimento")
    print("0 - Sair")

    escolha = int(input("\nEscolha sua opcao: "))
    #exercer a função 
    if escolha == 1:
        novo()
    elif escolha == 2:
        apaga()
    elif escolha == 3:
        debito()
    elif escolha == 4:
        deposito()
    elif escolha == 5:
        extrato()   
    elif escolha == 6:
        transferencia()
    elif escolha == 7:
        investimento()
    elif escolha == 0:
        sair()
    else: #caso um número que não está dentro das opções seja selecionado
        print("\n Digite uma opção válida \n")
        sleep(2)
        menu()

#definir as funçôes do menu 
    # funcao para novo cliente.
def novo():
    print()
    print("Novo cliente\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf)
    if x == False:
        nome = input("Nome: ")
        senha = input("Senha: ")
        tip = input("Digite o tipo de conta: 1-Comum 2-Plus. ")
        valor = float(input("Digite o valor inicial da conta: "))
        now = datetime.datetime.now()
        if tip=="1":
            tipo="comum"
        else:
            tipo="plus"
        arquivo = open("%s.txt"%cpf, "w") #cria um arquivo com o cpf do usuário
        arquivo.write("Nome: %s\nCPF: %s\n%s\nConta: %s\n" %(nome, cpf, senha, tipo)) #insere os dados pedidso acima dentro do arquivo cada dado em uma linha
        arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
        arquivo.write("   + %8.2f   Tarifa:     0.00   Saldo: %8.2f\n" %(valor, valor))
        arquivo.close()
        print("Conta cadastrada com sucesso.")
        sleep(2)
        menu() #retorna ao menu já que o usuário pode utilizar sua conta
    if x == True: #compara se não existe arquivo com o cpf cadastrado
        print("CPF em conta existente.") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode utilizar sua conta ou criar uma nova


    # funcao para apagar cliente.
def apaga():
    print()
    print("Apaga cliente\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    if x == True: #caso exista irá executar as ações abaixo
        senha = input("Senha: ") #pede a senha da conta
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        senhac = escrito[2].strip() #guarda a senha correta da conta
        arquivo.close()
        if senha == senhac: #compara se a senha é a mesma da conta          
            os.remove("%s.txt"%cpf) #apaga o arquivo do cpf 
            print("Confirmado") #confirma a ação
            sleep(2)
            menu() #retorna ao menu
        else:
            arquivo.close() #fecha o arquivo para poder executar qualquer nova ação em outros arquivos e no aberto também
            print("CPF ou senha incorretos") #caso a senha seja a errada ele notifica o usuário e retorna à função de cancelar pedido 
            sleep(2)
            menu()
    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Não há conta com esse CPF") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta


    # funcao para debito.
def debito():
    print()
    print("Débito\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    if x == True: #caso exista irá executar as ações abaixo
        senha = input("Senha: ") #pede a senha da conta
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        senhac = escrito[2].strip() #guarda a senha correta da conta
        arquivo.close()
        if senha == senhac: #compara se a senha é a mesma da conta          
            tipo = escrito[3].split()[-1]
            valor = int(input("Digite o valor a ser debitado: "))
            if tipo == "comum":
                tarifa = valor * 0.05
                saldo = float(escrito[-1].split()[-1]) - valor - tarifa
                if saldo>-1000:
                    now = datetime.datetime.now()
                    arquivo = open("%s.txt"%cpf, "a")
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   - %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    print("Confirmado") #confirma a ação
                    sleep(2)
                    menu() #retorna ao menu
                else:
                    print("Limite de saldo negativo excedido por R$ %.2f." %(saldo+1000))
                    print("Operação cancelada.")
                    sleep(2)
                    menu()
            else:
                tarifa = valor * 0.03
                saldo = float(escrito[-1].split()[-1]) - valor - tarifa
                if saldo<-5000:
                    print("Limite de saldo negativo excedido por R$ %.2f." %(saldo+1000))
                    print("Operação cancelada.")
                    sleep(2)
                    menu()
                else:
                    now = datetime.datetime.now()
                    arquivo = open("%s.txt"%cpf, "a")
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   - %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    print("Confirmado") #confirma a ação
                    sleep(2)
                    menu() #retorna ao menu
        else:
            arquivo.close() #fecha o arquivo para poder executar qualquer nova ação em outros arquivos e no aberto também
            print("CPF ou senha incorretos") #caso a senha seja a errada ele notifica o usuário e retorna à função de cancelar pedido 
            sleep(2)
            menu()
    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Não há conta com esse CPF") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta
 

    # funcao para deposito.
def deposito():
    print()
    print("Depósito\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    if x == True: #caso exista irá executar as ações abaixo
        valor = int(input("Digite o valor a ser depositado: "))
        tarifa = 0
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        arquivo.close()
        arquivo = open("%s.txt"%cpf, "a")
        now = datetime.datetime.now()
        saldo = float(escrito[-1].split()[-1]) + valor
        arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
        arquivo.write("   + %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
        arquivo.close()
        print("Confirmado") #confirma a ação
        sleep(2)
        menu() #retorna ao menu

    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Não há conta com esse CPF") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta


    # funcao para extrato.
def extrato():
    print()
    print("Extrato\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    if x == True: #caso exista irá executar as ações abaixo
        senha = input("Senha: ") #pede a senha da conta
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        senhac = escrito[2].strip() #guarda a senha correta da conta
        arquivo.close()
        if senha == senhac: #compara se a senha é a mesma da conta          
            print()
            print(escrito[0].strip())
            print(escrito[1].strip())
            for i in range(3, len(escrito)):
                print(escrito[i].strip())
            sleep(6)
            menu()
        else:
            arquivo.close() #fecha o arquivo para poder executar qualquer nova ação em outros arquivos e no aberto também
            print("CPF ou senha incorretos") #caso a senha seja a errada ele notifica o usuário e retorna à função de cancelar pedido 
            sleep(2)
            menu()
    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Não há conta com esse CPF") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta


    # funcao para transferencia.
def transferencia():
    print()
    print("Transferência entre contas\n")
    cpf = input("CPF da conta de origem: ")
    cpf2 = input("CPF da conta destino: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    y = os.path.exists("%s.txt"%cpf2)
    if x == True and y == True: #caso exista irá executar as ações abaixo
        senha = input("Senha da conta origem: ") #pede a senha da conta
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        senhac = escrito[2].strip() #guarda a senha correta da conta
        arquivo.close()
        if senha == senhac: #compara se a senha é a mesma da conta          
            tipo = escrito[3].split()[-1]
            valor = int(input("Digite o valor a ser transferido: "))
            if tipo == "comum":
                tarifa = valor * 0.05
                saldo = float(escrito[-1].split()[-1]) - valor - tarifa
                if saldo<-1000:
                    print("Limite de saldo negativo excedido por R$ %.2f." %(saldo+1000))
                    print("Operação cancelada.")
                    sleep(2)
                    menu()
                else:
                    now = datetime.datetime.now()
                    arquivo = open("%s.txt"%cpf, "a")
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   - %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    tarifa = 0
                    arquivo = open("%s.txt"%cpf2, "r")
                    escrito = arquivo.readlines()
                    arquivo.close()
                    arquivo = open("%s.txt"%cpf2, "a")
                    now = datetime.datetime.now()
                    saldo = float(escrito[-1].split()[-1]) + valor
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   + %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    print("Confirmado") #confirma a ação
                    sleep(2)
                    menu() #retorna ao menu
            else:
                tarifa = valor * 0.03
                saldo = float(escrito[-1].split()[-1]) - valor - tarifa
                if saldo<-5000:
                    print("Limite de saldo negativo excedido por R$ %.2f." %(saldo+1000))
                    print("Operação cancelada.")
                    sleep(2)
                    menu()
                else:
                    now = datetime.datetime.now()
                    arquivo = open("%s.txt"%cpf, "a")
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   - %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    tarifa = 0
                    arquivo = open("%s.txt"%cpf2, "r")
                    escrito = arquivo.readlines()
                    arquivo.close()
                    arquivo = open("%s.txt"%cpf2, "a")
                    now = datetime.datetime.now()
                    saldo = float(escrito[-1].split()[-1]) + valor
                    arquivo.write(now.strftime("Data: %d-%m-%Y %H:%M"))
                    arquivo.write("   + %8.2f   Tarifa: %8.2f   Saldo: %8.2f\n" %(valor, tarifa, saldo))
                    arquivo.close()
                    print("Confirmado") #confirma a ação
                    sleep(2)
                    menu() #retorna ao menu
        else:
            arquivo.close() #fecha o arquivo para poder executar qualquer nova ação em outros arquivos e no aberto também
            print("CPF ou senha incorretos") #caso a senha seja a errada ele notifica o usuário e retorna à função de cancelar pedido 
            sleep(2)
            menu()
    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Conta origem não existente") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta
    if y == False: #compara se não existe arquivo com o cpf cadastrado
        print("Conta destino não existente") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta


    # funcao para investimento.
def investimento():
    print()
    print("Simule um investimento:\n")
    cpf = input("CPF: ")
    x = os.path.exists("%s.txt"%cpf) #verifica se existe um arquivo com o cpf inserido
    if x == True: #caso exista irá executar as ações abaixo
        senha = input("Senha: ") #pede a senha da conta
        print()
        arquivo = open("%s.txt"%cpf, "r")
        escrito = arquivo.readlines()
        senhac = escrito[2].strip() #guarda a senha correta da conta
        arquivo.close()
        if senha == senhac: #compara se a senha é a mesma da conta
            opc = int(input("Selecione seu tipo de investimento:\n1-Baixo risco\n2-Médio risco\n3-Alto risco\n"))
            if opc==1:
                print("Baixo risco renderá 1.2% ao ano.")
                quant = int(input("Quantos % da sua conta deseja investir: "))
                tempo = int(input("Quantos meses pretende investir: "))
                arquivo = open("%s.txt"%cpf, "r")
                escrito = arquivo.readlines()
                arquivo.close()
                arquivo = open("%s.txt"%cpf, "a")
                saldo = float(escrito[-1].split()[-1])
                if saldo<0:
                    print("Saldo da conta negativo")
                    print("Não é possível fazer investimentos")
                    sleep(2)
                    menu()
                else:
                    rend = (saldo * (quant/100)) * ((1.2/100) * tempo) + (saldo * (quant/100))
                    print("Seu rendimento em %d meses será de R$%.2f" %(tempo, rend))
                    sleep(2)
                    menu()
            elif opc==2:
                print("Médio risco renderá 2.4% ao ano.")
                quant = int(input("Quantos % da sua conta deseja investir: "))
                tempo = int(input("Quantos meses pretende investir: "))
                arquivo = open("%s.txt"%cpf, "r")
                escrito = arquivo.readlines()
                arquivo.close()
                arquivo = open("%s.txt"%cpf, "a")
                saldo = float(escrito[-1].split()[-1])
                if saldo<0:
                    print("Saldo da conta negativo")
                    print("Não é possível fazer investimentos")
                    sleep(2)
                    menu()
                else:
                    rend = (saldo * (quant/100)) * ((2.4/100) * tempo) + (saldo * (quant/100))
                    print("Seu rendimento em %d meses será de R$%.2f" %(tempo, rend))
                    sleep(2)
                    menu()
            elif opc==2:
                print("Alto risco renderá 3.6% ao ano.")
                quant = int(input("Quantos % da sua conta deseja investir: "))
                tempo = int(input("Quantos meses pretende investir: "))
                arquivo = open("%s.txt"%cpf, "r")
                escrito = arquivo.readlines()
                arquivo.close()
                arquivo = open("%s.txt"%cpf, "a")
                saldo = float(escrito[-1].split()[-1])
                if saldo<0:
                    print("Saldo da conta negativo")
                    print("Não é possível fazer investimentos")
                    sleep(2)
                    menu()
                else:
                    rend = (saldo * (quant/100)) * ((3.6/100) * tempo) + (saldo * (quant/100))
                    print("Seu rendimento em %d meses será de R$%.2f" %(tempo, rend))
                    sleep(2)
                    menu()
            else:
                print("Investiemnto não existente")
                sleep(2)
                investimento()
        else:
            arquivo.close() #fecha o arquivo para poder executar qualquer nova ação em outros arquivos e no aberto também
            print("CPF ou senha incorretos") #caso a senha seja a errada ele notifica o usuário e retorna à função de cancelar pedido 
            sleep(2)
            menu()
    if x == False: #compara se não existe arquivo com o cpf cadastrado
        print("Não há conta com esse CPF") #notifica o usuário
        sleep(2)
        menu() #retorna ao menu já que o usuário pode então querer criar uma conta


    # funcao para sair.
def sair():
    print()
    print("Obrigado pela preferência ao Banco FEI\n ")

menu()
