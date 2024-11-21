# Importa módulos necessários
from datetime import datetime  # Para lidar com datas
import random  # Para sorteio de treinos
from metas import metas_pessoais  # Importa a função para lidar com metas pessoais

# Função para criar dados formatados de treino ou competição
def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica):
    """
    Cria uma string formatada com os dados de um treino ou competição.
    Verifica e formata distância e tempo para exibição.
    """
    try:
        # Formata o tempo (em horas e minutos ou somente minutos)
        if tempo >= 60:
            tempo = f'{tempo // 60} h e {tempo - ((tempo // 60) * 60)} min'
        else:
            tempo = f'{tempo} min'

        # Calcula a parte inteira em quilômetros e a fração em metros
        try:
            km = int(distancia)
            metros = int((distancia - km) * 1000)
        except ValueError:
            print("Erro: A distância fornecida não é válida.")
            return None

        # Formata a distância para exibição
        if metros == 0:
            distancia_nome = f"{km} km"
        else:
            distancia_nome = f"{km} km e {metros} m"

        # Retorna o formato correto baseado no tipo de atividade
        if treinoOUcompeticao == 't':
            return f"treino: data: {data}, distância percorrida: {distancia_nome}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
        elif treinoOUcompeticao == 'c':
            return f"competição: data: {data}, distância percorrida: {distancia_nome}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
        else:
            raise ValueError("Erro: Tipo de atividade inválido.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado ao criar os dados: {e}")

# Função para salvar os dados no arquivo
def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    """
    Salva os dados formatados em um arquivo (banco.txt por padrão).
    Cada entrada recebe um índice incremental.
    """
    try:
        # Cria os dados formatados
        entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
        if entrada is None:
            return

        # Lê o arquivo para obter o índice da próxima entrada
        try:
            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
            proximo_indice = len(linhas) + 1
        except FileNotFoundError:
            # Se o arquivo não existir, começa do índice 1
            proximo_indice = 1

        # Adiciona a nova entrada no arquivo
        try:
            with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{proximo_indice}. {entrada}")
        except IOError:
            print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except ValueError as e:
        print(f"Erro ao salvar os dados no banco: {e}")
    except Exception as e:
        print(f"Erro inesperado ao salvar os dados no banco: {e}")

# Função para obter dados de entrada do usuário
def obter_dados():
    """
    Solicita ao usuário os dados do treino ou competição.
    Verifica e valida cada entrada.
    """
    try:
        # Pede o tipo de atividade
        treinoOUcompeticao = input("Escreva 't' para treino e 'c' para competição: \n")
        if treinoOUcompeticao not in ['t', 'c']:
            raise ValueError("Opção inválida: escolha 't' para treino ou 'c' para competição.")

        # Solicita e valida a data
        try:
            data_input = input("Escreva a data no formato: dd/mm/aaaa \n")
            data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y") # Formata a data, para ser uma data real e que já existiu
        except ValueError:
            print("Erro: A data deve estar no formato dd/mm/aaaa.")
            return None

        # Solicita e valida a distância
        try:
            distancia = float(input("Escreva a distância em quilômetros: \n"))
            if distancia <= 0:
                raise ValueError("A distância deve ser um número positivo maior que zero.")
        except ValueError:
            print("Erro: A distância deve ser um número positivo.")
            return None

        # Solicita e valida o tempo
        try:
            tempo = int(input("Coloque o tempo em minutos: \n"))
            if tempo <= 0:
                raise ValueError("O tempo deve ser um número positivo maior que zero.")
        except ValueError:
            print("Erro: O tempo deve ser um número inteiro maior que zero.")
            return None

        # Solicita o local
        localizacao = input("Coloque o nome do local: \n")
        if not localizacao.strip():
            print("Erro: A localização não pode estar vazia.")
            return None

        # Solicita a condição climática
        condicaoClimatica = input("Coloque a condição climática no tempo da atividade: \n")
        if not condicaoClimatica.strip():
            print("Erro: A condição climática não pode estar vazia.")
            return None

        return treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, "banco.txt"
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao obter os dados: {e}")
        return None

# Função para exibir as linhas do arquivo
def ler_linhas_individuais(arquivo_nome="banco.txt"):
    """
    Lê e exibe todas as linhas do arquivo especificado.
    """
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            texto = arquivo.readlines()
            for linha in texto:
                print(linha, end="")
            return texto
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado ao ler as linhas do arquivo: {e}")




