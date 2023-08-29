import os
lista = []
lista_par = []
lista_impar = []

while True:
    try:
        numero = int(input('Digite um número: '))
        lista.append(numero)
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)

        continuar = input('Deseja continuar? [Sim/Não] ').lower()
        if continuar != 'sim':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            lista.sort()
            print(f'Lista completa {lista}')
            print(f'Lista com numeros impares {lista_impar}')
            print(f'Lista com numero pares {lista_par}')
            break  

    except (ValueError):
        print('Por favor digite o que foi pedido.')
        break