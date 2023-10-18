from PyQt6.QtWidgets import QMainWindow, QTabWidget, QLabel
from ControlPanel import ControlPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Heizungssteuerung")


        tab_widget = QTabWidget()

        tab_control = ControlPanel()
        tab_widget.addTab(tab_control, "ControlPanel")


        tab_temp = QLabel("Inhalt für Tab 2")
        tab_widget.addTab(tab_temp, "Temperaturverlauf")

        tab_anlage = QLabel("Inhalt für Tab 3")
        tab_widget.addTab(tab_anlage, "Heizungsanlage")


        self.setCentralWidget(tab_widget)