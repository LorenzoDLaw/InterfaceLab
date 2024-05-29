from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:/Users/LorenzoScanu/Documents/helpHour/mainwindow.ui", self)
 
        # find the widgets in the xml file
        self.table = self.findChild(QTableWidget, "tabella") 
        self.button = self.findChild(QPushButton, "bAggiungiAlunno")
        self.button.clicked.connect(self.clickedBtn)
        
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels(["Nome", "Cognome","Classe"])
        
        self.show()
 
    def clickedBtn(self):
       lista = [  {"nome": "Mario", "cognome": "Rossi", "classe": "3A"},
                {"nome": "Anna", "cognome": "Verdi", "classe": "4B"},
                {"nome": "Luca", "cognome": "Bianchi", "classe": "2C"},
                {"nome": "Elena", "cognome": "Neri", "classe": "5D"},
                {"nome": "Giovanni", "cognome": "Gialli", "classe": "1E"} ]
       
       loc=0
       for x in lista:
           item_name = QTableWidgetItem(lista[loc]["nome"])
           item_cognome = QTableWidgetItem(lista[loc]["cognome"])
           item_classe = QTableWidgetItem(lista[loc]["classe"])
           self.table.setItem(loc, 0, item_name)
           self.table.setItem(loc, 1, item_cognome)
           self.table.setItem(loc, 2, item_classe)
           loc+=1
           
app = QApplication(sys.argv)
window = UI()
app.exec_()