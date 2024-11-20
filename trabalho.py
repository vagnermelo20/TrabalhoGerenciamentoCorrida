from datetime import datetime
import random
from metas import metas_pessoais

def criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica):
    try:
        if tempo >= 60:
            tempo = f'{tempo // 60} h e {tempo - ((tempo // 60) * 60)} min'
        else:
            tempo = f'{tempo} min'

        try:
            km = int(distancia)  # Parte inteira em quilômetros
            metros = int((distancia - km) * 1000)  # Parte inteira dos metros
        except ValueError:
            print("Erro: A distância fornecida não é válida.")
            return None

        if metros == 0:
            distancia_nome = f"{km} km"
        else:
            distancia_nome = f"{km} km e {metros} m"

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


def salvar_no_banco(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica, arquivo_nome="banco.txt"):
    try:
        entrada = criar_dados(treinoOUcompeticao, data, distancia, tempo, localizacao, condicaoClimatica)
        if entrada is None:
            return

        try:
            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
            proximo_indice = len(linhas) + 1
        except FileNotFoundError:
            proximo_indice = 1

        try:
            with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{proximo_indice}. {entrada}")
        except IOError:
            print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except ValueError as e:
        print(f"Erro ao salvar os dados no banco: {e}")
    except Exception as e:
        print(f"Erro inesperado ao salvar os dados no banco: {e}")


def obter_dados():
    try:
        treinoOUcompeticao = input("Escreva 't' para treino e 'c' para competição: \n")
        if treinoOUcompeticao not in ['t', 'c']:
            raise ValueError("Opção inválida: escolha 't' para treino ou 'c' para competição.")

        try:
            data_input = input("Escreva a data no formato: dd/mm/aaaa \n")
            data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Erro: A data deve estar no formato dd/mm/aaaa.")
            return None

        try:
            distancia = float(input("Escreva a distância em quilômetros: \n"))
            if distancia <= 0:
                raise ValueError("A distância deve ser um número positivo maior que zero.")
        except ValueError:
            print("Erro: A distância deve ser um número positivo.")
            return None

        try:
            tempo = int(input("Coloque o tempo em minutos: \n"))
            if tempo <= 0:
                raise ValueError("O tempo deve ser um número positivo maior que zero.")
        except ValueError:
            print("Erro: O tempo deve ser um número inteiro maior que zero.")
            return None

        localizacao = input("Coloque o nome do local: \n")
        if not localizacao.strip():
            print("Erro: A localização não pode estar vazia.")
            return None

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


def ler_linhas_individuais(arquivo_nome="banco.txt"):
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



