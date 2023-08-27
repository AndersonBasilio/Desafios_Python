valores = []

for contador in range(1, 6):
    valores.append(int(input(f'Informe o {contador}º valor: ')))

print(f'\nValores digitados foram {valores}')
menor = min(valores)
maior = max(valores)

print(f'O maior valor digitado foi {maior} na posição ', end='')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao + 1}...', end='')

print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao + 1}...', end='')

    
