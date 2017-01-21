
from settings import *
import gui.main

class MainApp(gui.main.MainAppGUI):
    def __init__(self, *arg, **kwargs):
        gui.main.MainAppGUI.__init__(self, *arg, **kwargs)



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

