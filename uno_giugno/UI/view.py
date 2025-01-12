import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddyear = None
        self.ddcountry = None
        self.txtN = None

        self.btn_graph = None
        self.btn_volume = None
        self.btn_path = None

        self.txt_result = None
        self.txtOut2 = None
        self.txtOut3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with some controls
        # self.ddyear = ft.Dropdown(label="Anno")
        # self.ddcountry= ft.Dropdown(label="Nazione")

        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)

        row1 = ft.Row([self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=0, spacing=5, padding=5, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

        self.ddgene = ft.Dropdown(label="Gene")
        self._controller.fillDD()
        self.btn_genes = ft.ElevatedButton(text="Geni adiacenti", on_click=self._controller.handle_genes)
        row2 = ft.Row([self.ddgene, self.btn_genes],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()



    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
