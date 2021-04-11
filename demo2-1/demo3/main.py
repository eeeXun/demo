from UI import Ui_Frame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QBrush, QFont
from PyQt5.QtCore import Qt, QRectF, QPoint, QRect
import sys

class Win(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clickfoo)
        self.myShops = []
        self.allPath = []
        self.visited = []
        self.myPath = []

    def clickfoo(self):
        self.dataInit()
        self.prime()

    def dataInit(self):
        self.myShops = list(self.lineEdit.text())
        self.allPath = [[i[1], i[3], int(i[5])] for i in self.lineEdit_2.text().split()]
        self.myPath = []

    def prime(self):
        self.visited = ["A"]
        while len(self.visited) < len(self.myShops):
            searchingPaths = []
            minPath = ["", "", sys.maxsize]
            for path in self.allPath:
                if self.XORvisited(path[0], path[1]):
                    searchingPaths.append(path)
            for path in searchingPaths:
                if path[2] < minPath[2]:
                    minPath = path
            self.myPath.append(minPath)
            if minPath[0] in self.visited:
                self.visited.append(minPath[1])
            else:
                self.visited.append(minPath[0])

    def XORvisited(self, a, b):
        if (a in self.visited and b not in self.visited) or \
                (a not in self.visited and b in self.visited):
            return True
        else:
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Win()
    window.show()
    sys.exit(app.exec_())
