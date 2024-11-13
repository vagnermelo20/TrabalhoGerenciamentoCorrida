def excluir_treinos():
    dados = obter_dados()
    if not dados:
        print('Esse treino ja nao existe!')
    
    print('\nLista de Treinos:')
    for i, treino in enumerate(dados):
        print(f'{i+1}. {treino[0]} - {treino[1]} km - {treino[2]} min')
    try:
        escolha = int(input('\ndigite o numero do treino que deve ser excluido'))

        if 1<=escolha<=len(dados):
            treino_excluido = dados.pop(escolha-1)
            obter_dados(dados)
            print(f'Treino de {treino_excluido[0]} excluído com sucesso!')
        else:
            print('Opção inválida. Nenhum treino foi excluído.')
    except ValueError:
        print('digite um numero valido')


