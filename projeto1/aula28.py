nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade.isnumeric():
    idade = int(idade)
    print (f'Olá {nome}, você tem {idade} anos')
    print (f'Seu nome tem {len(nome)} letras')
    print (f'Seu nome invertido é {nome[::-1]}')
    print (f'Seu nome contém espaço" "? {" " in nome}')
    print (f'Seu nome contém "a" ou "A"? {"a" in nome or "A" in nome}')
    print (f'A primeira letra do seu nome é: {nome[0]}')
    print (f'A última letra do seu nome é: {nome[-1]}')

else:
    print('Você não digitou um nome ou uma idade válida')