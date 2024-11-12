from datetime import datetime
import random

def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica):
    if tempo >= 60:
        tempo = f'{tempo//60} h e {tempo - ((tempo//60) * 60)} min'
    else:
        tempo = f'{tempo} min'

    km = int(distancia)  # Parte inteira em quilômetros
    metros = int((distancia - km) * 1000)  # Parte inteira dos metros

    if metros == 0:
        distancia = f"{km} km"
    else:
        distancia = f"{km} km e {metros} m"

    if treinoOUcompeticao == 't':
        return f"treino: data: {data}, distância percorrida: {distancia}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    elif treinoOUcompeticao == 'c':
        return f"competição: data: {data}, distância percorrida: {distancia}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    
def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
    try:
        with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
            arquivo.write(entrada)
    except IOError as e:
        print(f"Erro ao salvar no banco de dados: {e}")
        return None

def obter_dados():
    try:
        treinoOUcompeticao = input("Escreva 't' para treino e 'c' para competição: \n")
        if treinoOUcompeticao not in ['t', 'c']:
            raise ValueError("Opção inválida: escolha 't' para treino ou 'c' para competicao. \n")
        
        data_input = input("Escreva a data no formato: dd/mm/aaaa \n")
        try:
            data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Erro: A data deve estar no formato dd/mm/aaaa. \n")
            return None

        try:
            distancia = float(input("Escreva a distância em quilômetros: \n"))
            if distancia <= 0:
                raise ValueError("Erro: a distância deve ser um número positivo maior que zero. \n")

        except ValueError:
            print("Erro: a distância deve ser um número positivo. \n")
            return None

        try:
            tempo = int(input("Coloque o tempo em minutos: \n"))
            if tempo <= 0:
                raise ValueError("Erro: o tempo deve ser um número positivo maior que zero. \n")
        except ValueError:
            print("Erro: o tempo deve ser um número inteiro e maior que zero. \n")
            return None
        
        localizacao = input("Coloque o nome do local: \n")
        if any(char.isdigit() for char in localizacao):
            print("Erro: a localização não deve conter números. \n")
            return None
        if not localizacao.strip():
            print("Erro: a localização não pode estar vazia. \n")
            return None

        condicaoClimatica = input("Coloque a condição climática no tempo da atividade: \n")
        if any(char.isdigit() for char in condicaoClimatica):
            print("Erro: a condição climática não deve conter números. \n")
            return None
        if not condicaoClimatica.strip():
            print("Erro: a condição climática não pode estar vazia. \n")
            return None
        
        return treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, "banco.txt"
    except ValueError as e:
        print(f"Erro: {e} \n")
        return None


def vMedia(distancia,tempo):
    vMedia = distancia/tempo
# sorteio de treinos
def sorteio_treinos(treino):
    return random.choice(treino)
treino =["Treino de Intervalo Curto","Treino de Velocidade em Tiro Curto","Treino de Intervalo Longo","Corrida Longa","Treino de Ritmo Sustentado","Treino de subida"]
sorteado = sorteio_treinos(treino)
  
i = 0
while i == 0:
    try:
        pergunta = int(input("Digite um número: \n1 para registrar dados\n2 para sortear um treino\n3 para sair\n"))
        if pergunta == 1:
            dados = obter_dados()
            if dados:
                salvar_no_banco(*dados)
                print("Dados salvos com sucesso.\n")
            else:
                print("Dados não puderão ser salvos, tente novamente.\n")
        elif pergunta == 2:
            print("Elemento sorteado:", sorteio_treinos(treino))
        elif pergunta == 3:
            i += 1
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Digite um número válido.")