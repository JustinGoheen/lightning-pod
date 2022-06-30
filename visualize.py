import sys
import lightning as L
from app import DashFlow
from pprint import pprint

from dash import Dash, html
import dash_cytoscape as cyto
import networkx as nx


class DashUI(L.LightningWork):
    def run(self, tree):
        app = Dash(__name__)

        G = nx.from_dict_of_dicts(tree)
        nxcd = nx.cytoscape_data(G) 
        for node in nxcd['elements']['nodes']:
            node['data']['label'] = node['data'].pop('name')
        pprint(nxcd)


        app.layout = html.Div([
            html.P("Dash Cytoscape:"),
            cyto.Cytoscape(
                id='cytoscape',
                elements=nxcd['elements'],
                # layout={'name': 'breadthfirst'}
            )
        ])

        app.run_server(host=self.host, port=self.port)



class Tree(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.uiw = DashUI(parallel=True)
        self.target_flow = DashFlow()
        self.show_works = True

    def run(self):
        tfname = self.target_flow.__class__.__name__
        tree = {tfname: {}}
        if self.show_works:
            for flow in self.flows:
                flowobj = getattr(self, flow)
                fnw = flowobj.named_works()
                print(fnw)
                fnw = {w[0]: w[1].__class__.__name__ for w in fnw}
                branch = {flowobj.__class__.__name__: fnw}
                print("branch")
                print(branch)
                tree.update(branch)
            apptree = {"App": tree}
            self.uiw.run(apptree)
            self.show_works = False

    def configure_layout(self):
        tab1 = {"name": "home", "content": self.uiw}
        return tab1

app = L.LightningApp(Tree())

        