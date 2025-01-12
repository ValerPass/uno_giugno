import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        for g in self._model.nodi:
            self._view.ddgene.options.append(ft.dropdown.Option(g))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._model.buildGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato"))
        nNodes, nEdges = self._model.getDetails()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} vertici e {nEdges} archi"))
        self._view.update_page()

    def handle_genes(self, e):
        self._view.txt_result.controls.append(ft.Text(f"Geni adiacenti a: {self._view.ddgene.value}"))
        vicini = self._model.getVicini(self._view.ddgene.value)
        for k, v in vicini.items():
            self._view.txt_result.controls.append(ft.Text(f"{k} con peso {v}"))
        self._view.update_page()



