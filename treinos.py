import os 
os.system("cls")

import random

def sorteio_treinos(treino):
    return random.choice(treino)
treino=["Treino de Intervalo Curto","Treino de Velocidade em Tiro Curto","Treino de Intervalo Longo","Corrida Longa","Treino de Ritmo Sustentado","Treino de subida"]
sorteado = sorteio_treinos(treino)
print("Elemento sorteado:", sorteado)





