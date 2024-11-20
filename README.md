# TrabalhoGerenciamentoCorrida

Este trabalho é um sistema de gerenciamento de corrida.
Ele consiste de várias funções que serão chamadas dentro de um while, nesse while a pessoa terá 9 opções: Poderá registrar os dados; fazer um treino aleátorio; deletar os dados; atualizar os dados, filtrar os treinos ou competições; conseguir um resumo estatistico dos treinos; fazer um resumo de gastos calórico;  fazer as metas pessoais; sair do while.
Esse metas pessoais é especial porque nele também há um while com 8 opções: Pode visualizar as metas atuais; definir novas metas; alterar metas; deletar metas; concluir metas; checar metas concluídas; deletar metas concluídas; sair do while.


# Dentro do while pincipal

Será feito uma pergunta para você digitar um número. Esse número pode ser de 1 a 9, qualquer coisa digitada que não seja isso, será considerado incorreto.

Se for colocado 1: Você irá adicionar novos dados no sistema. Você será perguntado se quer colocar 't' para Treino ou 'c' para competição (Qualquer outra coisa é inválido), você será perguntado para escrever a distância em quilometros(Pode ser inteiro ou decimal), o tempo em minutos(tem  que ser inteiro), o nome do local, a condição climática no tempo da atividade. Esse dados serão adicionados no arquivo "banco.txt".

se for colocado 2: Você irá para um treino aleátorio relacionado a velocidade média do último treino ou competição. Se ela for maior que 5 km/h: Ela será dada opções de treinos mais curtos, senão ela será dada opções de treinos mais longos.

se for colocado 3: você poderá escolher a linha que quer deletar, deletando-a no arquivo 'banco.txt'

se for colocado 4: você poderá escolher qual linha você quer atualizar, atualizando-a e botando no arquivo banco.txt.

ser for colocado 5: você poderá escolher se quer filtrar os arquivos por tempo ou distância, colocando 1 ou 2. Depois de forma crescente ou decrescente, colocando 1 ou 2.

se for colocado 6: Você terá um resumo dos treinos ou competições, que possuirá a maior distância percorrida, a menor distância percorrida, o maior tempo gasto, o menor tempo gasto e a velocidade média geral em km/h.

se for colocado 7: Você será perguntado sua velocidade média em km/h, seu peso em kg, quantos minutos voce gastou correndo. Ele dará uma estimativa de quantas calórias você perdeu nessa corrida.

Se for colocado 9: Você irá sair do programa

se for colocado 8: Você irá para as metas pessoais, nelas você pode escolher de 1 a 8

# dentro das metas pessoais
Você poderá escolher de 1 a 8

se escolher 1: Você poderá visualizar as metas atuais.

se escolher 2: Você poderá definir novas metas, que serão adicionadas no arquivo 'metas.txt'.

se escolher 3: Você poderá alterar uma meta: Será escolhido o id de uma meta e depois uma nova meta que irá substitui-la. Isso será substituido no arquivo 'metas.txt'.

se escolher 4: Você poderá deletar uma meta: Será escolhido o id de uma meta e ela será deletada do arquivo 'metas.txt'

se escolher 5: Você pode concluir uma meta: Será escolhido o id de uma meta e ela será deletada do arquivo 'metas.txt' e adicionada no aruqivo metas_concluidas.txt

se escolher 6: Você poderá visualizar as metas concluídas.

se escolher 7: Você poderá deletar uma meta: Será escolhido o id de uma meta concluida e ela será deletada do arquivo 'metas_concluidas.txt'

se escolher 8: Você irá sair do programa