import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QDial, QLCDNumber


class SteuerElement(QWidget):
    def __init__(self, raum, soll_temp, ist_temp):
        super().__init__()

        layout = QVBoxLayout()

        self.label_raum = QLabel(raum)
        layout.addWidget(self.label_raum)

        # Soll-Temperatur als LCDNumber
        self.lcd_soll_temp = QLCDNumber()
        self.lcd_soll_temp.display(soll_temp)
        layout.addWidget(self.lcd_soll_temp)

        # Ist-Temperatur als LCDNumber
        self.lcd_ist_temp = QLCDNumber()
        self.lcd_ist_temp.display(ist_temp)
        layout.addWidget(self.lcd_ist_temp)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.dial.setMinimum(11)  # Setzt den minimalen Wert
        self.dial.setMaximum(35)  # Setzt den maximalen Wert
        layout.addWidget(self.dial)

        self.dial.valueChanged.connect(self.dial_changed)

        self.resize(200, 300)

        self.setLayout(layout)

    def dial_changed(self, value):
        self.lcd_soll_temp.display(value)  # Aktualisiert die angezeigte Soll-Temperatur

def main():
    app = QApplication(sys.argv)

    # Text für Labels und anfängliche Temperaturen
    raum = 'Wohnzimmer'
    soll_temp = 22  # als Zahl, nicht als String
    ist_temp = 23  # als Zahl, nicht als String

    widget = SteuerElement(raum, soll_temp, ist_temp)
    widget.show()
    sys.exit(app.exec())

