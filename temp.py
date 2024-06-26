from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    
    
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:/Users/LorenzoScanu/Documents/helpHour/mainwindow.ui", self)
 
        # find the widgets in the xml file
        self.table = self.findChild(QTableWidget, "tabella") 
        self.button = self.findChild(QPushButton, "bAggiungiAlunno")
        self.buttonAggiorna = self.findChild(QPushButton, "bAggiorna")
        self.bModifica = self.findChild(QPushButton, "bModifica")
        self.tNome = self.findChild(QLineEdit, "lineEditNome")
        self.tCognome = self.findChild(QLineEdit, "lineEditCognome")
        self.tClasse = self.findChild(QLineEdit, "lineEditClasse")
        self.lNome = self.findChild(QLabel, "lNome_2")
        self.lCognome = self.findChild(QLabel, "lCognome_2")
        self.lClasse = self.findChild(QLabel, "lClasse_2")
        
        self.button.clicked.connect(self.clickedBtn)
        self.buttonAggiorna.clicked.connect(self.btnAggiorna)
        self.bModifica.clicked.connect(self.ModificaDati)
        
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(["Nome", "Cognome","Classe"])
        
        self.show()
     
    def clickedBtn(self): 
        
        self.lista = [  {"nome": "Mario", "cognome": "Rossi", "classe": "3A"},
                 {"nome": "Anna", "cognome": "Verdi", "classe": "4B"},
                 {"nome": "Luca", "cognome": "Bianchi", "classe": "2C"},
                 {"nome": "Elena", "cognome": "Neri", "classe": "5D"},
                 {"nome": "Giovanni", "cognome": "Gialli", "classe": "1E"} ]
       
        row = len(self.lista)
        self.table.setRowCount(row)
        
        loc=0
        for x in self.lista:
           item_name = QTableWidgetItem(x["nome"])
           item_cognome = QTableWidgetItem(x["cognome"])
           item_classe = QTableWidgetItem(x["classe"])
           self.table.setItem(loc, 0, item_name)
           self.table.setItem(loc, 1, item_cognome)
           self.table.setItem(loc, 2, item_classe)
           loc+=1
    
    def ModificaDati(self):
        indice = self.table.currentRow()
        item_name = QTableWidgetItem(self.lista[indice]["nome"])
        item_cognome = QTableWidgetItem(self.lista[indice]["cognome"])
        item_classe = QTableWidgetItem(self.lista[indice]["classe"])
        
        self.lNome.setText(item_name.text())
        self.lCognome.setText(item_cognome.text())
        self.lClasse.setText(item_classe.text())
    
    def btnAggiorna(self):
        indice = self.table.currentRow()
        name = self.tNome
        cognome = self.tCognome
        classe = self.tClasse
        
        print(name.text())
        print(cognome.text())
        print(classe.text())
        
        self.lista[indice]["nome"] = name.text()
        self.lista[indice]["cognome"] = cognome.text()
        self.lista[indice]["classe"] = classe.text()
        
        self.table.setItem(indice, 0, QTableWidgetItem(name.text()))
        self.table.setItem(indice, 1, QTableWidgetItem(cognome.text()))
        self.table.setItem(indice, 2, QTableWidgetItem(classe.text()))
        
        print(self.lista)
        
app = QApplication(sys.argv)
window = UI()
app.exec_()