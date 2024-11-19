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
        distancia_nome = f"{km} km"
    else:
        distancia_nome = f"{km} km e {metros} m"

    if treinoOUcompeticao == 't':
        return f"treino: data: {data}, distância percorrida: {distancia_nome}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    elif treinoOUcompeticao == 'c':
        return f"competição: data: {data}, distância percorrida: {distancia_nome}, tempo: {tempo}, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n"
    
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

def ler_linhas_individuais(arquivo_nome="banco.txt"):

    # Abrir o arquivo e ler todas as linhas
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
        for linha in texto:
            certo = print(linha, end="")
        return certo


def deletar_linha(arquivo_nome="banco.txt", numero_linha=1):

    try:
        # Abrir o arquivo e ler todas as linhas
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        # Verificar se o número da linha está dentro do intervalo válido
        if numero_linha < 1 or numero_linha > len(linhas):
            print("Número de linha inválido.")
            return

        # Remover a linha desejada (convertendo para índice de lista, subtraindo 1)
        del linhas[numero_linha - 1]

        # Reescrever o arquivo sem a linha especificada
        with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)

        print(f"Linha {numero_linha} deletada com sucesso.")

    except IOError as erro:
        print("Erro ao acessar o arquivo:", erro)
    
def atualizar_linha(arquivo_nome="banco.txt", numero_linha=1, novo_conteudo = 1):

    try:
        # Abrir o arquivo e ler todas as linhas
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        # Verificar se o número da linha está dentro do intervalo válido
        if numero_linha < 1 or numero_linha > len(linhas):
            print("Número de linha inválido.")
            return

        # Atualizar a linha desejada (convertendo para índice de lista, subtraindo 1)
        linhas[numero_linha - 1] = novo_conteudo

        # Reescrever o arquivo com a linha atualizada
        with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)

        print(f"Linha {numero_linha} atualizada com sucesso.")

    except IOError as erro:
        print("Erro ao acessar o arquivo:", erro)
    
def calcular_velocidade_media(distancia_km, tempo_min):
    velocidade_media = distancia_km / tempo_min
    return velocidade_media

def calcular_velocidade_media_ultimo_treino(arquivo_nome="banco.txt"):
    try:

        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            ultima_linha = arquivo.readlines()[-1] #esse menos 1 é a ´tltima linha
        distancia_str = ultima_linha.split("distância percorrida: ")[1].split(", tempo:")[0] #Pega o que vem depois de "distancia percorrida: " e o que vem antes de ", tempo":
        #isso vira 7 km e 22 m
        if "e" in distancia_str:
            km_str = distancia_str.split(" km")[0]
            m_str = distancia_str.split("e ")[1].split(" m")[0]
            distancia_km = int(km_str) + int(m_str)
        else:
            distancia_km = int(distancia_str.split(" km")[0])
            tempo_str = ultima_linha.split("tempo: ")[1].split(", localização:")[0] #16 h e 30 min
        if "h" in tempo_str:
            horas = tempo_str.split(" h")[0]
            if "min" in tempo_str:
                minutos = tempo_str.split("h e ")[1].split(" min")[0]
                tempo_min = int(horas) * 60 + int(minutos)
            else:
                tempo_min = int(horas) * 60
        else:
            tempo_min = int(tempo_str.split(" min")[0])
        horas=tempo_min/60
        velocidade_media = calcular_velocidade_media(distancia_km, horas)
        return velocidade_media  
    except (IOError, IndexError, ValueError) as e:
        print(f"Erro ao calcular a velocidade média do último treino: {e}")

def sorteio_treinos(velocidade):
    treinos = [
        "Treino de Intervalo Curto",
        "Treino de Velocidade em Tiro Curto",
        "Treino de Intervalo Longo",
        "Corrida Longa",
        "Treino de Ritmo Sustentado",
        "Treino de subida"
    ]
    if velocidade > 5:
        return random.choice(treinos[:2])
    else:
        return random.choice(treinos[2:6])

