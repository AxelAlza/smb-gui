import sys
from PyQt6 import QtWidgets
import os
from elevate import elevate
from vistas.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    elevate()
    os.system('xhost +si:localuser:root')
    os.environ['DISPLAY'] = ":0"
    os.environ['XAUTHORITY'] = '~/.Xauthority'
    app = QtWidgets.QApplication(sys.argv)
    v = VentanaPrincipal()
    v.show()
    sys.exit(app.exec())
