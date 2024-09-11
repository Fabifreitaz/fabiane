import sys

from PyQt6.QtWidgets import QApplication, QWidget,QLabel, QPushButton
class JanelaPrincipal(QWidget):
    def __init__(self):
        self.botao
        super().__init__()
        self.setWindowTitle("Hello word")
        self.setGeometry(200,200,300,400)
        
        
def main():
    
    app = QApplication(sys.argv)
    window =QWidget()
    
    window.show()
    sys.exit(app)
   
   
   
   
def main():
    
    def botaoClicado():
        label.setText("O botao foi apertado")
    app = QApplication(sys.argv)
    window =QWidget()
    window.setWindowTitle("Hello")
    window.setGeometry(200,200,400,300)
    label = QLabel(window)
    label.setText("Hello Word")
    label.move(150,100)
    
    botao = QPushButton("Apertar", window)
    botao.
    