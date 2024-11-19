class Atividade:
    def __init__(self, tipo, data, distancia, tempo, localizacao, condicoes_climaticas):
        self.tipo = tipo
        self.data = data
        self.distancia = distancia
        self.tempo = tempo
        self.localizacao = localizacao
        self.condicoes_climaticas = condicoes_climaticas

    def __str__(self):
        return f"Tipo: {self.tipo}, Data: {self.data}, Distância: {self.distancia} km, Tempo: {self.tempo} min, Localização: {self.localizacao}, Condições Climáticas: {self.condicoes_climaticas}"

class SistemaAtividade:
    def __init__(self):
        self.atividades = []

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def filtrar_por_distancia(self, min_distancia, max_distancia):
        return [atividade for atividade in self.atividades if min_distancia <= atividade.distancia <= max_distancia]

    def filtrar_por_tempo(self, min_tempo, max_tempo):
        return [atividade for atividade in self.atividades if min_tempo <= atividade.tempo <= max_tempo]

    def exibir_atividades(self, atividades):
        if atividades:
            for atividade in atividades:
                print(atividade)
        else:
            print("Nenhuma atividade encontrada com os filtros especificados.")

    def carregar_atividades(self, nome_arquivo):
        try:
            with open(nome_arquivo, "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    tipo = dados[0]
                    data = dados[1]
                    distancia = float(dados[2])
                    tempo = int(dados[3])
                    localizacao = dados[4]
                    condicoes_climaticas = dados[5]
                    atividade = Atividade(tipo, data, distancia, tempo, localizacao, condicoes_climaticas)
                    self.adicionar_atividade(atividade)
        except FileNotFoundError:
            print(f"O arquivo {nome_arquivo} não foi encontrado.")
    
    def salvar_atividades(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            for atividade in self.atividades:
                linha = f"{atividade.tipo};{atividade.data};{atividade.distancia};{atividade.tempo};{atividade.localizacao};{atividade.condicoes_climaticas}\n"
                arquivo.write(linha)

if __name__ == "__main__":
    sistema = SistemaAtividade()

    
    sistema.carregar_atividades("banco.txt")

    
    if not sistema.atividades:
        sistema.adicionar_atividade(Atividade("Treino", "20/08/2024", 10.0, 60, "Centro", "Ensolarado"))
        sistema.adicionar_atividade(Atividade("Competição", "15/02/2024", 21.0, 120, "Praia", "Nublado"))
        sistema.adicionar_atividade(Atividade("Treino", "20/02/2000", 39.0, 129, "Recife", "Boa"))
        sistema.salvar_atividades("banco.txt")

    
    print("Filtrando atividades por distância (10 km a 40 km):")
    atividades_filtradas_distancia = sistema.filtrar_por_distancia(10, 40)
    sistema.exibir_atividades(atividades_filtradas_distancia)

    print("\nFiltrando atividades por tempo (60 min a 130 min):")
    atividades_filtradas_tempo = sistema.filtrar_por_tempo(60, 130)
    sistema.exibir_atividades(atividades_filtradas_tempo)
