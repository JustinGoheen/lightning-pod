import lightning as L
import dearpygui.dearpygui as dpg


class UserInterfaceWorker(L.LightningWork):
    def run(self):
        dpg.create_context()
        dpg.create_viewport(title="Custom Title", width=600, height=300)

        with dpg.window(label="Example Window"):
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()


class RootFlow(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.uiw = UserInterfaceWorker(parallel=True)

    def run(self):
        self.uiw.run()

    def stop(self):
        dpg.destroy_context()


app = L.LightningApp(RootFlow())
