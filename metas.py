def metas_pessoais():
    print("Entrando nas metas pessoais ")
    while True:
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

        try:
            arquivo = open('metas_concluidas.txt', 'r', encoding='utf-8')
            metas_arquivo_concluído = arquivo.readlines()
            linha_metas_concluidas = len(metas_arquivo_concluído) + 1  # Para usar com o índice começando em 1
            arquivo.close()
        except FileNotFoundError:
            print("Erro: O arquivo 'metas_concluidas.txt' não foi encontrado.")
            return
        except IOError:
            print("Erro ao acessar o arquivo 'metas_concluidas.txt'.")
            return

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
        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")
            continue

        if escolha == 1:
            try:
                for linha in metas_arquivo:
                    print(linha)
                input("\nEscreva qualquer coisa para sair\n")
                print("Voltando ao menu\n")
            except Exception as e:
                print(f"Erro inesperado ao exibir as metas: {e}")

        elif escolha == 2:
            opção_2 = ''
            while opção_2 != 's':
                try:
                    nova_meta = str(input('Defina uma nova meta pessoal: (Coloque "s" para sair sem adicionar uma meta)\n')).lower()
                    if nova_meta == 's':
                        print("Saindo sem definir metas ")
                        opção_2 = 's'
                    else:
                        try:
                            arquivo = open('metas.txt', 'r', encoding='utf-8')
                            metas_arquivo = arquivo.readlines()
                            linha_metas = len(metas_arquivo) + 1
                            arquivo.close()
                        except FileNotFoundError:
                            linha_metas = 1
                        except IOError:
                            print("Erro ao acessar o arquivo 'metas.txt'.")
                            break

                        try:
                            arquivo = open('metas.txt', 'a', encoding='utf-8')
                            arquivo.write(f'{linha_metas}. {nova_meta}\n')
                            arquivo.close()
                        except IOError:
                            print("Erro ao gravar no arquivo 'metas.txt'.")
                            break

                        print('Nova meta definida!! Caso queira adicionar outra meta digite qualquer letra, Caso queira sair aperte a tecla "s":')
                        opção_2 = input('Selecione uma opção: \n').lower()
                except Exception as e:
                    print(f"Erro inesperado ao definir nova meta: {e}")

        elif escolha == 3:
            opção_3 = ''
            while opção_3 != 's':
                try:
                    for linha in metas_arquivo:
                        print(linha)
                    index_meta = int(input('Selecione a meta que deseja alterar: (coloque "-1" para sair)\n'))
                    if index_meta == -1:
                        print("Saindo sem alterar metas ")
                        opção_3 = 's'
                    else:
                        nova_meta = input('Digite a nova meta: (coloque "s" para sair)\n').lower()
                        if nova_meta == 's':
                            print("Saindo sem alterar metas ")
                            opção_3 = 's'
                        else:
                            metas_arquivo[index_meta - 1] = f'{index_meta}. {nova_meta}'
                            try:
                                arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                                for linha in metas_arquivo:
                                    arquivo_alterar.write(f'{linha.strip()}\n')
                                arquivo_alterar.close()
                            except IOError:
                                print("Erro ao atualizar o arquivo 'metas.txt'.")
                                break
                            print('Meta alterada com sucesso!! Caso queira alterar outra meta digite qualquer letra:')
                            opção_3 = input('Caso queira sair aperte a tecla "s": \n').lower()
                except ValueError:
                    print('Erro: Por favor digite um número inteiro.')
                except IndexError:
                    print('Erro: Número fora do intervalo de metas disponíveis.')
                except Exception as e:
                    print(f"Erro inesperado ao alterar a meta: {e}")

        elif escolha == 4:
            opção_4 = ''
            while opção_4 != 's':
                try:
                    for linha in metas_arquivo:
                        print(linha)
                    deletar = int(input('Selecione a meta que você deseja deletar: (coloque -1 para sair)\n'))
                    if deletar == -1:
                        print("Saindo sem deletar metas")
                        opção_4 = 's'
                    else:
                        metas_arquivo.pop(deletar - 1)
                        try:
                            arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                            for indice, linha in enumerate(metas_arquivo, start=1):
                                Linha_sem_indice = linha[3:].strip()
                                arquivo_alterar.write(f'{indice}. {Linha_sem_indice} \n')
                            arquivo_alterar.close()
                        except IOError:
                            print("Erro ao atualizar o arquivo 'metas.txt'.")
                            break
                        print('Meta deletada com sucesso!! Caso queira deletar outra meta digite qualquer letra:')
                        opção_4 = input('Caso queira sair aperte a tecla "s": \n').lower()
                except ValueError:
                    print('Erro: Por favor digite um número inteiro.')
                except IndexError:
                    print('Erro: Número fora do intervalo de metas disponíveis.')
                except Exception as e:
                    print(f"Erro inesperado ao deletar a meta: {e}")
        
        elif escolha == 5:
                opção_5 = ''
                while opção_5 != 's':

                        try:
                            arquivo = open('metas.txt', 'r', encoding='utf-8')
                            metas_arquivo = arquivo.readlines()
                            arquivo.close()
                        except FileNotFoundError:
                            print("Erro: Arquivo 'metas.txt' não encontrado.")
                            break
                        except IOError:
                            print("Erro ao acessar o arquivo 'metas.txt'.")
                            break

                        for linha in metas_arquivo:
                            print(linha)

                        try:
                            arquivo = open('metas_concluidas.txt', 'r', encoding='utf-8')
                            metas_arquivo_concluído = arquivo.readlines()
                            linha_metas_concluidas = len(metas_arquivo_concluído) + 1
                            arquivo.close()
                        except FileNotFoundError:
                            print("Erro: Arquivo 'metas_concluidas.txt' não encontrado.")
                            break
                        except IOError:
                            print("Erro ao acessar o arquivo 'metas_concluidas.txt'.")
                            break

                        try:
                            concluir = int(input("Selecione a meta que você deseja concluir: (Coloque '-1' para sair)\n"))
                            if concluir == -1:
                                print("Saindo sem concluir metas.")
                                opção_5 = 's'
                            else:
                                linha_concluida = metas_arquivo[concluir - 1]
                                Linha_sem_indice = linha_concluida[3:].strip()

                                metas_arquivo.pop(concluir - 1)

                                try:
                                    arquivo_alterar = open('metas.txt', 'w', encoding='utf-8')
                                    for indice, linha in enumerate(metas_arquivo, start=1):
                                        Linha_sem_indice_atual = linha[3:].strip()
                                        arquivo_alterar.write(f'{indice}. {Linha_sem_indice_atual} \n')
                                    arquivo_alterar.close()
                                except IOError:
                                    print("Erro ao salvar no arquivo 'metas.txt'.")
                                    break

                                try:
                                    arquivo = open('metas_concluidas.txt', 'a', encoding='utf-8')
                                    arquivo.write(f'{linha_metas_concluidas}. {Linha_sem_indice}\n')
                                    arquivo.close()
                                except IOError:
                                    print("Erro ao salvar no arquivo 'metas_concluidas.txt'.")
                                    break

                                print('Meta concluída com sucesso!! Caso queira concluir outra meta, digite qualquer letra. Caso queira sair, aperte a tecla "s".')
                                opção_5 = input('Selecione uma opção: ')
                        except ValueError:
                            print("Por favor, insira um número inteiro válido.")
                        except IndexError:
                            print("Erro: O índice está fora do intervalo válido.")
                        except Exception as e:
                          print(f"Erro inesperado: {e}")

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

        elif escolha == 7:
                try:
                    opção_7 = ''
                    while opção_7 != 's':
                        try:
                            arquivo = open('metas_concluidas.txt', 'r', encoding='utf-8')
                            metas_arquivo_concluído = arquivo.readlines()
                            arquivo.close()
                        except FileNotFoundError:
                            print("Erro: Arquivo 'metas_concluidas.txt' não encontrado.")
                            break
                        except IOError:
                            print("Erro ao acessar o arquivo 'metas_concluidas.txt'.")
                            break

                        for linha in metas_arquivo_concluído:
                            print(linha)
                        try:
                            deletar_concluido = int(input('Selecione a meta que você deseja deletar: (Coloque "-1" para sair)\n'))
                            if deletar_concluido == -1:
                                opção_7 = 's'
                                print('Saindo sem deletar as metas concluídas.')
                            else:
                                metas_arquivo_concluído.pop(deletar_concluido - 1)

                                try:
                                    arquivo_alterar = open('metas_concluidas.txt', 'w', encoding='utf-8')
                                    for indice, linha in enumerate(metas_arquivo_concluído, start=1):
                                        Linha_sem_indice = linha[3:].strip()
                                        arquivo_alterar.write(f'{indice}. {Linha_sem_indice} \n')
                                    arquivo_alterar.close()
                                except IOError:
                                    print("Erro ao salvar no arquivo 'metas_concluidas.txt'.")
                                    break

                                print('Meta deletada com sucesso!! Caso queira deletar outra meta, digite qualquer letra. Caso queira sair, aperte a tecla "s".')
                                opção_7 = input('Selecione uma opção: ')
                        except ValueError:
                            print("Por favor, insira um número inteiro válido.")
                        except IndexError:
                            print("Erro: O índice está fora do intervalo válido.")
                except Exception as e:
                    print(f"Erro inesperado: {e}")

        elif escolha == 8:
            try:
                print('Finalizando programa.')
                break
            except Exception as e:
                print(f"Erro inesperado ao finalizar o programa: {e}")

        else:
            try:
                print('Escreva um número válido na lista: ')
            except Exception as e:
                print(f"Erro inesperado ao exibir a mensagem de erro: {e}")
