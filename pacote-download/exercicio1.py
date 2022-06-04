print ('Seja bem vindo a loja da Aline Carla Gomes')
valorProduto = float(input('Insira o valor unitário do produto: '))
qtd = int(input('Insira a quantidade desejada: '))
subtotal = valorProduto*qtd
if qtd > 0 and qtd <= 9:
    valorFinal = subtotal
elif qtd >=10 and qtd <= 99:
    valorFinal = subtotal - (subtotal * 0.05)
elif qtd>=100 and qtd <=999:
    valorFinal = subtotal - (subtotal * 0.10)
else:
    valorFinal = subtotal - (subtotal * 0.15)
print ('O valor total sem desconto é: R$ {:.2f}'.format(subtotal))
print ('O valor total com desconto é: R$ {:.2f}'.format(valorFinal))






