import re

def validar_cpf(cpf: str) -> bool:
    # Remove tudo que não é número do CPF
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)

    # Verifica se o CPF é sequencial
    sequencial = cpf == cpf[0] * len(cpf)
    if sequencial:
        print('Você enviou dados sequenciais.')
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i, digito in enumerate(cpf_limpo[:9]):
        soma += int(digito) * (10 - i)
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calcula o segundo dígito verificador
    soma = 0
    for i, digito in enumerate(cpf_limpo[:9] + str(digito_1)):
        soma += int(digito) * (11 - i)
    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Verifica se o CPF é válido
    cpf_calculado = f'{cpf_limpo[:9]}{digito_1}{digito_2}'
    if cpf_limpo == cpf_calculado:
        return True
    else:
        return False


# Exemplo de uso
cpf = input('Digite o CPF: ')
if validar_cpf(cpf):
    print(f'{cpf} é válido')
else:
    print('CPF inválido')