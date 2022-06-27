import os
import dash
import torch
import lightning as L
import dearpygui.dearpygui as dpg


class UserInterfaceWorker(L.LightningWork):
    def run(self):
        pass


class RootFlow(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.uiw = UserInterfaceWorker(parallel=True)

    def run(self):
        self.uiw.run()

    def configure_layout(self):
        tab1 = {"name": "home", "content": self.uiw}
        return tab1


app = L.LightningApp(RootFlow())