# Função para deletar uma linha específica de um arquivo
def deletar_linha(arquivo_nome="banco.txt", numero_linha=1):
    """
    Remove uma linha específica de um arquivo com base no número da linha fornecido.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo a ser editado (padrão: 'banco.txt').
    numero_linha (int): Número da linha que deve ser deletada.
    Isso será usado no while 3.

    Retorno:
    None
    """
    try:
        # Abrir o arquivo e ler todas as linhas
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        # Verificar se o número da linha está dentro do intervalo válido
        if numero_linha < 1 or numero_linha > len(linhas):
            print("Erro: Número de linha inválido.")
            return

        try:
            # Remover a linha desejada (convertendo para índice de lista, subtraindo 1)
            del linhas[numero_linha - 1]
        except IndexError:
            print("Erro: Linha fora do intervalo válido para exclusão.")
            return

        try:
            # Reescrever o arquivo sem a linha especificada
            with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
                for indice, linha in enumerate(linhas, start=1):
                    arquivo.write(f'{indice}. {linha.split(". ")[1]}')
            print(f"Linha {numero_linha} deletada com sucesso.")
        except IOError:
            print("Erro: Problema ao reescrever o arquivo após exclusão.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para atualizar uma linha específica de um arquivo
def atualizar_linha(arquivo_nome="banco.txt", numero_linha=1, novo_conteudo=1): 
    """
    Atualiza o conteúdo de uma linha específica em um arquivo.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo a ser editado (padrão: 'banco.txt').
    numero_linha (int): Número da linha que deve ser atualizada. 
    novo_conteudo (str): Novo conteúdo a ser inserido na linha.
    Isso será usadao no while 4.
    Retorno:
    None
    """
    try:
        # Abrir o arquivo e ler todas as linhas
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        # Verificar se o número da linha está dentro do intervalo válido
        if numero_linha < 1 or numero_linha > len(linhas):
            print("Erro: Número de linha inválido.")
            return

        try:
            # Atualizar a linha desejada (convertendo para índice de lista, subtraindo 1)
            linhas[numero_linha - 1] = f"{numero_linha}. {novo_conteudo}"
        except IndexError:
            print("Erro: Linha fora do intervalo válido para atualização.")
            return

        try:
            # Reescrever o arquivo com a linha atualizada
            with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
                for indice, linha in enumerate(linhas, start=1): # start = 1 é para começar a contar o indice com 1
                    arquivo.write(f"{indice}. {linha.split('. ')[1]}")
            print(f"Linha {numero_linha} atualizada com sucesso.")
        except IOError:
            print("Erro: Problema ao reescrever o arquivo após atualização.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para calcular a velocidade média
def calcular_velocidade_media(distancia_km, tempo_min):
    """
    Calcula a velocidade média com base na distância percorrida e no tempo gasto.

    Parâmetros:
    distancia_km (float): Distância percorrida em quilômetros.
    tempo_min (float): Tempo gasto em minutos.

    Retorno:
    float: Velocidade média em km/h.
    """
    try:
        if tempo_min <= 0:
            raise ValueError("Erro: O tempo deve ser maior que zero para calcular a velocidade média.")
        velocidade_media = distancia_km / (tempo_min / 60)  # Conversão de minutos para horas
        return velocidade_media
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular a velocidade média.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado ao calcular a velocidade média: {e}")


# Função para calcular a velocidade média do último treino
def calcular_velocidade_media_ultimo_treino(arquivo_nome="banco.txt"):
    """
    Calcula a velocidade média com base nos dados do último treino registrado.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo contendo os dados dos treinos (padrão: 'banco.txt').

    Retorno:
    float: Velocidade média do último treino, em km/h, ou None em caso de erro.
    """
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            try:
                ultima_linha = arquivo.readlines()[-1]  # Pega a última linha do arquivo
            except IndexError:
                print("Erro: O arquivo está vazio, não há dados para calcular a velocidade média.")
                return None

        try:
            # Extrair a distância da última linha
            distancia_str = ultima_linha.split("distância percorrida: ")[1].split(", tempo:")[0]
            if "e" in distancia_str:  # Exemplo: "7 km e 22 m"
                km_str = distancia_str.split(" km")[0]
                m_str = distancia_str.split("e ")[1].split(" m")[0]
                distancia_km = int(km_str) + int(m_str) / 1000
            else:  # Exemplo: "7 km"
                distancia_km = int(distancia_str.split(" km")[0])
        except IndexError:
            print("Erro: Formato inesperado ao extrair a distância.")
            return None
        except ValueError:
            print("Erro: Distância contém valores inválidos.")
            return None

        try:
            # Extrair o tempo da última linha
            tempo_str = ultima_linha.split("tempo: ")[1].split(", localização:")[0]
            if "h" in tempo_str:  # Exemplo: "16 h e 30 min"
                horas = tempo_str.split(" h")[0]
                if "min" in tempo_str:
                    minutos = tempo_str.split("h e ")[1].split(" min")[0]
                    tempo_min = int(horas) * 60 + int(minutos)
                else:
                    tempo_min = int(horas) * 60
            else:  # Exemplo: "30 min"
                tempo_min = int(tempo_str.split(" min")[0])
        except IndexError:
            print("Erro: Formato inesperado ao extrair o tempo.")
            return None
        except ValueError:
            print("Erro: Tempo contém valores inválidos.")
            return None

        try:
            # Calcular a velocidade média
            horas = tempo_min / 60
            if horas <= 0:
                raise ZeroDivisionError("Erro: O tempo não pode ser zero ou negativo.")
            velocidade_media = calcular_velocidade_media(distancia_km, horas)
            return velocidade_media
        except ZeroDivisionError as e:
            print(e)
            return None

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para sortear um tipo de treino baseado na velocidade
def sorteio_treinos(velocidade):
    """
    Sorteia um tipo de treino baseado na velocidade média informada.

    Parâmetros:
    velocidade (float): Velocidade média em km/h.

    Retorno:
    str: Tipo de treino sorteado.
    """
    try:
        treinos = [
            "Treino de Intervalo Curto",
            "Treino de Velocidade em Tiro Curto",
            "Treino de Intervalo Longo",
            "Corrida Longa",
            "Treino de Ritmo Sustentado",
            "Treino de Subida"
        ]
        if velocidade > 5:
            return random.choice(treinos[:2])  # Sorteia entre os dois primeiros treinos
        else:
            return random.choice(treinos[2:])  # Sorteia entre os treinos restantes
    except ValueError:
        print("Erro: A velocidade fornecida não é válida.")
    except IndexError:
        print("Erro: O índice de treino está fora do intervalo permitido.")
    except Exception as e:
        print(f"Erro inesperado ao sortear treinos: {e}")


# Função auxiliar para acessar a distância de um treino
def chave_distancia(treino):
    """
    Obtém a distância do treino a partir de um dicionário, usado posteriormente.

    Parâmetros:
    treino (dict): Dicionário contendo a chave 'distancia_km'.

    Retorno:
    float: Distância do treino em quilômetros.
    """
    try:
        return treino["distancia_km"]
    except KeyError:
        print("Erro: Chave 'distancia_km' não encontrada no treino.")
    except TypeError:
        print("Erro: O objeto fornecido não é um dicionário ou está mal formatado.")
    except Exception as e:
        print(f"Erro inesperado ao acessar a distância do treino: {e}")


# Função auxiliar para acessar o tempo de um treino
def chave_tempo(treino):
    """
    Obtém o tempo do treino a partir de um dicionário.
    Aparecerá posteriormente

    Parâmetros:
    treino (dict): Dicionário contendo a chave 'tempo_min'.

    Retorno:
    int: Tempo do treino em minutos.
    """
    try:
        return treino["tempo_min"]
    except KeyError:
        print("Erro: Chave 'tempo_min' não encontrada no treino.")
    except TypeError:
        print("Erro: O objeto fornecido não é um dicionário ou está mal formatado.")
    except Exception as e:
        print(f"Erro inesperado ao acessar o tempo do treino: {e}")


# Função para filtrar treinos por distância
def filtrar_treinos_por_distancia(arquivo_nome="banco.txt", ordem_decrescente=True):
    """
    Filtra e ordena treinos registrados no arquivo com base na distância percorrida.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo contendo os dados dos treinos (padrão: 'banco.txt').
    ordem_decrescente (bool): Ordenar em ordem decrescente (True) ou crescente (False).

    Retorno:
    list: Lista de treinos ordenados por distância.
    """
    treinos = []
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                try:
                    distancia_str = linha.split("distância percorrida: ")[1].split(", tempo:")[0] #Split cria lista. Esse 1 é pra pegar tudo o que vem depois desse: e o 0 é pra pegar tudo o que vem antes desse , tempo
                    if "e" in distancia_str:
                        km_str, m_str = distancia_str.split(" km e ")
                        distancia_km = int(km_str) + int(m_str.split(" m")[0]) / 1000 #Esse 0 é tudo o que vem antes de ' m'
                    else:
                        distancia_km = int(distancia_str.split(" km")[0])

                    treinos.append({"linha": linha, "distancia_km": distancia_km})
                except IndexError:
                    print(f"Erro: Formato inesperado na linha (indexação fora do esperado): {linha}")
                except ValueError:
                    print(f"Erro: Valor inválido ao processar a distância na linha: {linha}")
                except Exception as e:
                    print(f"Erro inesperado ao processar a linha: {linha}. Detalhes: {e}")

        treinos.sort(key=chave_distancia, reverse=ordem_decrescente) #Usa a chave distancia da função anterior e retorna o distancia_km. Tem um reverse para o inverso, se quiser fazer contar de forma ao contrária.
        return [treino["linha"] for treino in treinos] #só vai ser lido a linha na ordem, pois será pego a linha nos treinos e elas foram ordenadas

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado ao abrir ou ler o arquivo: {e}")
        return []


# Função para filtrar treinos por tempo
def filtrar_treinos_por_tempo(arquivo_nome="banco.txt", ordem_decrescente=True):
    """
    Filtra e ordena treinos registrados no arquivo com base no tempo gasto.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo contendo os dados dos treinos (padrão: 'banco.txt').
    ordem_decrescente (bool): Ordenar em ordem decrescente (True) ou crescente (False).

    Retorno:
    list: Lista de treinos ordenados por tempo.
    """
    treinos = []
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                try:
                    tempo_str = linha.split("tempo: ")[1].split(", localização:")[0]
                    if "h" in tempo_str:
                        horas = int(tempo_str.split(" h")[0]) 
                        minutos = int(tempo_str.split("h e ")[1].split(" min")[0])
                        tempo_min = horas * 60 + minutos
                    else:
                        tempo_min = int(tempo_str.split(" min")[0]) #Esse 0 é tudo o que vem antes de ' min', mas dentro de tempo string

                    treinos.append({"linha": linha, "tempo_min": tempo_min})
                except IndexError:
                    print(f"Erro: Formato inesperado na linha (indexação fora do esperado): {linha}")
                except ValueError:
                    print(f"Erro: Valor inválido ao processar o tempo na linha: {linha}")
                except Exception as e:
                    print(f"Erro inesperado ao processar a linha: {linha}. Detalhes: {e}")

        treinos.sort(key=chave_tempo, reverse=ordem_decrescente) #Usa a chave_tempo de uma função anterior e retorna o distancia_km. Tem um reverse para o inverso, se quiser fazer contar de forma ao contrária.
        return [treino["linha"] for treino in treinos] #só vai ser lido a linha na ordem, pois será pego a linha nos treinos e elas foram ordenadas

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado ao abrir ou ler o arquivo: {e}")
        return []


# Função para criar um resumo estatístico dos treinos
def resumo_estatistico_treinos(arquivo_nome="banco.txt"):
    """
    Cria um resumo estatístico dos treinos com base nos dados registrados no arquivo.

    Parâmetros:
    arquivo_nome (str): Nome do arquivo contendo os dados dos treinos (padrão: 'banco.txt').

    Retorno:
    None: Exibe no console as informações estatísticas sobre os treinos.
    """
    try:
        distancias = []  # Lista para armazenar as distâncias de cada treino
        tempos = []  # Lista para armazenar os tempos de cada treino
        velocidades_medias = []  # Lista para armazenar as velocidades médias calculadas

        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            try:
                # Extrair a distância do treino
                distancia_str = linha.split("distância percorrida: ")[1].split(", tempo:")[0]
                if "e" in distancia_str:  # Exemplo: "7 km e 22 m"
                    km_str, m_str = distancia_str.split(" km e ")
                    distancia_km = int(km_str) + int(m_str.split(" m")[0]) / 1000
                else:  # Exemplo: "7 km"
                    distancia_km = int(distancia_str.split(" km")[0])
                distancias.append(distancia_km)

                # Extrair o tempo do treino
                tempo_str = linha.split("tempo: ")[1].split(", localização:")[0]
                if "h" in tempo_str:  # Exemplo: "2 h e 30 min"
                    horas = int(tempo_str.split(" h")[0])
                    minutos = int(tempo_str.split("h e ")[1].split(" min")[0])
                    tempo_min = horas * 60 + minutos
                else:  # Exemplo: "45 min"
                    tempo_min = int(tempo_str.split(" min")[0])
                tempos.append(tempo_min)

                # Calcular a velocidade média
                try:
                    velocidade_media = calcular_velocidade_media(distancia_km, tempo_min / 60)
                    velocidades_medias.append(velocidade_media)
                except ZeroDivisionError:
                    print("Erro: Tentativa de divisão por zero ao calcular a velocidade média.")

            except IndexError:
                print(f"Erro: Problema ao acessar índices na linha: {linha}")
            except ValueError:
                print(f"Erro: Valor inválido encontrado ao processar a linha: {linha}")
            except Exception as e:
                print(f"Erro inesperado ao processar a linha: {e}")

        if distancias and tempos:
            try:
                maior_distancia = max(distancias)
                menor_distancia = min(distancias)
                maior_tempo = max(tempos)
                menor_tempo = min(tempos)
                velocidade_media_geral = sum(velocidades_medias) / len(velocidades_medias)

                # Exibir resumo estatístico
                print("\nResumo Estatístico dos Treinos:")
                print(f"Maior distância percorrida: {maior_distancia:.2f} km")
                print(f"Menor distância percorrida: {menor_distancia:.2f} km")
                print(f"Maior tempo gasto: {maior_tempo} min")
                print(f"Menor tempo gasto: {menor_tempo} min")
                print(f"Velocidade média geral: {velocidade_media_geral:.2f} km/h")
            except ZeroDivisionError:
                print("Erro: Tentativa de divisão por zero ao calcular a velocidade média geral.")
        else:
            print("Nenhum dado válido encontrado nos treinos.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError as e:
        print(f"Erro ao acessar o arquivo: {e}")
    except Exception as e:
        print(f"Erro inesperado ao acessar o arquivo: {e}")


# Função para calcular o gasto calórico com base na velocidade média, peso e duração da corrida
def gastoCaloricoTeste(velocidadeMedia, peso, min):  # vm é em km/h
    """
    Calcula o gasto calórico com base na velocidade média, peso e tempo de corrida.

    Parâmetros:
    velocidadeMedia (float): Velocidade média em km/h.
    peso (float): Peso da pessoa em quilogramas.
    min (int): Tempo da corrida em minutos.

    Retorno:
    float: O gasto calórico estimado em calorias.
    """
    try:
        if velocidadeMedia <= 0 or peso <= 0 or min <= 0:
            raise ValueError("Velocidade, peso e tempo devem ser maiores que zero.")
        gastoCalorico = velocidadeMedia * peso * min * 0.0175
        return gastoCalorico
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado ao calcular o gasto calórico: {e}")


# Bloco principal para interação com o usuário
while True:
    try:
        # Exibe o menu de opções para o usuário
        pergunta = int(input(
            "Digite um número: \n"
            "1 para registrar dados\n"
            "2 para um treino aleatório\n"
            "3 para deletar dados\n"
            "4 para atualizar dados\n"
            "5 para filtrar os treinos\n"
            "6 para fazer um resumo estatístico dos treinos\n"
            "7 para ver quantas calorias serão gastas em uma determinada corrida\n"
            "8 para ver as metas pessoais\n"
            "9 para sair\n"
        ))

        if pergunta == 1:
            # Registrar novos dados
            dados = obter_dados()
            if dados:
                salvar_no_banco(*dados)
                print("Dados salvos com sucesso.\n")
            else:
                print("Dados não puderam ser salvos. Tente novamente.\n")

        elif pergunta == 2:
            # Sortear um treino com base na velocidade média do último treino
            velocidade_media_ultimo = calcular_velocidade_media_ultimo_treino()
            if velocidade_media_ultimo is not None:
                treino_sorteado = sorteio_treinos(velocidade_media_ultimo)
                print("Treino sorteado:", treino_sorteado)
            else:
                print("Não foi possível calcular a velocidade média do último treino.\n")

        elif pergunta == 3:
            # Deletar um dado específico
            ler_linhas_individuais()
            try:
                linha = int(input("\nEscolha a linha do treino ou competição que você quer deletar:\n"))
                deletar_linha(numero_linha=linha)
            except ValueError:
                print("Erro: Por favor, insira um número válido.")

        elif pergunta == 4:
            # Atualizar dados específicos
            ler_linhas_individuais()
            try:
                linha = int(input("\nEscolha a linha do treino ou competição que você quer atualizar:\n"))
                dados = obter_dados()
                if dados is not None:
                    novo_conteudo = criar_dados(*dados[:6])  # Pega só os seis primeiros elementos e proibe que que algo como o nome do arquivo entre.
                    atualizar_linha(numero_linha=linha, novo_conteudo=novo_conteudo) # ta na função atualizar_linha
                    print("Dados atualizados com sucesso.\n")
                else:
                    print("Erro ao atualizar os dados.")
            except ValueError:
                print("Erro: Por favor, insira um número válido.")
            except IndexError:
                print("Erro: A linha especificada não existe.")
            except Exception as e:
                print(f"Erro inesperado: {e}")







        elif pergunta == 5:
            # Filtrar treinos por distância ou tempo
            try:
                # Solicita ao usuário o critério de filtragem: 1 para distância ou 2 para tempo
                criterio = input("Filtrar por: 1 para distância ou 2 para tempo\n")
                
                if criterio == "1":  # Caso o critério seja distância
                    try:
                        # Solicita ao usuário a ordem de ordenação: 1 para maior distância ou 2 para menor distância
                        ordem = input("Ordenar por: 1 para maior distância ou 2 para menor distância\n")
                        ordem_decrescente = ordem == "1"  # Define se a ordenação será decrescente
                        treinos_ordenados = filtrar_treinos_por_distancia(ordem_decrescente=ordem_decrescente)  # Filtra os treinos por distância
                        print("Treinos ordenados por distância:")
                        for treino in treinos_ordenados:  # Exibe os treinos ordenados
                            print(treino)
                    except IndexError:
                        # Captura erros de indexação durante o processamento
                        print("Erro: Não foi possível acessar os treinos para ordenação por distância.")
                    except Exception as e:
                        # Captura erros gerais durante a filtragem por distância
                        print(f"Erro inesperado ao filtrar por distância: {e}")
                
                elif criterio == "2":  # Caso o critério seja tempo
                    try:
                        # Solicita ao usuário a ordem de ordenação: 1 para maior tempo ou 2 para menor tempo
                        ordem = input("Ordenar por: 1 para maior tempo ou 2 para menor tempo\n")
                        ordem_decrescente = ordem == "1"  # Define se a ordenação será decrescente
                        treinos_ordenados = filtrar_treinos_por_tempo(ordem_decrescente=ordem_decrescente)  # Filtra os treinos por tempo
                        print("Treinos ordenados por tempo:")
                        for treino in treinos_ordenados:  # Exibe os treinos ordenados
                            print(treino)
                    except IndexError:
                        # Captura erros de indexação durante o processamento
                        print("Erro: Não foi possível acessar os treinos para ordenação por tempo.")
                    except Exception as e:
                        # Captura erros gerais durante a filtragem por tempo
                        print(f"Erro inesperado ao filtrar por tempo: {e}")
                
                else:
                    # Caso o usuário insira um critério inválido
                    print("Erro: Opção inválida para critério de filtragem.")
            except ValueError:
                # Captura erros de valor inválido na entrada do usuário
                print("Erro: Por favor, insira um número válido.")
            except IndexError:
                # Captura erros de indexação fora do intervalo permitido
                print("Erro: A linha especificada não existe.")
            except Exception as e:
                # Captura erros gerais e inesperados
                print(f"Erro inesperado: {e}")


        elif pergunta == 6:
            # Mostrar resumo estatístico dos treinos
            resumo_estatistico_treinos()

        elif pergunta == 7:
            # Calcular o gasto calórico de uma corrida
            try:
                velocidadeMedia = float(input("Coloque a velocidade média em quilômetros por hora:\n"))
                peso = float(input("Coloque o seu peso em quilogramas:\n"))
                minutos = int(input("Coloque o tempo gasto na corrida (em minutos):\n"))
                gastoCalorico = gastoCaloricoTeste(velocidadeMedia, peso, minutos)
                print(f"Houve um gasto calórico de {gastoCalorico:.2f} calorias.")
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")

        elif pergunta == 8:
            # Gerenciar metas pessoais
            metas_pessoais()

        elif pergunta == 9:
            # Sair do programa
            print("Finalizando programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

        # Pergunta se o usuário deseja continuar
        continuacao = input("Você quer continuar? Digite '1' para parar. Qualquer outra tecla para continuar.\n")
        if continuacao == '1':
            print("Finalizando programa. Até logo!")
            break

    except ValueError:
        print("Erro: Digite um número válido.\n")
        continuacao = input("Você quer continuar? Digite '1' para parar. Qualquer outra tecla para continuar.\n")
        if continuacao == '1':
            print("Finalizando programa. Até logo!")
            break
