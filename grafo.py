class Grafo():
    def __init__(self):
        self.vertices = {}

    def imprimirGrafo(self):
        for i in self.vertices.keys():
            print(i, ' -> ', ' -> '.join([str(j) for j in self.vertices[i]]))

    # Para adicionar aresta entre dois vertices
    def adicionarAresta(self, v1, v2):

        # verifica se o vertice já existe
        if v1 in self.vertices.keys():
            self.vertices[v1].append(v2)
        else:
            # Senão insere um novo vertice
            self.vertices[v1] = [v2]


if __name__ == '__main__':
    grafo = Grafo()
    grafo.adicionarAresta(1, 2)
    grafo.adicionarAresta(4, 2)
    grafo.adicionarAresta(2, 3)
    grafo.adicionarAresta(5, 2)
    grafo.adicionarAresta(7, 1)

    grafo.imprimirGrafo()
