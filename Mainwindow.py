from PyQt6.QtWidgets import QMainWindow, QTabWidget, QLabel
from ControlPanel import ControlPanel, TemperatureCourse

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Heating Control")


        tab_widget = QTabWidget()

        tab_control = ControlPanel()
        tab_widget.addTab(tab_control, "Control Panel")


        tab_temp = TemperatureCourse()
        tab_widget.addTab(tab_temp, "Temperature course")

        tab_anlage = QLabel("Inhalt für Tab 3")
        tab_widget.addTab(tab_anlage, "Heatingsystem")


        self.setCentralWidget(tab_widget)