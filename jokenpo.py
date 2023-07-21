import random
from time import sleep
import os

itens = ('Pedra', 'Papel', 'Tesoura')
vitoria = 0
derrota = 0
empate = 0
partidas = 0

nome = input('Digite seu nome: ')


while True:

    try:
        partidas += 1
        computador = random.randint(0, 2)

        print('[0] - Pedra')
        print('[1] - Papel')
        print('[2] - Tesoura')
        escolha_usuario = input('Escolha uma opção: ')
        escolha_usuario = int(escolha_usuario)

        if computador == 0: #Computador jogou pedra
            print('Pedra')
            sleep(1)
            print('Papel')
            sleep(1)
            print('Tesouraaa!!!\n')

            print('===' * 10)
            print(f'Computador: {itens[computador]}')
            print(f'{nome}: {itens[escolha_usuario]}')
            print('===' * 10)
            
            if escolha_usuario ==  0:
                print('Partida empatada.')
                empate += 1
            
            elif escolha_usuario == 1:
                print(f'{nome}: Ganhou!')
                vitoria += 1
        
            elif escolha_usuario == 2:
                print('Computador Ganhou!')
                derrota += 1
    
        elif computador == 1: #Computador jogou papel
            print('Pedra')
            sleep(1)
            print('Papel')
            sleep(1)
            print('Tesouraaa!!!\n')

            print('===' * 10)
            print(f'Computador: {itens[computador]}')
            print(f'{nome}: {itens[escolha_usuario]}')
            print('===' * 10)
            
            if escolha_usuario ==  0:
                print(f'Computador Ganhou!')
                derrota += 1
            
            elif escolha_usuario == 1:
                print('Partida Empatada.')
                empate += 1
        
            elif escolha_usuario == 2:
                print(f'{nome} Ganhou!')
                vitoria += 1
    
        elif computador == 2: #Computador jogou Tesoura
            print('Pedra')
            sleep(1)
            print('Papel')
            sleep(1)
            print('Tesouraaa!!!\n')

            print('===' * 10)
            print(f'Computador: {itens[computador]}')
            print(f'{nome}: {itens[escolha_usuario]}')
            print('===' * 10)
            
            if escolha_usuario ==  0:
                print(f'{nome}: Ganhou!')
                vitoria += 1
            
            elif escolha_usuario == 1:
                print('Computador Ganhou!')
                derrota += 1
        
            elif escolha_usuario == 2:
                print('Partida empatada.')
                empate += 1

        continuar = input('Deseja continuar a partida? [Sim] / [Nao]: ').lower()
        if continuar != 'sim':
            os.system('cls')
            print('===' * 12)
            print(' '  * 6,'Resumo da partida')
            print(f' Partidas: {partidas}')
            print(f' Vitórias: {vitoria}')
            print(f' Derrotas: {derrota}')
            print(f' Empate:   {empate}')
            print('===' * 12)
            break            

        else: 
            continue

    except(ValueError, IndexError):
        print('Opção escolhida é inválida.')
        continuar = input('Deseja continuar a partida? [Sim] / [Nao]: ').lower()
        if continuar != 'sim':
            os.system('cls')
            print('===' * 12)
            print(' '  * 6,'Resumo da partida')
            print(f' Vitorias: {vitoria}')
            print(f' Derrotas: {vitoria}')
            print(f' Empate:  {empate}') 
            print('===' * 12) 
            break      

        else: 
            continue
