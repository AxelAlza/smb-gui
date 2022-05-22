from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from parser import Parser
from ui.main import Ui_MainWindow
from vistas.VentanaAnadir import VentanaAnadir


class VentanaPrincipal(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaPrincipal, self).__init__(*args, **kwargs)
        self.VentanaAnadir = VentanaAnadir()
        self.VentanaAnadir.on_confirm.connect(self.updateTabla)
        self.setupUi(self)
        self.popularTabla()

    @pyqtSlot()
    def on_BtnAnadir_clicked(self):
        self.VentanaAnadir.show()

    @pyqtSlot()
    def on_BtnEliminar_clicked(self):
        i = self.tableView.selectedIndexes()
        if not i:
            QMessageBox.warning(self, "Seleccione un recurso", "Debe seleccionar un recurso")
        else:
            nombreshare = self.tableView.model().data(i[0])
            print(nombreshare)
            self.tableView.model().removeRow(i[0].row())
            parser = Parser()
            parser.EliminarShare(nombreshare)

    @pyqtSlot()
    def updateTabla(self):
        path = self.VentanaAnadir.EdtPath.text()
        nombre = self.VentanaAnadir.EdtName.text()
        i = self.tableView.model().rowCount()
        self.tableView.model().insertRow(i)
        i0 = self.tableView.model().index(i, 0)
        i1 = self.tableView.model().index(i, 1)
        self.tableView.model().setData(i0, nombre)
        self.tableView.model().setData(i1, path)

    def popularTabla(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Nombre', 'Path'])
        model.setColumnCount(2);
        parser = Parser()
        shareslist = parser.GetShares()
        for share in shareslist:
            name = QStandardItem(share)
            name.setEditable(False)
            path = QStandardItem(shareslist[share])
            path.setEditable(False)
            model.appendRow([name, path])
        self.tableView.setModel(model)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    v = VentanaPrincipal()
    v.show()
    sys.exit(app.exec())
