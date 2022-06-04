acumulador = 0
print('Bem vindo a Loja da Aline Carla Gomes')
print(20*'*'+'Cardápio'+20*'*')
print('| Código |          Descrição        | Valor |')
print('|   100  |       Cachorro Quente     |  9,00 |')
print('|   101  |   Cachorro quente duplo   | 11,00 |')
print('|   102  |           X-Egg           | 12,00 |')
print('|   103  |         X-Salada          | 12,00 |')
print('|   104  |           X-Bacon         | 14,00 |')
print('|   105  |           X-Tudo          | 17,00 |')
print('|   200  |     Refrigerante Lata     |  5,00 |')
print('|   201  |        Chá Gelado         |  4,00 |')
while True:
    codigo = input('Entre com o código desejado: ')
    if codigo == '100':
        print('Voce pediu um cachorro quente no valor de R$ 9,00')
        acumulador = acumulador + 9
    elif codigo == '101':
        print('Voce pediu um cachorro quente duplo no valor de R$ 11,00')
        acumulador = acumulador + 11
    elif codigo == '102':
        print('Voce pediu um x-egg no valor de R$ 12,00')
        acumulador = acumulador + 12
    elif codigo == '103':
        print('Voce pediu um x-salada no valor de R$ 13,00')
        acumulador = acumulador + 12
    elif codigo == '104':
        print('Voce pediu um x-bacon no valor de R$ 14,00')
        acumulador = acumulador + 14
    elif codigo == '105':
        print('Voce pediu um x-tudo no valor de R$ 17,00')
        acumulador = acumulador + 17
    elif codigo == '200':
        print('Voce pediu um refrigerante lata no valor de R$ 5,00')
        acumulador = acumulador + 5
    elif codigo == '201':
        print('Voce pediu um chá gelado no valor de R$ 4,00')
        acumulador = acumulador + 4
    else:
        print('Opção inválida')
        continue

    resposta = input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não ')
    if resposta == '1':
        continue
    else:
        print('O total a ser pago é: R$ {:.2f}'.format(acumulador))
        break









