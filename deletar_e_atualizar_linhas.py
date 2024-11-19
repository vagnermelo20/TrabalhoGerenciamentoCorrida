def deletar_linha(arquivo_nome="banco.txt", numero_linha=1):

    try:

        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()


        if numero_linha < 1 or numero_linha > len(linhas):
            print("Número de linha inválido.")
            return


        del linhas[numero_linha - 1]


        with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)

            print(f"Linha {numero_linha} deletada com sucesso.")

    except IOError as erro:
        print("Erro ao acessar o arquivo:", erro)



def atualizar_linha(arquivo_nome="banco.txt", numero_linha=1, novo_conteudo = 1):

    try:

        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if numero_linha < 1 or numero_linha > len(linhas):
                print("Número de linha inválido.")
                return

            linhas[numero_linha - 1] = novo_conteudo

        with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)

            print(f"Linha {numero_linha} atualizada com sucesso.")

    except IOError as erro:
        print("Erro ao acessar o arquivo:", erro)