def deletar_linha(arquivo_nome="banco.txt", numero_linha=1):
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
                    arquivo.write(f'{indice}. {linha.split(". ", 1)[1]}')
            print(f"Linha {numero_linha} deletada com sucesso.")
        except IOError:
            print("Erro: Problema ao reescrever o arquivo após exclusão.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def atualizar_linha(arquivo_nome="banco.txt", numero_linha=1, novo_conteudo=1):
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
                for indice, linha in enumerate(linhas, start=1):
                    arquivo.write(f"{indice}. {linha.split('. ', 1)[1]}")
            print(f"Linha {numero_linha} atualizada com sucesso.")
        except IOError:
            print("Erro: Problema ao reescrever o arquivo após atualização.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def calcular_velocidade_media(distancia_km, tempo_min):
    try:
        if tempo_min <= 0:
            raise ValueError("Erro: O tempo deve ser maior que zero para calcular a velocidade média.")
        velocidade_media = distancia_km / tempo_min
        return velocidade_media
    except ZeroDivisionError:
        print("Erro: Divisão por zero ao calcular a velocidade média.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado ao calcular a velocidade média: {e}")


def calcular_velocidade_media_ultimo_treino(arquivo_nome="banco.txt"):
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

def sorteio_treinos(velocidade):
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
            return random.choice(treinos[:2])
        else:
            return random.choice(treinos[2:6])
    except ValueError:
        print("Erro: A velocidade fornecida não é válida.")
    except IndexError:
        print("Erro: O índice de treino está fora do intervalo permitido.")
    except Exception as e:
        print(f"Erro inesperado ao sortear treinos: {e}")


def chave_distancia(treino):
    try:
        return treino["distancia_km"]
    except KeyError:
        print("Erro: Chave 'distancia_km' não encontrada no treino.")
    except TypeError:
        print("Erro: O objeto fornecido não é um dicionário ou está mal formatado.")
    except Exception as e:
        print(f"Erro inesperado ao acessar a distância do treino: {e}")


def chave_tempo(treino):
    try:
        return treino["tempo_min"]
    except KeyError:
        print("Erro: Chave 'tempo_min' não encontrada no treino.")
    except TypeError:
        print("Erro: O objeto fornecido não é um dicionário ou está mal formatado.")
    except Exception as e:
        print(f"Erro inesperado ao acessar o tempo do treino: {e}")


def filtrar_treinos_por_distancia(arquivo_nome="banco.txt", ordem_decrescente=True):
    treinos = []
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                try:
                    distancia_str = linha.split("distância percorrida: ")[1].split(", tempo:")[0]
                    if "e" in distancia_str:
                        km_str, m_str = distancia_str.split(" km e ")
                        distancia_km = int(km_str) + int(m_str.split(" m")[0]) / 1000
                    else:
                        distancia_km = int(distancia_str.split(" km")[0])

                    treinos.append({"linha": linha, "distancia_km": distancia_km})

                except IndexError:
                    print(f"Erro: Formato inesperado na linha (indexação fora do esperado): {linha}")
                except ValueError:
                    print(f"Erro: Valor inválido ao processar a distância na linha: {linha}")
                except Exception as e:
                    print(f"Erro inesperado ao processar a linha: {linha}. Detalhes: {e}")

        treinos.sort(key=chave_distancia, reverse=ordem_decrescente)
        return [treino["linha"] for treino in treinos]

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado ao abrir ou ler o arquivo: {e}")
        return []

def filtrar_treinos_por_tempo(arquivo_nome="banco.txt", ordem_decrescente=True):

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
                        tempo_min = int(tempo_str.split(" min")[0])

                    treinos.append({"linha": linha, "tempo_min": tempo_min})
                except IndexError:
                    print(f"Erro: Formato inesperado na linha (indexação fora do esperado): {linha}")
                except ValueError:
                    print(f"Erro: Valor inválido ao processar a distância na linha: {linha}")
                except Exception as e:
                    print(f"Erro inesperado ao processar a linha: {linha}. Detalhes: {e}")

        treinos.sort(key=chave_tempo, reverse=ordem_decrescente)
        return [treino["linha"] for treino in treinos]
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError:
        print(f"Erro ao acessar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Erro inesperado ao abrir ou ler o arquivo: {e}")
        return []        

def resumo_estatistico_treinos(arquivo_nome="banco.txt"):
    try:
        distancias = []
        tempos = []
        velocidades_medias = []

        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            try:
                # Extrair a distância
                distancia_str = linha.split("distância percorrida: ")[1].split(", tempo:")[0]
                if "e" in distancia_str:
                    km_str, m_str = distancia_str.split(" km e ")
                    distancia_km = int(km_str) + int(m_str.split(" m")[0]) / 1000
                else:
                    distancia_km = int(distancia_str.split(" km")[0])
                distancias.append(distancia_km)

                # Extrair o tempo
                tempo_str = linha.split("tempo: ")[1].split(", localização:")[0]
                if "h" in tempo_str:
                    horas = int(tempo_str.split(" h")[0])
                    minutos = int(tempo_str.split("h e ")[1].split(" min")[0])
                    tempo_min = horas * 60 + minutos
                else:
                    tempo_min = int(tempo_str.split(" min")[0])
                tempos.append(tempo_min)

                # Calcular a velocidade média
                try:
                    velocidade_media = calcular_velocidade_media(distancia_km, tempo_min / 60)
                    velocidades_medias.append(velocidade_media)
                except ZeroDivisionError:
                    print("Erro: Tentativa de dividir por zero ao calcular a velocidade média.")

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

                print("\nResumo Estatístico dos Treinos:")
                print(f"Maior distância percorrida: {maior_distancia:.2f} km")
                print(f"Menor distância percorrida: {menor_distancia:.2f} km")
                print(f"Maior tempo gasto: {maior_tempo} min")
                print(f"Menor tempo gasto: {menor_tempo} min")
                print(f"Velocidade média geral: {velocidade_media_geral:.2f} km/h")
            except ZeroDivisionError:
                print("Erro: Tentativa de dividir por zero ao calcular a velocidade média geral.")
        else:
            print("Nenhum dado válido encontrado nos treinos.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_nome}' não encontrado.")
    except IOError as e:
        print(f"Erro ao acessar o arquivo: {e}")
    except Exception as e:
        print(f"Erro inesperado ao acessar o arquivo: {e}")


def gastoCaloricoTeste(velocidadeMedia, peso, min):  # vm é em km/h
    try:
        if velocidadeMedia <= 0 or peso <= 0 or min <= 0:
            raise ValueError("Velocidade, peso e tempo devem ser maiores que zero.")
        gastoCalorico = velocidadeMedia * peso * min * 0.0175
        return gastoCalorico
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado ao calcular o gasto calórico: {e}")


while True:
    try:
        pergunta = int(input("Digite um número: \n1 para registrar dados\n2 para um treino aleátorio\n3 para deletar dados\n4 para atualizar dados\n5 para filtrar os treinos\n6 para fazer um resumo estatístico dos treinos\n7 para ver quantas calórias serão gastas em uma determinada corrida\n8 para ver as metas pessoais\n9 para sair\n"))
        if pergunta == 1:
            dados = obter_dados()
            if dados:
                salvar_no_banco(*dados)
                print("Dados salvos com sucesso.\n")
            else:
                print("Dados não puderão ser salvos, tente novamente.\n")
        elif pergunta == 2:
            velocidade_media_ultimo = calcular_velocidade_media_ultimo_treino()
            if velocidade_media_ultimo is not None:
                treino_sorteado = sorteio_treinos(velocidade_media_ultimo)
                print("Treino sorteado:", treino_sorteado)
            else:
                print("Não foi possível calcular a velocidade média do último treino.\n")
        elif pergunta == 3:
            ler_linhas_individuais()
            linha = int(input("\n Escolha a linha do treino ou competição que você quer deletar:\n"))
            deletar_linha(numero_linha=linha)

        elif pergunta == 4:
            ler_linhas_individuais()
            linha = int(input("\n Escolha a linha do treino ou competição que você quer atualizar:\n"))
            dados = obter_dados()
            if dados:
                novo_conteudo = criar_dados(*dados[:6])  # Formata os dados para a linha
                atualizar_linha(numero_linha=linha, novo_conteudo=novo_conteudo)
                print("Dados atualizados com sucesso.\n")
            else:
                print("Erro ao atualizar os dados")
        
        elif pergunta == 5:
            criterio = input("Filtrar por: 1 para distância ou 2 para tempo\n")
            if criterio == "1":
                ordem = input("Ordenar por: 1 pra ir da maior para menor distância ou 2 pra ir da menor para maior deistância\n")
                ordem_decrescente = ordem == "1"
                treinos_ordenados = filtrar_treinos_por_distancia(ordem_decrescente=ordem_decrescente)
                print("Treinos ordenados por distância:")
                for treino in treinos_ordenados:
                    print(treino)
            elif criterio == "2":
                ordem = input("Ordenar por: 1 pra ir do maior para o menor tempo ou 2 pra ir do maior para o menor tempo\n")
                ordem_decrescente = ordem == "1"
                treinos_ordenados = filtrar_treinos_por_tempo(ordem_decrescente=ordem_decrescente)
                print("Treinos ordenados por tempo:")
                for treino in treinos_ordenados:
                    print(treino)
        
        elif pergunta == 6:
            resumo_estatistico_treinos ()
        elif pergunta == 7:
            velocidadeMedia = float(input("Coloque a velocidade média em quilometros por hora\n"))
            peso = float(input("Coloca o seu peso em quilogramas\n"))
            minutos = int(input("Coloque quanto tempo em minutos que voce gastou na corrida\n"))
            gastoCalorico = gastoCaloricoTeste(velocidadeMedia, peso, minutos)
            print(f'houve um gasto calórico de {gastoCalorico} calorias')
        elif pergunta == 8:
            metas_pessoais()
        elif pergunta == 9:
            break
        else:
            print("Opção inválida. Tente novamente.\n")
        continuacao = input("Voce quer continuar: Digite '1' para parar, todas as outras respostas, o código vai continuar\n")
        if continuacao == '1':
            break
    except ValueError:
        print("Erro: Digite um número válido.\n")
        continuacao = input("Voce quer continuar: Digite '1' para parar, todas as outras respostas, o código vai continuar\n")
        if continuacao == '1':
            break