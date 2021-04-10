from UI import Ui_Frame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QBrush, QFont
from PyQt5.QtCore import Qt, QRectF, QPoint
import sys

Ingredients = {"S": "Salmon", "T": "Tuna", "I": "Istiophoridae", "F": "Fenneropenaeus",
               "B": "Borealis", "A": "Adductor", "H": "Haliotis", "G": "Gratilla",
               "K": "Kuroge", "C": "Chionoecetes", "E": "Eriocheir", "P": "Palinuridae"}

class SubWin(QWidget):
    def __init__(self, myItems, cost):
        super().__init__()
        self.setFixedSize(10000, 10000)
        self.myItems = myItems
        self.cost = cost
        self.N = len(myItems)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont("Monospace", 15))
        painter.setPen(Qt.white)

        tmp_count = 1
        item_width = 200
        item_height = 20
        for item in self.myItems:
            painter.drawText(QRectF(tmp_count * item_width, 0, item_width, item_height),
                             Ingredients[item])
            painter.drawText(QRectF(0, tmp_count * item_height, item_width, item_height),
                             Ingredients[item])
            tmp_count += 1
        for i in range(1, self.N + 1):
            for j in range(i, self.N + 1):
                painter.drawText(QRectF(j * item_width,
                                        i * item_height,
                                        item_width, item_height),
                                 str(self.cost[i][j][0]) + self.cost[i][j][1])

class Win(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clickfoo)
        # self.myItems = {}
        self.myItems = []
        self.myFreq = []
        self.N = 0
        self.cost = []

    def clickfoo(self):
        self.dataInit()
        self.optimalSearch()
        self.drawOutput()
        # for i in range(len(self.cost)):
        #     print(self.cost[i])

    def dataInit(self):
        # self.myItems = {}
        # key = list(self.lineEdit.text())
        # freq = [int(i) for i in self.lineEdit_2.text().split(",")]
        # for i in range(len(key)):
        #     self.myItems[key[i]] = freq[i]
        # # self.cost = [[[]] * (len(key) + 1)] * (len(key) + 1)
        # self.cost = [[[]] * len(key)] * len(key)
        self.myItems = list(self.lineEdit.text())
        self.myFreq = [int(i) for i in self.lineEdit_2.text().split(",")]
        self.N = len(self.myItems)
        # self.cost = [[[]] * (self.N + 2)] * (self.N + 2)
        # self.cost = []
        # for i in range(self.N + 2):
        #     self.cost.append([])
        # for i in range(self.N + 2):
        #     self.cost[i] = [0] * (self.N + 2)
        self.cost = [[[sys.maxsize, ""] for x in range(self.N + 2)] for y in range(self.N + 2)]

    def optimalSearch(self):
        for i in range(1, self.N + 1):
            self.cost[i][i] = [self.myFreq[i - 1], self.myItems[i - 1]]
        for i in range(1, self.N + 2):
            self.cost[i][i -1] = [0, ""]
        for j in range(1, self.N):
            for i in range(1, self.N - j + 1):
                for k in range(1, i + j + 1):
                    tmp = self.cost[i][k - 1][0] + self.cost[k + 1][i + j][0]
                    if tmp < self.cost[i][i + j][0]:
                        self.cost[i][i + j] = [tmp, self.myItems[k - 1]]
                tmp = 0
                for k in range(i, i + j + 1):
                    tmp += self.myFreq[k - 1]
                self.cost[i][i + j][0] += tmp

    def drawOutput(self):
        subWin = SubWin(self.myItems, self.cost)
        self.scrollArea.setWidget(subWin)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Win()
    window.show()
    sys.exit(app.exec_())
