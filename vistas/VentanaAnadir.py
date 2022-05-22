import os

from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from parser import Parser
from ui.añadir import Ui_Form
from PyQt6.QtCore import pyqtSignal


class VentanaAnadir(QWidget, Ui_Form):
    on_confirm = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(VentanaAnadir, self).__init__(*args, **kwargs)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setupUi(self)

    @pyqtSlot()
    def on_BtnCancelar_clicked(self):
        self.close()

    @pyqtSlot()
    def on_BtnExplorar_clicked(self):
        explorer = QFileDialog(self)
        explorer.setFileMode(QFileDialog.FileMode.Directory)
        path = explorer.getExistingDirectory(self, "Seleccionar directorio")
        if path:
            self.EdtPath.setText(path)
            self.EdtName.setText(os.path.basename(os.path.normpath(path)))

    @pyqtSlot()
    def on_BtnConfirmar_clicked(self):
        if self.Validar():
            parser = Parser()
            parser.ConfigShare(self.EdtName.text(), self.EdtPath.text(), self.chkWrite.isChecked(),
                               self.chkBrowseable.isChecked())
            self.on_confirm.emit()
            self.close()

    def Validar(self):
        if not (self.EdtName.text()) or not (self.EdtPath.text()):
            QMessageBox.critical(self, "Error", "Nombre de recurso y directorio no pueden estar vacios")
            return False
        if not os.path.exists(self.EdtPath.text()):
            QMessageBox.critical(self, "Error", "Ese directorio no existe")
            return False
        return True



