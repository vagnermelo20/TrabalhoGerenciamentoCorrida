#                                                    TrabalhoGerenciamentoCorrida

Trabalho feito pelos Alunos da turma de CC-A <br> <br>
**Felipe Cavalcanti Melo Bezerra** <br>
**Guilherme  Cireno Baltar**<br>
**Leonardo de Queiroz Chavez Filho**<br>
**Tomás de Aquino Vieira Jamacaru**<br>
**Vagner Montenegro de melo**<br>





Este trabalho é um sistema de gerenciamento de corrida.
Ele consiste de várias funções que serão chamadas dentro de um while(while seria uma função pra fazer loop no python), nesse while a pessoa terá 9 opções: Poderá registrar os dados; fazer um treino aleátorio; deletar os dados; atualizar os dados, filtrar os treinos ou competições; conseguir um resumo estatistico dos treinos; fazer um resumo de gastos calórico;  fazer as metas pessoais; sair do loop


    Demonstração:
    
![image](https://github.com/user-attachments/assets/75fd5ba1-2619-4d9f-b4d3-e753ab4313cb)


Esse metas pessoais é especial porque nele também há um while com 8 opções: Pode visualizar as metas atuais; definir novas metas; alterar metas; deletar metas; concluir metas; deletar metas concluídas; visualizar metas concluídas; sair do loop.


![image](https://github.com/user-attachments/assets/edd26541-adcf-43dd-a165-dd3006d1372c)


Todos os dados salvos nos arquivos são salvos em linhas individuais e numerados a partir do número 1. Toda a vez que um dado é deletado, os outros irão continuar na estrutura numerada. ex: 


![image](https://github.com/user-attachments/assets/3bbd02d1-b546-4b09-832a-3a8a27970898)



  Se deletar o 3: O 4 vira 3 e o 5 vira 4. Ficando assim
            
![image](https://github.com/user-attachments/assets/e5b87101-d35c-4fa9-a97e-eb2a0238481a)
                                                        
                
#                                                   Dentro do programa principal

Será feito uma pergunta para você digitar um número. Esse número pode ser de 1 a 9, qualquer coisa digitada que não seja isso, será considerado incorreto.
Sempre que você reponder algo, voce pode escolher clicar 1 para sair do loop

![image](https://github.com/user-attachments/assets/8b52aeac-f81d-4d6a-8324-fbdb35181c8d)


Se for colocado 1: Você irá adicionar novos dados no sistema. Você será perguntado se quer colocar 't' para Treino ou 'c' para competição (Qualquer outra coisa é inválido), a data(tem que ser uma data real e na formatação que foi pedida que é **dd/mm/aaaa**, traduzido em dias, mês e anos), a distância em quilometros(Pode ser inteiro ou decimal), o tempo em minutos(tem que ser inteiro), o nome do local e a condição climática no tempo da atividade, esses 2 não podem ter números. Esse dados serão adicionados no arquivo "banco.txt". Esses dados serão tranformados e formatados para entrar no **banco.txt**, além de transformar os minutos em horas e minutos e os quilometros em quilometros e metros


ex: ![image](https://github.com/user-attachments/assets/432b0725-2488-4329-9a88-15deda49c54f)


se for colocado 2: Você irá para um treino aleátorio relacionado a velocidade média do último treino ou competição. Se ela for maior que 5 km/h: Ela será dada opções de treinos mais curtos, senão ela será dada opções de treinos mais longos.

se for colocado 3: você poderá escolher a linha que quer deletar, deletando-a no arquivo 'banco.txt'

se for colocado 4: você poderá escolher qual linha você quer atualizar, atualizando-a e botando no arquivo banco.txt.

ser for colocado 5: você poderá escolher se quer filtrar os arquivos por tempo ou distância, colocando 1 ou 2. Depois de forma crescente ou decrescente, colocando 1 ou 2.

![image](https://github.com/user-attachments/assets/98524d62-be73-4df4-8af4-02170d1b1a1e)





se for colocado 6: Você terá um resumo dos treinos ou competições, que possuirá a maior distância percorrida, a menor distância percorrida, o maior tempo gasto, o menor tempo gasto e a velocidade média geral em km/h.

se for colocado 7: Você será perguntado sua velocidade média em km/h, seu peso em kg, quantos minutos voce gastou correndo. Ele dará uma estimativa de quantas calórias você perdeu nessa corrida.

se for colocado 8: Você irá para as metas pessoais, nelas você pode escolher de 1 a 8

Se for colocado 9: Você irá sair do programa

# dentro das metas pessoais
Você poderá escolher de 1 a 8
Voce terá as opções de escolher '-1' pra voltar ao menu de metas pessoais a qualquer momento.

![image](https://github.com/user-attachments/assets/5d34bf87-4fcc-4765-b0ed-a115cf71395a)          ![image](https://github.com/user-attachments/assets/a597e5ff-5ba0-4ee6-90b4-9b31f2bbf114)        ![image](https://github.com/user-attachments/assets/01de379a-a9b4-4846-8426-227465b9c64d)



se escolher 1: Você poderá visualizar as metas atuais.

se escolher 2: Você poderá definir novas metas, que serão adicionadas no arquivo 'metas.txt'.

se escolher 3: Você poderá alterar uma meta: Será escolhido o id de uma meta e depois uma nova meta que irá substitui-la. Isso será substituido no arquivo 'metas.txt'.

se escolher 4: Você poderá deletar uma meta: Será escolhido o id de uma meta e ela será deletada do arquivo 'metas.txt'

se escolher 5: Você pode concluir uma meta: Será escolhido o id de uma meta e ela será deletada do arquivo 'metas.txt' e adicionada no aruqivo metas_concluidas.txt

se escolher 6: Você poderá deletar uma meta: Será escolhido o id de uma meta concluida e ela será deletada do arquivo 'metas_concluidas.txt'

se escolher 7: Você poderá visualizar as metas concluídas.

se escolher 8: Você irá sair do programa



Diretórios usados: O trabalho possui 3 arquivos .txt, 2 arquivos.py, em que o metas.py é importado para o trabalho.py e um arquivo README.md, além de um arquivo git.ignore do python, que foi colocado caso fosse necessário

![image](https://github.com/user-attachments/assets/963bffd2-b7ea-4731-81e4-11837f6ab2f5)

# fluxograma

https://miro.com/app/live-embed/uXjVLCe-M4c=/?moveToViewport=5015,-16,2040,957&embedId=88151455188