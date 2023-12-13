import sys
from xmlrpc.client import DateTime
from DateTime import DateTime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QDial, QLCDNumber, QHBoxLayout, QSlider
from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget


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

class CentralWidget(QWidget):

    send_random = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.datetime = DateTime(parent)
        self.send_random.connect(self.datetime.add_random_value)

        self.slider = QSlider()
        self.slider.setRange(-5, 5)
        self.slider.valueChanged.connect(self.datetime.add_value)

        layout = QHBoxLayout()

        layout.addWidget(self.datetime)
        layout.addWidget(self.slider)

        self.setLayout(layout)

class ChartView(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        series = QSplineSeries()
        series2 = QLineSeries()

        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")
        chart.addSeries(series)
        chart.addSeries(series2)

        axis_x = QValueAxis()
        axis_x.setRange(1, 4)

        axis_y = QValueAxis()
        axis_y.setRange(0, 10)

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignTop)
        series.attachAxis(axis_x)
        series2.attachAxis(axis_x)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)
        series2.attachAxis(axis_y)

        series2.attachAxis(axis_x)
        series2.attachAxis(axis_y)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        series.setName("Parabel")
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)
        series.append(4, 16)
        series.append(5, 25)

        series2.setName("Gerade")
        series2.append(0, -5)
        series2.append(1, -2.5)
        series2.append(2, 0)
        series2.append(3, 2.5)
        series2.append(4, 5)
        series2.append(5, 7.5)

        self.setChart(chart)

def main():
    app = QApplication(sys.argv)

    # Text für Labels und anfängliche Temperaturen
    raum = 'Wohnzimmer'
    soll_temp = 22  # als Zahl, nicht als String
    ist_temp = 23  # als Zahl, nicht als String

    widget = SteuerElement(raum, soll_temp, ist_temp)
    widget.show()
    sys.exit(app.exec())

