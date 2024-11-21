def metas_pessoais():
    """
    Gerencia metas pessoais, permitindo visualizar, adicionar, alterar, concluir, 
    e excluir metas, além de visualizar e gerenciar metas concluídas.

    O programa funciona em um loop contínuo até o usuário optar por sair.

    Recursos principais:
    - Visualizar as metas atuais.
    - Definir novas metas.
    - Alterar uma meta existente.
    - Excluir uma meta.
    - Concluir uma meta e movê-la para o arquivo de metas concluídas.
    - Visualizar metas concluídas.
    - Excluir metas concluídas.

    Entradas:
    O programa solicita números e informações textuais dependendo da funcionalidade selecionada.

    Arquivos usados:
    - 'metas.txt': Armazena as metas atuais.
    - 'metas_concluidas.txt': Armazena as metas concluídas.
    """
    
    print("Entrando nas metas pessoais")
    
    while True:
        # Tenta abrir o arquivo de metas e armazená-las em uma lista
        try:
            arquivo = open('metas.txt', 'r', encoding='utf-8')
            metas_arquivo = arquivo.readlines()
            arquivo.close()
        except FileNotFoundError:
            print("Erro: O arquivo 'metas.txt' não foi encontrado.")
            return
        except IOError:
            print("Erro ao acessar o arquivo 'metas.txt'.")
            return

        # Tenta abrir o arquivo de metas concluídas e armazená-las em uma lista
        try:
            arquivo = open('metas_concluidas.txt', 'r', encoding='utf-8')
            metas_arquivo_concluído = arquivo.readlines()
            linha_metas_concluidas = len(metas_arquivo_concluído) + 1  # Contagem para indexação
            arquivo.close()
        except FileNotFoundError:
            print("Erro: O arquivo 'metas_concluidas.txt' não foi encontrado.")
            return
        except IOError:
            print("Erro ao acessar o arquivo 'metas_concluidas.txt'.")
            return

        # Exibe o menu de opções
        print(
            '1. Visualizar as metas atuais:\n'
            '2. Definir novas metas:\n'
            '3. Alterar uma meta:\n'
            '4. Deletar uma meta:\n'
            '5. Concluir uma meta:\n'
            '6. Checar as metas concluídas:\n'
            '7. Deletar uma meta concluída:\n'
            '8. Fechar o programa:\n'
        )
        try:
            # Solicita ao usuário que escolha uma opção
            escolha = int(input('Selecione uma opção: '))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")
            continue

        # Opção 1: Visualizar metas atuais
        if escolha == 1:
            try:
                for linha in metas_arquivo:
                    print(linha)
                input("\nEscreva qualquer coisa para sair\n")
                print("Voltando ao menu\n")
            except Exception as e:
                print(f"Erro inesperado ao exibir as metas: {e}")

        # Opção 2: Definir novas metas
        elif escolha == 2:
            opção_2 = ''
            while opção_2 != '-1':
                try:
                    nova_meta = input('Defina uma nova meta pessoal: (Coloque "-1" para sair)\n')
                    if nova_meta == '-1':
                        print("Saindo sem definir metas.")
                        opção_2 = '-1'
                    else:
                        try:
                            # Conta as linhas existentes para determinar o índice
                            arquivo = open('metas.txt', 'r', encoding='utf-8')
                            metas_arquivo = arquivo.readlines()
                            linha_metas = len(metas_arquivo) + 1
                            arquivo.close()
                        except FileNotFoundError:
                            linha_metas = 1
                        except IOError:
                            print("Erro ao acessar o arquivo 'metas.txt'.")
                            break

                        # Adiciona a nova meta no arquivo
                        try:
                            arquivo = open('metas.txt', 'a', encoding='utf-8')
                            arquivo.write(f'{linha_metas}. {nova_meta}\n')
                            arquivo.close()
                        except IOError:
                            print("Erro ao gravar no arquivo 'metas.txt'.")
                            break

                        print('Nova meta definida! Caso queira adicionar outra, digite qualquer letra. Para sair, digite "-1".')
                        opção_2 = input('Selecione uma opção: \n')
                except Exception as e:
                    print(f"Erro inesperado ao definir nova meta: {e}")

        # Opção 3: Alterar uma meta
        elif escolha == 3:
            opção_3 = ''
            while opção_3 != '-1':
                try:
                    for linha in metas_arquivo:
                        print(linha)
                    index_meta = int(input('Selecione a meta que deseja alterar: (coloque "-1" para sair)\n'))
                    if index_meta == -1:
                        print("Saindo sem alterar metas.")
                        opção_3 = '-1'
                    else:
                        nova_meta = input('Digite a nova meta: (coloque "-1" para sair)\n')
                        
                        if nova_meta == '-1':
                            print("Saindo sem alterar metas.")
                            opção_3 = '-1'
                        else:
                            # Atualiza a meta selecionada
                            metas_arquivo[index_meta - 1] = f'{index_meta}. {nova_meta}'
                            try:
                                arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                                for linha in metas_arquivo:
                                    arquivo_alterar.write(f'{linha.strip()}\n')
                                arquivo_alterar.close()
                            except IOError:
                                print("Erro ao atualizar o arquivo 'metas.txt'.")
                                break
                            print('Meta alterada com sucesso! Para alterar outra, digite qualquer letra. Para sair, digite "-1".')
                            opção_3 = input('Selecione uma opção: \n')
                except ValueError:
                    print('Erro: Por favor, digite um número inteiro.')
                except IndexError:
                    print('Erro: Número fora do intervalo de metas disponíveis.')
                except Exception as e:
                    print(f"Erro inesperado ao alterar a meta: {e}")

                # Opção 4: Deletar uma meta
        elif escolha == 4:
            opção_4 = ''
            while opção_4 != '-1':
                try:
                    for linha in metas_arquivo:
                        print(linha)
                    deletar = int(input('Selecione a meta que você deseja deletar: (coloque -1 para sair)\n'))
                    if deletar == -1:
                        print("Saindo sem deletar metas.")
                        opção_4 = '-1'
                    else:
                        # Remove a meta escolhida da lista
                        metas_arquivo.pop(deletar - 1)
                        try:
                            # Reescreve o arquivo com os novos índices
                            arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                            for indice, linha in enumerate(metas_arquivo, start=1):
                                Linha_sem_indice = linha[3:].strip() # Isso tira o indice aterior, as 3 primeiras coisas da linha e pemiti botar um indice novo
                                arquivo_alterar.write(f'{indice}. {Linha_sem_indice} \n') #Resccreve o código com o indice e o resto da linha
                            arquivo_alterar.close()
                        except IOError:
                            print("Erro ao atualizar o arquivo 'metas.txt'.")
                            break
                        print('Meta deletada com sucesso! Para deletar outra, digite qualquer letra. Para sair, digite "-1".')
                        opção_4 = input('Selecione uma opção: \n')
                except ValueError:
                    print('Erro: Por favor, digite um número inteiro.')
                except IndexError:
                    print('Erro: Número fora do intervalo de metas disponíveis.')
                except Exception as e:
                    print(f"Erro inesperado ao deletar a meta: {e}")

        # Opção 5: Concluir uma meta
        elif escolha == 5:
            opção_5 = ''
            while opção_5 != '-1':
                try:
                    for linha in metas_arquivo:
                        print(linha)
                    concluir = int(input("Selecione a meta que você deseja concluir: (Coloque '-1' para sair)\n"))
                    if concluir == -1:
                        print("Saindo sem concluir metas.")
                        opção_5 = '-1'
                    else:
                        # Move a meta para o arquivo de metas concluídas
                        linha_concluida = metas_arquivo[concluir - 1]
                        Linha_sem_indice = linha_concluida[3:].strip() # Isso tira o indice aterior, as 3 primeiras coisas da linha e pemiti botar um indice novo
                        metas_arquivo.pop(concluir - 1)
                        try:
                            # Atualiza o arquivo de metas
                            arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                            for indice, linha in enumerate(metas_arquivo, start=1):
                                Linha_sem_indice_atual = linha[3:].strip() # Isso tira o indice aterior, as 3 primeiras coisas da linha e pemiti botar um indice novo
                                arquivo_alterar.write(f'{indice}. {Linha_sem_indice_atual} \n')
                            arquivo_alterar.close()
                        except IOError:
                            print("Erro ao salvar no arquivo 'metas.txt'.")
                            break
                        try:
                            # Adiciona ao arquivo de metas concluídas
                            arquivo = open('metas_concluidas.txt', 'a', encoding='utf-8')
                            arquivo.write(f'{linha_metas_concluidas}. {Linha_sem_indice}\n')
                            arquivo.close()
                        except IOError:
                            print("Erro ao salvar no arquivo 'metas_concluidas.txt'.")
                            break
                        print('Meta concluída com sucesso! Para concluir outra, digite qualquer letra. Para sair, digite "-1".')
                        opção_5 = input('Selecione uma opção: ')
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
                except IndexError:
                    print("Erro: O índice está fora do intervalo válido.")
                except Exception as e:
                    print(f"Erro inesperado: {e}")

        # Opção 6: Checar metas concluídas
        elif escolha == 6:
            try:
                for linha in metas_arquivo_concluído:
                    print(linha)
                input("\nEscreva qualquer coisa para sair\n")
                print("Voltando ao menu\n")
            except FileNotFoundError:
                print("Erro: Arquivo 'metas_concluidas.txt' não encontrado.")
            except IOError:
                print("Erro ao acessar o arquivo 'metas_concluidas.txt'.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        # Opção 7: Deletar uma meta concluída
        elif escolha == 7:
            try:
                opção_7 = ''
                while opção_7 != '-1':
                    try:
                        for linha in metas_arquivo_concluído:
                            print(linha)
                        deletar_concluido = int(input('Selecione a meta que você deseja deletar: (Coloque "-1" para sair)\n'))
                        if deletar_concluido == -1:
                            opção_7 = '-1'
                            print('Saindo sem deletar as metas concluídas.')
                        else:
                            metas_arquivo_concluído.pop(deletar_concluido - 1)
                            try:
                                # Atualiza o arquivo de metas concluídas
                                arquivo_alterar = open('metas_concluidas.txt', 'w', encoding='utf-8')
                                for indice, linha in enumerate(metas_arquivo_concluído, start=1):
                                    Linha_sem_indice = linha[3:].strip() # Isso tira o indice aterior, as 3 primeiras coisas da linha e pemiti botar um indice novo
                                    arquivo_alterar.write(f'{indice}. {Linha_sem_indice} \n')
                                arquivo_alterar.close()
                            except IOError:
                                print("Erro ao salvar no arquivo 'metas_concluidas.txt'.")
                                break
                            print('Meta deletada com sucesso! Para deletar outra, digite qualquer letra. Para sair, digite "-1".')
                            opção_7 = input('Selecione uma opção: ')
                    except ValueError:
                        print("Por favor, insira um número inteiro válido.")
                    except IndexError:
                        print("Erro: O índice está fora do intervalo válido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        # Opção 8: Sair do programa
        elif escolha == 8:
            try:
                print('Finalizando programa.')
                break
            except Exception as e:
                print(f"Erro inesperado ao finalizar o programa: {e}")

        # Opção inválida
        else:
            try:
                print('Escreva um número válido na lista: ')
            except Exception as e:
                print(f"Erro inesperado ao exibir a mensagem de erro: {e}")
