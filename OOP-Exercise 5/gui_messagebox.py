import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQt Button"
        self.x = 200  # or left
        self.y = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))  # Make sure the icon file exists or comment out if not

        # In GUI Python, these buttons, textboxes, labels are called widgets
        self.button = QPushButton('Click Me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 70)  # button.move(x,y)
        self.button.clicked.connect(self.clickMe)  # Connect to the correct method

        self.show()

    @pyqtSlot()
    def clickMe(self):
        buttonReply = QMessageBox.question(self,"Testing Response", "Do you like PyQt5?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            QMessageBox.warning(self, "Evaluation", "User clicked Yes", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Evaluation", "User clicked No", QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
