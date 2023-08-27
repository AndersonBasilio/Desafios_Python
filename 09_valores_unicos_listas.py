valores = []
valores_duplicados = []

while True:
    try:
        numeros = int(input('Digite um valor: '))
        if numeros  not in valores:
            valores.append(numeros)
            print('Valor adicionado com sucesso...')
        else:
            valores_duplicados.append(numeros)
            print('Valor duplicado! Não vou adicionar.')
        continuar = input('Deseja continuar? [Sim/ Nao] ').lower()
        if continuar != 'sim':
            valores.sort()
            print(valores)
            print(f'Valores duplicados que foram digitados: {valores_duplicados}')
            break
        
    except (ValueError):
        print('Você não digitou números.')
        continuar = input('Deseja continuar? [Sim/ Nao] ').lower()
        if continuar != 'sim':
            break
