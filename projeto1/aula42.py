frase = 'Qual é a letra que mais irá aparecer nessa frase que você está lendo agora!'
frase2 = 'bbaaaaoooob'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    elif qtd_apareceu_mais_vezes == qtd_apareceu_mais_vezes_atual and letra_atual not in letra_apareceu_mais_vezes:
        letra_apareceu_mais_vezes += letra_atual

    i += 1

if len(letra_apareceu_mais_vezes) > 1:
    print(f'As letras que mais apareceram na frase "{frase}" foram: {", ".join(letra_apareceu_mais_vezes)}, cada uma aparecendo {qtd_apareceu_mais_vezes}x.')
else:
    print(f'A letra que mais apareceu na frase "{frase}" foi a letra "{letra_apareceu_mais_vezes}", que apareceu {qtd_apareceu_mais_vezes}x.')
