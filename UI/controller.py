import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        self._view.lista_visualizzazione.clean()
        grafo = self._model.costruisci_grafo(float(self._view.guadagno_medio_minimo.value)) #legge valore dalla view, lo passa come soglia a costruisci_grafo e assegna il grafo restituito alla variabile grafo
        tratte = grafo.edges(data = True)  #resistuisce tuple per ogni arco
        self._view.lista_visualizzazione.controls.append(ft.Row(controls = [ft.Text("numero di Tratte:"), ft.Text(str(self._model.get_num_edges()))]))
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("numero di Hubs:"), ft.Text(str(self._model.get_num_nodes()))]))

        #PER STAMPARE
        for partenza, arrivo, guadagno in tratte:
            guadagno = guadagno["weight"]
            stampa = f"{partenza.nome} | {arrivo.nome} | {guadagno:.2f}" #restituisci stringa formattata con nodo di partenza, nodo arrivo, e valore di guadagno
            self._view.lista_visualizzazione.controls.append(ft.Text(stampa))
            self._view.page.update()


