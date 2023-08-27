import os
os.system('cls')
# Pedir um numero entre 0 e 20 para o usuário

# Tratar o numero para evitar erros

# Se for maior que vinte repetir

# lista de numeros
lista_de_numeros = (
    'Zero',
    'Um',
    'Dois',
    'Três',
    'Quatro',
    'Cinco',
    'Seis', 
    'Sete', 
    'Oito',
    'Nove', 
    'Dez', 
    'Onze',
    'Doze',
    'Treze',
    'Catorze',
    'Quinze', 
    'Dezesseis',
    'Dezessete',
    'Dezoito',
    'Dezenove',
    'Vinte',
)

while True:
    # Pedir um numero entre 0 e 20 para o usuário
    numero_usuario = input('Digite um número entre 0 a 20: ')

    try:
        numero_usuario = int(numero_usuario)

        if 0 <= numero_usuario <= 20:
            os.system('cls')
            print(f'O número informado por extenso é {lista_de_numeros[numero_usuario]}.')
            break  
        print('Tente Novamente! ', end='')

    except (ValueError):
        os.system('cls')
        print('Por favor, digite o que foi pedido.')
        continue
