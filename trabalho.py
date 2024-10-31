def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    if treinoOUcompeticao == 'treino':
        return f"treino: data: {data}, distância percorrida: {distancia} km, tempo: {tempo} min, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    elif treinoOUcompeticao == 'competicao':
        return f"competição: data: {data}, distância percorrida: {distancia}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
    with open(arquivo_nome, "a") as arquivo:
        arquivo.write(entrada)
def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
    with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
        arquivo.write(entrada)

# Exemplo de uso
salvar_no_banco("treino", "20/08/2024", 10, 60, "Centro", "Ensolarado")
salvar_no_banco("competicao", "15/02/2024", 21, 120, "Praia", "Nublado")