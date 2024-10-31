def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica):
    tipo = 'treino' if treinoOUcompeticao == 'treino' else 'competição'
    return f"{tipo}: data: {data}, distância percorrida: {distancia} km, tempo: {tempo} min, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"

def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
    with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
        arquivo.write(entrada)
    print("Dados salvos com sucesso!")

def obter_dados():
    treinoOUcompeticao = input("Escreva 'treino' para treino e 'competicao' para competição: \n")
    data = input("Escreva a data no formato: dd/mm/aaaa \n")
    distancia = int(input("Escreva a distância em quilômetros: \n"))
    tempo = int(input("Coloque o tempo em minutos: \n"))
    localizacao = input("Coloque o nome do local: \n")
    condicaoClimatica = input("Coloque a condição climática no tempo da atividade: \n")
    return treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica

def main():
    while True:
        try:
            pergunta = int(input("Bota um número (1 para adicionar dados, 2 para sair): "))
            if pergunta == 1:
                dados = obter_dados()
                salvar_no_banco(*dados)    
            elif pergunta == 2:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
