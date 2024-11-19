def ler_linhas_individuais(arquivo_nome="banco.txt"):

    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
        for linha in texto:
            certo = print(linha, end="")
            return certo