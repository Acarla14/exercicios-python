def dimensoesObjeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto em cm: '))
            comprimento = float(input('Digite o comprimento do objeto em cm: '))
            largura = float(input('Digite a largura do objeto em cm: '))

            volume = altura*comprimento*largura
            print('O volume do objeto em cm é: {}'. format(volume))

            if volume <= 1000:
                return 10
            elif volume <= 1000 or volume < 10000:
                return 20
            elif volume <= 10001 or volume < 30000:
                return 30
            elif volume <= 30001 or volume < 100000:
                return 50
            elif volume > 100000:
                print('Não aceitamos objetos com dimensões tão grandes', volume)
                print('Entre com dimensões desejadas novamente')
                continue
        except: 
            print('Valor inválido! Aceitamos somente números')
            continue

def pesoObjeto():
    while True:
        try:
            pesoO = float(input('Informe o peso do objeto em KG: '))
            if pesoO <= 0.1:
                return 1
            elif 0.11 < pesoO <=1:
                return 1.5
            elif 1.10 < pesoO <= 10:
                return 2
            elif 10.1 < pesoO <= 30:
                return 3
            elif pesoO > 30:
                print('Não aceitamos objetos tão pesados. Tente novamente')
                continue
        except:
            print('Valor inválido. Tente novamente')
            continue

def rotaObjeto():
    while True:
        rotaO = input('Escolha a rota desejada: \n RS - De Rio de Janeiro até São Paulo \n SR - De São Paulo até Rio de Janeiro'
                      ' \n BS - De Brasília até São Paulo\n SB - De São Paulo até Brasília\n BR - De Brasília até Rio de Janeiro'
                      '\nRB - Rio de Janeiro até Brasília\n')
        if rotaO == 'RS':
            return 1
        if rotaO == 'SR':
            return 1
        if rotaO == 'BS':
            return 1.2
        if rotaO == 'SB':
            return 1.2
        if rotaO == 'BR':
            return 1.5
        if rotaO == 'RB':
            return 1.5
        else:
            print('Rota inválida. Tente novamente')
            continue

print('Bem vindo a companhia de logística Aline Carla Gomes')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes*peso*rota
print('O valor total é de R$ {} (dimensões: {} * peso: {} * rota: {})'. format(total,dimensoes,peso,rota))


