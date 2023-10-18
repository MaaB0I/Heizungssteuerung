from PyQt6.QtWidgets import QMainWindow
from ControlPanel import ControlPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Heizungssteuerung")


        control_panel = ControlPanel()
        self.setCentralWidget(control_panel)
