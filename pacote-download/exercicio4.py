listaPecas = []

def cadastrarPeca(codigo):
    print('Voce selecionou a opção CADASTRAR PEÇAS')
    print('O código da peça é: {:03d}'.format(codigo))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    valor = float(input('Digite o valor da peça: '))
    dicionarioPeca= {'codigo': codigo,
                     'nome': nome,
                     'fabricante': fabricante,
                     'valor': valor}
    listaPecas.append(dicionarioPeca.copy())

def consultarPeca():
    while True:
        try:
           print('Voce selecionou a opção CONSULTAR PEÇAS')
           opcao = int(input('Escolha com a opção desejada: \n'
                             '1-Consultar todas as peças\n'
                             '2-Consultar peças por códigos\n'
                             '3-Consultar peças por fabricante\n'
                             '4-Retornar'))
           if opcao == 1:
               print('Voce escolheu consultar TODOS')
               for peca in listaPecas:
                   for key, value in peca.items():
                       print('{} : {}' .format(key,value))
           elif opcao ==2:
               print('Voce escolheu consultar CODIGOS')
               entrada = int(input('Digite o codigo: '))
               for peca in listaPecas:
                   if(peca['codigo'] == entrada):
                       for key, value in peca.items():
                           print('{} : {}'.format(key, value))
           elif opcao ==3:
               print('Voce escolheu consultar por FABRICANTE')
               entrada = input('Digite o fabricante: ')
               for peca in listaPecas:
                   if (peca['fabricante'] == entrada):
                       for key, value in peca.items():
                           print('{} : {}'.format(key, value))
           elif opcao ==4:
               break
        except:
            print('Dígito inválido. Tente novamente')

def removerPeca():
    print('Voce selecionou a opção REMOVER PEÇAS')
    entrada = int(input('Digite o codigo a ser removido: '))
    for peca in listaPecas:
        if (peca['codigo'] == entrada):
            listaPecas.remove(peca)

print('Bem Vindo ao controle de estoque da bicicletaria da Aline Carla Gomes')
codPeca = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1-Cadastrar peças \n2-Consultar peças \n3-Remover peças\n4-Sair '))
        if opcao == 1:
            codPeca = codPeca+1
            cadastrarPeca(codPeca)
        elif opcao ==2:
            consultarPeca()
        elif opcao ==3:
            removerPeca()
        elif opcao == 4:
            break
        else:
            print('Dígito inválido. Tente novamente')
    except:
        print('Dígito inválido. Tente novamente')


