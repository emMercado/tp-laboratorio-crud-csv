from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QInputDialog
from PyQt5 import uic
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01-tabla.ui", self)

        # Crear las columnas
        self.tabla.setColumnCount(3)

        # Nombrar las columnas
        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail'))

        self.filas = 0

        self.agregar.clicked.connect(self.on_agregar)
        self.cargar.clicked.connect(self.on_load)
        self.guardar.clicked.connect(self.on_save)
        self.eliminar.clicked.connect(self.on_delete)

    def on_delete(self):
        msg = QMessageBox()
        msg.setWindowTitle('Eliminar')
        msg.setText('Esta seguro de querer eliminar el registro? ')
        index = self.tabla.currentRow()
        item = [self.tabla.item(index,0).text(),self.tabla.item(index,1).text(), self.tabla.item(index,2).text()]
        msg.setInformativeText(str(item))
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes:
            row = self.tabla.currentRow()
            self.tabla.removeRow(row)
        elif resultado == QMessageBox.No:
            self.tabla.currentIndex()

    def on_save(self):
        msg = QMessageBox()
        msg.setWindowTitle('Guardar')
        msg.setText('Data saved successfully')
        archivo = open('datos-guardados.csv', 'w', newline='')
        save = csv.writer(archivo, delimiter=',', quotechar='"')

        numRow = self.tabla.rowCount()

        for i in range(numRow):
            allDataTable = [self.tabla.item(i,0).text(), self.tabla.item(i,1).text(), self.tabla.item(i,2).text()]
            save.writerow(allDataTable)

        archivo.close()
        msg.exec()

    def on_load(self):
        msg = QMessageBox()
        msg.setWindowTitle('Cargar')
        msg.setText('Data load successfully')
        fila = self.filas
        #self.tabla.insertRow(fila)
        self.filas = self.filas

        archivo = open('datos.csv')
        all_data = csv.reader(archivo, delimiter=',', quotechar='"')

        for i in all_data:
            fila = self.filas
            self.tabla.insertRow(fila)

            self.tabla.setItem(fila, 0, QTableWidgetItem('{0}'.format(i[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem('{0}'.format(i[1])))
            self.tabla.setItem(fila, 2, QTableWidgetItem('{0}'.format(i[2])))

        archivo.close()
        msg.exec()
        self.cargar.setEnabled(False)

    def on_agregar(self):
        msg = QMessageBox()
        msg.setWindowTitle('Add new data')
        msg.setText('The data was added successfully, remember to press the save button to add the changes')
        fila = self.filas
        self.tabla.insertRow(fila)

        nombre = self.nombre.text()
        self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))

        apellido = self.apellido.text()
        self.tabla.setItem(fila, 1, QTableWidgetItem(apellido))

        email = self.email.text()
        self.tabla.setItem(fila, 2, QTableWidgetItem(email))

        self.filas = self.filas + 1
        msg.exec()


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()

