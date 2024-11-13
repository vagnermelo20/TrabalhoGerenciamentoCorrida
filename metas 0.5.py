def Metas_pessoais():
    while True:

        arquivo = open('metas.txt','r')
        metas_arquivo = arquivo.readlines()
        arquivo.close()

        print('1. Visualizar as metas atuais: \n'
              '2. Definir novas metas: \n' 
              '3. Alterar uma meta: \n'
              '4. Deletar uma meta: \n'
              '5. Fechar o programa: \n')

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
                    arquivo.write('\n')
                    arquivo.write(f'{i}. {nova_meta}')
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

        elif escolha == 4:
                        
            opção_4 = ''

            while opção_4 != 's':
                for linha in metas_arquivo:
                    print(linha)

                deletar = int(input('Selecione a meta que você deseja deletar: '))
                metas_arquivo.pop(deletar)

                arquivo_alterar = open('metas.txt','w')
                for linha in metas_arquivo:
                    z = linha.strip()
                    arquivo_alterar.write(f'{z} \n')
                arquivo_alterar.close()
                
                print('Meta deletada com sucesso!! Caso queira deletar outra meta digite qualquer letra:  ')
                print('Caso queira sair aperte a tecla "s" ')
                opção_4 = input('Selecione uma opção: ')

                opção_4.lower()

        elif escolha == 5:
            print('Finalizando programa.')
            break        
