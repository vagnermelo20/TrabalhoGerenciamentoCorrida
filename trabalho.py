def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica):
    if treinoOUcompeticao == 'treino':
        return f"treino: data: {data}, distância percorrida: {distancia} km, tempo: {tempo} min, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    elif treinoOUcompeticao == 'competicao':
        return f"competição: data: {data}, distância percorrida: {distancia} km, tempo: {tempo} min, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
    with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
        arquivo.write(entrada)

# Exemplo de uso
# salvar_no_banco("treino", "20/08/2024", 10, 60, "Centro", "Ensolarado")
# salvar_no_banco("competicao", "15/02/2024", 21, 120, "Praia", "Nublado")
def obter_dados():
    treinoOUcompeticao = input("Escreva 'treino' para treino e 'competicao' para competição: \n")
    data = input("Escreva a data no formato: dd/mm/aaaa \n")
    distancia = int(input("Escreva a distância em quilômetros: \n"))
    tempo = int(input("Coloque o tempo em minutos: \n"))
    localizacao = input("Coloque o nome do local: \n")
    condicaoClimatica = input("Coloque a condição climática no tempo da atividade: \n")
    arquivo_nome="banco.txt"
    return treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome
i = 0
while i == 0:
    pergunta = int(input("Bota um numero: "))
    if pergunta == 1:
        dados = obter_dados()
        salvar_no_banco(*dados)    
    elif pergunta == 2:
        i+=1