import os
import random

os.system('cls')

vitoria = 0
derrota = 0
while True:

    print('**' * 12)
    print('  JOGO DO PAR OU IMPAR')
    print('**' * 12)
    try:

        numero_jogador = input('Digite um número: ')
        numero_jogador = int(numero_jogador)
        computador = random.randint(0, 10)
    

        if numero_jogador > 10:
            os.system('cls')
            print('Número escolhido foi maior que o permitido.')
            
        else:

            computador = random.randint(0, 10)
            jogador_par_ou_impar = input('"Par" ou "Impar"? ').lower()

            if (jogador_par_ou_impar != 'par') and (jogador_par_ou_impar != 'impar'):
                print('Opção desconhecida, verifique e tente novamente!')
                resposta = input('Você deseja continuar? [Sim]/[Não]: ').lower()
                if resposta == 'sim' and 's':
                    continue
                else:
                    break
        
            soma_computador_jogador = computador + numero_jogador
            
            print('---' * 10)
            print(f'\nComputador escolheu: {computador}')
            print(f'Você escolheu: {numero_jogador}')
            print(f'Total: {soma_computador_jogador}.')
            print('---' * 10)
        
            if jogador_par_ou_impar == 'par':
                if soma_computador_jogador % 2 == 0:
                    print('\n  Você venceu!\n')
                    vitoria += 1
                else:
                    print('\n  Você perdeu!\n')
                    derrota += 1

                print('---' * 10)
                resposta = input('Você deseja continuar? [Sim]/[Não]: ').lower()
                if resposta == 'sim' and 's':
                    continue
                else:
                    break

            elif jogador_par_ou_impar == 'impar':
                if soma_computador_jogador % 2 != 0:
                    print('\n  Você venceu!  \n')
                    vitoria += 1
                else:
                    print('\n  Você perdeu!  \n')  
                    derrota += 1

                print('---' * 10)
                resposta = input('Você deseja continuar? [Sim]/[Não]: ').lower()
                if resposta == 'sim' and 's':
                    continue
                else:
                    break
    except:
        os.system('cls')
        print('Você não digitou o que foi pedido, por favor digite corretamente.')
        
        resposta = input('Você deseja continuar? [Sim]/[Não]: ').lower()
        if resposta == 'sim' and 's':
            continue
        else:
            break
        
os.system('cls')
print('==' * 12)
print('    RESULTADO FINAL  ')
print('--' * 12)
print(f'Vitórias: {vitoria}')
print(f'Derrotas: {derrota}')
print('==' * 12)
