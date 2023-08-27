while True:
    sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados Inválidos. Por favor, ', end='')
    else:
        if sexo == 'M':
            print('Sexo MASCULINO registrado com sucesso.')
            break
        elif sexo == 'F':
            print('Sexo FEMININO registrado com sucesso.')
            break
        else:
            print('Não era para ter chegado aqui.')    
  