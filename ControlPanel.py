from PyQt6.QtWidgets import QWidget, QHBoxLayout
from SteuerElement import SteuerElement, CentralWidget


class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super(ControlPanel, self).__init__(parent)


        layout = QHBoxLayout(self)


        control_wohnzimmer = SteuerElement('Wohnzimmer', 22, 23)
        layout.addWidget(control_wohnzimmer)

        control_kueche = SteuerElement('Küche', 24, 25)
        layout.addWidget(control_kueche)

        control_schlafzimmer = SteuerElement('Schlafzimmer', 20, 21)
        layout.addWidget(control_schlafzimmer)

        control_bad = SteuerElement('Bad', 23, 24)
        layout.addWidget(control_bad)


        self.setLayout(layout)

class TemperatureCourse(QWidget):
    def __init__(self, parent=None):
        super(TemperatureCourse, self).__init__(parent)

        layout = QHBoxLayout(self)

        # Erstellen Sie hier Ihr zentrales Widget oder andere Widgets.
        self.central_widget = CentralWidget(parent)
        layout.addWidget(self.central_widget)

        # Fügen Sie hier zusätzliche Widgets zum Layout hinzu, falls erforderlich.
        # Beispiel: layout.addWidget(ein_anderes_widget)

        self.setLayout(layout)
        self.setWindowTitle("Einführung in QCharts")


