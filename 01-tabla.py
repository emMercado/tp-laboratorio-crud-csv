from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
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
        self.tabla.removeRow(self.tabla.currentRow())


    def on_save(self):
        archivo = open('datos.csv', 'w', newline='')
        save = csv.writer(archivo, delimiter=',', quotechar='"')

        numRow = self.tabla.rowCount()

        for i in range(numRow):
            allDataTable = [self.tabla.item(i,0).text(), self.tabla.item(i,1).text(), self.tabla.item(i,2).text()]
            save.writerow(allDataTable)

        archivo.close()


    def on_load(self):
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


    def on_agregar(self):
        fila = self.filas
        self.tabla.insertRow(fila)

        nombre = self.nombre.text()
        self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))

        apellido = self.apellido.text()
        self.tabla.setItem(fila, 1, QTableWidgetItem(apellido))

        email = self.email.text()
        self.tabla.setItem(fila, 2, QTableWidgetItem(email))

        self.filas = self.filas + 1



app = QApplication([])

win = MiVentana()
win.show()

app.exec_()

