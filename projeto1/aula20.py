primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor.isnumeric() and segundo_valor.isnumeric():
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)
    if primeiro_valor > segundo_valor:
        print(f'O primeiro valor "{primeiro_valor}" é maior que o segundo valor "{segundo_valor}"')
    elif primeiro_valor < segundo_valor:
        print(f'O segundo valor "{segundo_valor}" é maior que o primeiro valor "{primeiro_valor}"')
    else:
        print(f'Os dois valores são iguais "{primeiro_valor}" e "{segundo_valor}"')
else:
    print('Você não digitou um número')