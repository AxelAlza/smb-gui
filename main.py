import sys
from PyQt6 import QtWidgets
import os
from elevate import elevate
from vistas.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    elevate()

    os.environ['XAUTHORITY'] = '~/.Xauthority'
    os.environ['DISPLAY'] = ":0.0"
    app = QtWidgets.QApplication(sys.argv)
    v = VentanaPrincipal()
    v.show()
    sys.exit(app.exec())
