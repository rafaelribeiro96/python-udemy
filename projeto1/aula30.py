RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGER = 1

velocidade = input("Digite a velocidade do carro: ")
velocidade = int(velocidade)
local_carro = input("Digite a localização do carro: ")
local_carro = int(local_carro)

velocidade_acima_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar_1 = velocidade_acima_carro_passou_radar_1 and carro_passou_radar_1
dif_velocidade_radar_1 = velocidade - RADAR_1


if carro_passou_radar_1:
    print(f"Carro passou pelo radar 1, que tem o limite de {RADAR_1}km/h")

if velocidade_acima_carro_passou_radar_1:
    print(f'Velocidade que o carro passou no Radar 1 = {velocidade}km/h')

if carro_multado_radar_1:
    print(f"Carro multado no radar 1 por excesso de velocidade, pois passou a {velocidade}km/h em um radar que tem o limite de {RADAR_1}km/h sendo então a diferença de {dif_velocidade_radar_1}km/h acima do limite permitido")
