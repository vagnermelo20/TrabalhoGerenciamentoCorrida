# TrabalhoGerenciamentoCorrida

# funcao criar_dados
 
   Essa funcao criara os dados pro banco de dados.
  A primeira função que criamos foi a função criar_dados, essa funcao foi criada colocando as variaveis treinoOUcompeticao, data, distancia, tempo, localizacao e condicaoClimatica. Na variavel treinoOUcompeticao, se a pessoa colocar treino, retorna isso
   treino: data: {data}, distância percorrida: {distancia} km, tempo: {tempo} min, localização: {localizacao}, condições climáticas: {condicaoClimatica}\n" 
   se colocar competicao, so muda treino por competição.
   Essa função não será chamada pelo usuário.


# funcao salvar_no_banco

 Essa funcao salva os dados no banco de dados.
 ela cria uma variavel chamada entrada e coloca nela os dados da funcao criar_banco, adicionando o arquivo do banco de dados.
 Se abre o arquivo, adiciona nele os dados tranforma a liguagem em utf-8 para poder usar caracteres especiais.
 Recorda o conteúdo salvo no arquivo.
 Quando o usuário chamar a funcao salvar_no_banco e colocar os dados lá, os dados serão enviados para o banco de dados


# funcao obter_dados

Onde é colocado os input para adicionar os dados, depois os dados dessa funcao serão usados na funcao salvar_no_banco