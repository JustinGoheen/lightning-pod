import sys
import lightning as L
from app import DashFlow
from pprint import pprint

from dash import Dash, html
import dash_cytoscape as cyto


class DashUI(L.LightningWork):
    def __init__(self):
        super().__init__()

    def run(self, tree):
        app = Dash(__name__)

        app.layout = html.Div([
            html.P("Dash Cytoscape:"),
            cyto.Cytoscape(
                id='cytoscape',
                elements=[{'data': {"label": list(tree.keys())}}],
                layout={'name': 'breadthfirst'},
                style={'width': '400px', 'height': '500px'}
            )
        ])

        app.run_server(host=self.host, port=self.port)



class Tree(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.uiw = DashUI()
        self.target_flow = DashFlow()
        self.show_works = True

    def run(self):
        branches = dict()
        for flow in self.flows:
            flowobj = getattr(self, flow)
            fnw = flowobj.named_works()
            fnw = {w[0]: {hex(id(w[1])): w[1].__class__.__name__} for w in fnw}
            branch = {flowobj.__class__.__name__: fnw}
            branches.update(branch)
        tree = {self.__class__.__name__: branches}
        self.uiw.run(tree)
        #     print()
        #     pprint(tree)
        #     print()
        #     self.show_works = False
        # sys.exit()

    def configure_layout(self):
        tab1 = {"name": "home", "content": self.uiw}
        return tab1

app = L.LightningApp(Tree())

        