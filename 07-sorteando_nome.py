import random
lista = []

sorteado = random.randint(0, 3)
for contador in range(4):
    lista.append(input(f'{contador + 1}º nome: '))

print(lista)


print(f'O nome sorteado foi... {lista[sorteado]}')


