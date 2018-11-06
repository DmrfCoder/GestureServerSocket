import _thread

from model.gestureModel import GestureModel
from net.server import runServer
from ui.ui import Ui

if __name__ == '__main__':
    ui = Ui()
    model = GestureModel(ui)

    _thread.start_new_thread(runServer, (model,))
    ui.start()
