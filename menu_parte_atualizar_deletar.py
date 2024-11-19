elif pergunta == 3:
    ler_linhas_individuais()
    linha = int(input("\n Escolha a linha do treino ou competição que você quer deletar:\n"))
    deletar_linha(numero_linha=linha)

elif pergunta == 4:
    ler_linhas_individuais()
    linha = int(input("\n Escolha a linha do treino ou competição que você quer atualizar:\n"))
    dados = obter_dados()
if dados:
    novo_conteudo = criar_dados(*dados[:6]) # Formata os dados para a linha
    atualizar_linha(numero_linha=linha, novo_conteudo=novo_conteudo)
    print("Dados atualizados com sucesso.\n")
else:
    print("Erro ao atualizar os dados")