def atualizar_treinos():
    dados = obter_dados()

    if not  dados:
        print('Não encontramos esse treino!')
    print('\nLista de Treinos:')
    for i, treino in enumerate(dados):
        print(f'{i+1}. {treino[0]} - {treino[1]} km - {treino[2]} min')
    try:
        escolha = int(input('Escolha o numero do treino que deve ser atualizado: '))
        if  1 <= escolha <= len(dados):
            treino = dados[escolha-1]
            print(f'\nAtualizando treino de {treino[0]}:')
            nova_data = input(f'Data (atual: {treino[0]}) ou Enter para manter: ')
            nova_distancia = input(f'Distância em km (atual: {treino[1]}) ou Enter para manter: ')
            novo_tempo = input(f'Tempo em minutos (atual: {treino[2]}) ou Enter para manter: ')
            nova_localizacao = input(f'Localização (atual: {treino[3]}) ou Enter para manter: ')
            novo_clima = input(f'Clima (atual: {treino[4]}) ou Enter para manter: ')

            treino[0] = nova_data if nova_data else treino[0]
            treino[1] = float(nova_distancia) if nova_distancia else treino[1]
            treino[2] = float(novo_tempo) if novo_tempo else treino[2]
            treino[3] = nova_localizacao if nova_localizacao else treino[3]
            treino[4] = novo_clima if novo_clima else treino[4]

            obter_dados(dados)
            print('Treino atualizado com sucesso!')
        else:
            print('opcao invalida, tente novamente!')

    except ValueError:
        print('digite um valor valido!')
    except IndexError:
        print('numero fora do intervalo')

    
