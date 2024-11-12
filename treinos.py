import os 
os.system("cls")

import random

distancia=int(input("Digite a distancia em km: "))
tempo=int(input("Digite o tempo da sua corrida em horas: "))
velocidade=distancia/tempo

def sorteio_treinos(velocidade, treino):
    if velocidade>5:
        return random.choice(treino[:2])
    elif velocidade<=5:
        return random.choice(treino[2:5])

treinos = ["Treino de Intervalo Curto","Treino de Velocidade em Tiro Curto","Treino de Intervalo Longo","Corrida Longa","Treino de Ritmo Sustentado","Treino de subida"]
treino_sorteado = sorteio_treinos(velocidade, treinos)
print("Treino sorteado:", treino_sorteado)







