import random
import os
import time

vitoria = 0
derrota = 0
empate = 0

while True:
    os.system('cls')
    dado_computador = random.randint(1, 6)
    dado_jogador = input('Escolha o valor de 1 a 6: ')

    print('Jogando os dados em:')
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('Jáá...')
    
    try:
        dado_jogador = int(dado_jogador)
        if dado_jogador < 0 and dado_jogador > 6:
            print('Você escolheu uma opção maior ou menor que a permitida.')
            continue
        else:
            if dado_jogador > dado_computador:
                print('Você venceu!')
                vitoria += 1
                jogar_novamente = input('Deseja jogar novamente? [Sim/Nao]: ').lower() .strip()[0]
                if jogar_novamente == 's':
                    continue
                else:
                    break
            elif dado_jogador < dado_computador:
                print('Computador venceu!')
                derrota += 1
                jogar_novamente = input('Deseja jogar novamente? [Sim/Nao]: ').lower() .strip()[0]
                if jogar_novamente == 's':
                    continue
                else:
                    break
            else:
                print('Empate!')
                jogar_novamente = input('Deseja jogar novamente? [Sim/Nao]: ').lower().strip()[0]
                empate += 1
                if jogar_novamente == 's':
                    continue
                else:
                    break

    except:
        print('Você não digitou o que foi pedido,\npor favor leia atentamente e digite o que está sendo pedido.\nGrato!!!')
        jogar_novamente = input('Deseja jogar novamente? [Sim/Nao]: ').lower() .strip()[0]
        if jogar_novamente == 's':
            continue
        else:
            os.system('cls')
            break
os.system('cls')
print('Ate Mais!!!')
print('Resumo da partida')
print(f'Vitoria: {vitoria}')
print(f'Derrota: {derrota}')
print(f'Empate: {empate}')