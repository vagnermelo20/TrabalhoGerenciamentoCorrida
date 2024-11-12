def Metas_pessoais():
    while True:

        print('1. Visualizar as metas atuais: \n'
              '2. Definir novas metas: \n' 
              '3. Alterar uma meta: \n'
              '4. Deletar uma meta: \n'
              '5. Fechar o programa: \n')

        escolha = int(input('Selecione uma opção: '))

        metas = ['a']

        if escolha == 1:
            arquivo = open('metas.txt','r')
            print(arquivo.read())
            arquivo.close()
        
        elif escolha == 2: # Não está entrando na lista
            
            opção_2 = ''

            while opção_2 != 's':
                try:
                    nova_meta = str(input('Defina uma nova meta pessoal: '))

                    nova_meta.capitalize()

                    # linhas = arquivo.readlines() falta adicionar a função de checar se alguma meta foi repitida
                    
                    

                    arquivo = open('metas.txt', 'a')
                    arquivo.write(nova_meta + '\n')
                    arquivo.close()

                    print('Nova meta definida!! Caso queira adiconar outra meta digite qualquer letra:  ')
                    print('Caso queira sair aperte a tecla "s" ')
                    opção_2 = input('Selecione uma opção: ')

                    opção_2.lower()
                except:
                    print('Digite uma meta válida')

        elif escolha == 3:

            opção_3 = ''

            while opção_3 != 's':

                for meta in metas:
                    print(meta)

                index_meta = int(input('Selecione a meta que deseja alterar: '))
                nova_meta = input('Digite a nova meta: ')

                metas[index_meta] = nova_meta

                print('Meta alterada com sucesso!! Caso queira alterar outra meta digite qualquer letra:  ')
                print('Caso queira sair aperte a tecla "s" ')

                opção_3 = input('Selecione uma opção: ')

                opção_3.lower()

        elif escolha == 4:
                        
            opção_4 = ''

            while opção_4 != 's':
                deletar = int(input('Selecione a meta que você deseja deletar: '))
                metas.pop(deletar+1)
                print('Meta deletada com sucesso!! Caso queira deletar outra meta digite qualquer letra:  ')
                print('Caso queira sair aperte a tecla "s" ')
                opção_4 = input('Selecione uma opção: ')

                opção_4.lower()

        elif escolha == 5:
            print('Finalizando programa.')
            break        

Metas_pessoais()
