from database.dao import DAO
import networkx as nx

from model import hub


class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None




    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self._grafo = nx.Graph() #semplice non orientato
        lista_oggetti_hub = DAO.get_all_nodes()
        self._dizionario_hub= {}
        for hub in lista_oggetti_hub: #per ogni oggetto hub della lista
            self._dizionario_hub[hub.id] = hub  #assegna nel dizionario una voce con chiave id e oggetto hub
        self._grafo.add_nodes_from(lista_oggetti_hub) # aggiunge tutti gli hub come nodi del grafo
        self._edges = DAO.read_all_edges()
        for tratta in self._edges: #scorre tutte le tratte
            if tratta.guadagno_medio >= threshold: #solo se il guadagno medio supera la soglia
                hub_A = self._dizionario_hub[tratta.id_hub_origine] #ottengo oggetto corrispondente a id_hub_origine
                hub_B = self._dizionario_hub[tratta.id_hub_destinazione]
                self._grafo.add_edge(hub_A, hub_B, weight=tratta.guadagno_medio)#aggiunge arco tra i due nodi hub_A e hub_B, con il peso impostato a guadagno_medio
        return self._grafo #restituisce grafo



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self._grafo.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self._grafo.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self._edges

