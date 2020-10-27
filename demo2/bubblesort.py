from module import Ui_Frame
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.QtCore import Qt,QRectF
import sys

class Win(QMainWindow,Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sort)
        # self.bub=[]
        self.circles_list=[]
        self.circles_point=[]
        self.txt=[]

    def sort(self):
        self.bub=[]
        self.getTextList()
        self.circles_list=[]
        self.getBubList()
        self.bubble_sort()
        self.circles_point=[]
        self.setPoint()

    def getTextList(self):
        tmp=self.lineEdit.text().split(',')
        for i in tmp:
            self.bub.append(int(i))

    def getBubList(self):
        self.circles_list.append([])
        for i in self.bub:
            self.circles_list[len(self.circles_list)-1].append(i)

    def bubble_sort(self):
        for i in range(len(self.bub)-1,-1,-1):
            for j in range(i):
                if self.bub[j]<self.bub[j+1]:
                    self.bub[j],self.bub[j+1]=self.bub[j+1],self.bub[j]
                    self.getBubList()

    def setPoint(self):
        for i in range(len(self.circles_list)):
            for j in range(len(self.circles_list[i])):
                self.circles_point.append(QRectF(500+80*j,20+80*i,self.circles_list[i][j]*8,self.circles_list[i][j]*8))
        self.update()

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setBrush(Qt.cyan)
        for i in self.circles_point:
            painter.drawEllipse(i)

        painter.setPen(Qt.black)
        painter.setFont(QFont('txt',15))
        for i in range(len(self.circles_list)):
            for j in range(len(self.circles_list[i])):
                painter.drawText(QRectF(500+80*j,20+80*i,100,100),Qt.AlignCenter,str(self.circles_list[i][j]))

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Win()
    window.show()
    sys.exit(app.exec_())