def chave_distancia(treino):
    return treino["distancia_km"]
def chave_tempo(treino):
    return treino["tempo_min"]

def filtrar_treinos_por_distancia(arquivo_nome="banco.txt", ordem_decrescente=True):

    treinos = []

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
            except (IndexError, ValueError):
                print(f"Erro ao processar a linha: {linha}")

    treinos.sort(key=chave_distancia, reverse=ordem_decrescente)
    return [treino["linha"] for treino in treinos]

def filtrar_treinos_por_tempo(arquivo_nome="banco.txt", ordem_decrescente=True):

    treinos = []

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
            except (IndexError, ValueError):
                print(f"Erro ao processar a linha: {linha}")

    treinos.sort(key=chave_tempo, reverse=ordem_decrescente)
    return [treino["linha"] for treino in treinos]

def metas_pessoais():
    while True:

        arquivo = open('metas.txt','r', encoding='utf-8')
        metas_arquivo = arquivo.readlines()
        arquivo.close()

        arquivo = open('metas_concluidas.txt','r', encoding='utf-8')
        metas_arquivo_concluído = arquivo.readlines()
        linha_metas_concluidas = len(metas_arquivo_concluído)
        arquivo.close()

        print('1. Visualizar as metas atuais: \n'
              '2. Definir novas metas: \n' 
              '3. Alterar uma meta: \n'
              '4. Deletar uma meta: \n'
              '5. Concluir uma meta: \n'
              '6. Checar as metas concluídas: \n'
              '7. Deletar uma meta concluída: \n'
              '8. Fechar o programa: \n')
        try:
            escolha = int(input('Selecione uma opção: '))

            if escolha == 1:
                for linha in metas_arquivo:
                    print(linha)
            
            elif escolha == 2:
                
                opção_2 = ''

                while opção_2 != 's':
                    try:
                        # i é linhas_metas e ii é linhas_metas_concluidas, z é linha_formatada
                        nova_meta = str(input('Defina uma nova meta pessoal: '))
                        nova_meta.capitalize()
                        
                        arquivo = open('metas.txt','r')
                        metas_arquivo = arquivo.readlines()
                        linha_metas = len(metas_arquivo)
                        arquivo.close()
                        

                        arquivo = open('metas.txt', 'a')
                        arquivo.write(f'{linha_metas}. {nova_meta}\n')
                        arquivo.close()

                        print('Nova meta definida!! Caso queira adiconar outra meta digite qualquer letra, Caso queira sair aperte a tecla "s":   ')
                        opção_2 = input('Selecione uma opção: ')

                        opção_2.lower()
                    except:
                        print('Digite uma meta válida')

            elif escolha == 3:

                opção_3 = ''

                while opção_3 != 's':
                    for linha in metas_arquivo:
                        print(linha)

                    try:    

                        index_meta = int(input('Selecione a meta que deseja alterar: '))
                        nova_meta = input('Digite a nova meta: ')

                        metas_arquivo[index_meta] = ((f'{index_meta}. ') + nova_meta )

                        arquivo_alterar = open('metas.txt','w')
                        for linha in metas_arquivo:
                            linha_formatada = linha.strip()
                            arquivo_alterar.write(f'{linha_formatada} \n')
                        arquivo_alterar.close()

                        print('Meta alterada com sucesso!! Caso queira alterar outra meta digite qualquer letra:  ')
                        print('Caso queira sair aperte a tecla "s" ')

                        opção_3 = input('Selecione uma opção: ')

                        opção_3.lower()
                    except ValueError:
                        print('Por favor digite um número inteiro')
                    except IndexError:
                        print('Por favor digite um número contido na li')


            elif escolha == 4:
                            
                opção_4 = ''

                while opção_4 != 's':
                    for linha in metas_arquivo:
                        print(linha)
                    try:
                        deletar = int(input('Selecione a meta que você deseja deletar: '))
                        metas_arquivo.pop(deletar)

                        arquivo_alterar = open('metas.txt','w')

                        for indice, linha in enumerate(metas_arquivo):
                            y = linha[3:].strip()
                            arquivo_alterar.write(f'{indice}. {y} \n')
                        arquivo_alterar.close()
                        
                        print('Meta deletada com sucesso!! Caso queira deletar outra meta digite qualquer letra:  ')
                        print('Caso queira sair aperte a tecla "s" ')
                        opção_4 = input('Selecione uma opção: ')

                        opção_4.lower()
                    except ValueError:
                        print('Por favor digite um número inteiro')
                    except IndexError:
                        print('Por favor digite um número contido na lista')

            elif escolha == 5:
                            
                opção_5 = ''

                while opção_5 != 's':
                    for linha in metas_arquivo:
                        print(linha)
                    try:
                        deletar = int(input('Selecione a meta que você deseja concluir: '))
                        c = metas_arquivo[deletar]
                        concluida = c[3:].strip()
                        metas_arquivo.pop(deletar)

                        arquivo_alterar = open('metas.txt','w')

                        for indice, linha in enumerate(metas_arquivo):
                            y = linha[3:].strip()
                            arquivo_alterar.write(f'{indice}. {y} \n')
                        arquivo_alterar.close()

                        arquivo = open('metas_concluidas.txt', 'a')
                        arquivo.write(f'{linha_metas_concluidas}. {concluida}\n')
                        arquivo.close()

                        print('Meta concluida com sucesso!! Caso queira concluir outra meta digite qualquer letra:  ')
                        print('Caso queira sair aperte a tecla "s" ')

                        opção_5 = input('Selecione uma opção: ')
                        
                    except:
                        print('Valor inválido')

            elif escolha == 6:
                for linha in metas_arquivo_concluído:
                    print(linha)

            elif escolha == 7:
                opção_7 = ''
                while opção_7 != 's':
                    for linha in metas_arquivo_concluído:
                        print(linha)
                    try:
                        deletar_concluido = int(input('Selecione a meta que você deseja deletar: '))
                        metas_arquivo_concluído.pop(deletar_concluido)

                        arquivo_alterar = open('metas_concluidas.txt','w')

                        for indice, linha in enumerate(metas_arquivo_concluído):
                            l = linha[3:].strip()
                            arquivo_alterar.write(f'{indice}. {l} \n')
                        arquivo_alterar.close()
                        
                        print('Meta deletada com sucesso!! Caso queira deletar outra meta digite qualquer letra:  ')
                        print('Caso queira sair aperte a tecla "s" ')
                        opção_7 = input('Selecione uma opção: ')

                        opção_7.lower()
                    except ValueError:
                        print('Por favor digite um número inteiro')
                    except IndexError:
                        print('Por favor digite um número contido na lista')

            elif escolha == 8:
                print('Finalizando programa.')
                break       
            
            else:
                print('Escreva um número na lista: ')
        
        except ValueError:
            print('Por favor digite um número inteiro')



i = 0
while i == 0:
    try:
        pergunta = int(input("Digite um número: \n1 para registrar dados\n2 para um treino aleátorio\n3 para deletar dados\n4 para atualizar dados\n5 para filtrar os treinos\n6 para fazer metas pessoais\n7 extra\n8 para sair\n"))
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
            print(metas_pessoais())
        elif pergunta == 7:
            pass
        elif pergunta == 8:
            i+=1
        else:
            print("Opção inválida. Tente novamente.\n")
        continuacao = input("Voce quer continuar: Digite '1' para parar, todas as outras respostas, o código vai continuar\n")
        if continuacao == '1':
            i +=1
    except ValueError:
        print("Erro: Digite um número válido.\n")
        continuacao = input("Voce quer continuar: Digite '1' para parar, todas as outras respostas, o código vai continuar\n")
        if continuacao == '1':
            i +=1