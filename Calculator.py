# Building basic Calculator

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Roshan Calculator')
        self.setGeometry(100,100,300,400)
        self.initGUI()
        
    def initGUI(self):
        self.layout= QVBoxLayout()
        self.display= QLineEdit()
        self.display. setReadOnly(True)
        self.layout. addWidget(self.display)

        self.buttons=QGridLayout()
        self.create_buttons()
        self.layout. addLayout(self.buttons)
        self.setLayout(self.layout)

    def create_buttons(self):

        Labels =[
        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ( '*', 1, 3),
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
        ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),]

        for label, row, col in Labels:
            button = QPushButton(label)
            if label in ['C', '=']:
                button. setStyleSheet("background-color: orange; color: black; font-size: 20px;")
            elif label in ['+', '-', '*', '/']:
                button.setStyleSheet("background-color: blue; color: black; font-size: 20px;")
            else:
                button.setStyleSheet("background-color: gray; color: black; font-size: 20px;")
            
            button.clicked.connect(self.button_clicked)
            self.buttons.addWidget(button, row, col)

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif text == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()