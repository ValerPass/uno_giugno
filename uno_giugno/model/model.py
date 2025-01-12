from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodi = self.getAllGeni()

    def getAllGeni(self):
        return DAO.getAllGenes()

    def buildGrafo(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.nodi)
        archi = set(DAO.getArchi())
        for g1, g2, peso in archi:
            if g1 != g2:  # Evita cappi
                self.grafo.add_edge(g1, g2, weight=peso)

    def getVicini(self, geneID):
        vicini = {
            vicino: self.grafo[geneID][vicino]['weight']
            for vicino in self.grafo.neighbors(geneID)
        }
        self.viciniSorted = dict(sorted(vicini.items(), key=lambda x :x[1], reverse = True))
        return self.viciniSorted

    #def getViciniLISTA(self, geneID):
        # Ottieni i vicini e i pesi degli archi come lista di tuple
        #vicini = [
        #    (vicino, self.grafo[geneID][vicino]['weight'])
        #    for vicino in self.grafo.neighbors(geneID)
        #]
        # Ordina la lista per peso in ordine decrescente
        #vicini_sorted = sorted(vicini, key=lambda x: x[1], reverse=True)

        #return vicini_sorted

    def getDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)