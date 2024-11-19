def Metas_pessoais():
    while True:

        arquivo = open('metas.txt','r')
        metas_arquivo = arquivo.readlines()
        arquivo.close()

        arquivo = open('metas_concluidas.txt','r')
        metas_arquivo_concluído = arquivo.readlines()
        ii = len(metas_arquivo_concluído)
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
                        
                        nova_meta = str(input('Defina uma nova meta pessoal: '))
                        nova_meta.capitalize()
                        
                        arquivo = open('metas.txt','r')
                        metas_arquivo = arquivo.readlines()
                        i = len(metas_arquivo)
                        arquivo.close()
                        

                        arquivo = open('metas.txt', 'a')
                        arquivo.write(f'{i}. {nova_meta}\n')
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
                            z = linha.strip()
                            arquivo_alterar.write(f'{z} \n')
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

                    if len(metas_arquivo) == 0:
                        print('Nenhuma meta adicionada')
                        break
                    else:
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
                        arquivo.write(f'{ii}. {concluida}\n')
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
