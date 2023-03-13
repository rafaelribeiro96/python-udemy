entrada = input('VOcê quer "entrar" ou "sair"? ')
senha = input('Digite a senha: ')

if entrada == 'entrar' and senha == '1234':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou entrar ou sair, ou então a senha está errada')