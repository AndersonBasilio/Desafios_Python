import os
import random

tentativa = 0
numero_para_tentar_acertar = random.randint(1, 100)

print('===' * 12)
print(' ' * 6, 'Bem-Vindo ao Jogo ')
print(' ' * 3, 'Tente acertar o numero ...')
print('===' * 12)
while True:

    tentativa +=  1
    try:
        chute = input('Tente acertar o numero: ')
        chute = int(chute)
        
        if  chute == numero_para_tentar_acertar:
            os.system('cls')
            print(f'Parabéns!! Você acertou o número é {numero_para_tentar_acertar}.') 
            print('Obrigado por participar!')
            print(f'Foram {tentativa} tentativas.\n')
            break
        elif chute > numero_para_tentar_acertar:
            print('Seu chute foi alto, digite um número menor.')
            continue
        else:
            print('Seu chute foi baixo, digite um número maior.')
            continue
    
    except:
        print('Você não digitou um número inteiro, por favor digite um numero inteiro.')
        
        resposta = input('Deseja continuar? ')
        if resposta != 'sim':
            break