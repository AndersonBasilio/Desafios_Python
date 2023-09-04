from random import randint
import os

while True:

    respostas = [
        'Não', 'Sim', 'Talvez', 'Quem sabe', 'Acho que sim',
        'Com certeza', 'Você que sabe',
    ]
    pergunta = str(input('Faça uma pergunta: '))
    if len(pergunta) > 7:
        computador_escolheu = randint(0, 6) 
        print(respostas[computador_escolheu])
    else:
        print(f'Não reconhcia a pergunta, pois é muito curta ou você digitou algo errado.')
        
    continuar = input('Deseja continuar: [Sim/Não] ').lower()
    if continuar == 'sim':
        continue
    else:
        os.system('cls')  
        print('Obrigado por participar.')
        print('Volte sempre!!!')  
        break