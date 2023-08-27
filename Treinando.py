print('LOJAS MERCURY CENTER')

opcoes = (
    'À vista Dinheiro / Cheque: 10% de desconto',
    'À vista no cartão: 5% de desconto',
    '2x no Cartão: Preço Normal',
    '3x no Cartao: 20% de juros'
)

try:
    preco = input('Informe qual foi o preço da compra: R$')
    preco = float(preco)

    print('\n[0] - À vista Dinheiro / Cheque: 10% de desconto.')
    print('[1] - À vista no cartão: 5% de desconto.')
    print('[2] - 2x no Cartão: Preço Normal')
    print('[3] - 3x no Cartao: 20% de juros')

    forma_pagamento = input('Qual será a forma de pagamento: ')
    forma_pagamento = int(forma_pagamento)

    

    if forma_pagamento == 0:
        print('Forma de pagamento escolhida é ', opcoes[forma_pagamento])
        desconto = (preco * 10) / 100
        print(f'Valor total com desconto: {preco - desconto}')
    
    elif forma_pagamento == 1:
        print('Forma de pagamento escolhida é ', opcoes[forma_pagamento])
        desconto = (preco * 5) / 100
        print(f'Valor total com desconto {preco -  desconto}')
    
    elif forma_pagamento == 2:
        print('Forma de pagamento escolhida é ', opcoes[forma_pagamento])
        parcela = preco / 2
        print(f'Valor a ser pago será 2x de {parcela}')

    elif forma_pagamento == 3:
        print('Forma de pagamento escolhida é ', opcoes[forma_pagamento])
        juros = (preco * 20) / 100
        print(f'Valor total com juros: {preco + juros}')
        print(f'3x {(preco + juros) / 3}')
    
   
except ValueError:
    print('Informação inválida')

