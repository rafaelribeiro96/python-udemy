frase = 'Qual é a letra que mais irá aparecer nessa frase que você está lendo agora!'
frase2 = 'bbaaaaoooob'

i = 0
maior_quantidade_aparicoes = 0
letras_mais_apareceram = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_aparicoes_atual = frase.count(letra_atual)

    if quantidade_aparicoes_atual > maior_quantidade_aparicoes:
        maior_quantidade_aparicoes = quantidade_aparicoes_atual
        letras_mais_apareceram = letra_atual
    elif quantidade_aparicoes_atual == maior_quantidade_aparicoes and letra_atual not in letras_mais_apareceram:
        letras_mais_apareceram += letra_atual

    i += 1

if len(letras_mais_apareceram) > 1:
    print(f'As letras que mais apareceram na frase "{frase}" foram: {", ".join(letras_mais_apareceram)}, cada uma aparecendo {maior_quantidade_aparicoes}x.')
else:
    print(f'A letra que mais apareceu na frase "{frase}" foi a letra "{letras_mais_apareceram}", que apareceu {maior_quantidade_aparicoes}x.')
