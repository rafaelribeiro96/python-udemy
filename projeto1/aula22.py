entrada = input('[E]ntrar ou [S]air?: ')
senha = input('Digite a senha: ')

senha_correta = '1234'

if (entrada == 'E' or entrada == 'e') and senha == senha_correta:
    print('Você entrou no sistema')
else:
    print('Você saiu do sistema')