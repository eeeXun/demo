from b2 import Ui_Frame
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.QtCore import Qt,QRectF,QPoint
from red_black import RBNode,RBBinaryTree
import sys

rootx=1000
rooty=100
Rx=300
Ry=100
Radix=20

class draw_circle(QWidget):
    def __init__(self,circles_point,font_point,line_point):
        super().__init__()
        self.setFixedSize(10000,10000)
        self.circles_point=circles_point
        self.font_point=font_point
        self.line_point=line_point
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setPen(Qt.black)
        for i in self.line_point:
            painter.drawLine(i[0],i[1],i[2],i[3])

        for i in self.circles_point:
            if i[1]=='red':
                painter.setBrush(Qt.red)
            else:
                painter.setBrush(Qt.black)

            painter.drawEllipse(i[0][0],i[0][1],i[0][2])

        painter.setPen(Qt.white)
        painter.setFont(QFont('txt',15))
        for i in self.font_point:
            painter.drawText(i[0],Qt.AlignCenter,i[1])

class Win(QMainWindow,Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sort)

    def sort(self):
        nums=self.getTextList()
        self.myTree=RBBinaryTree()
        for num in nums:
            self.myTree.rb_insert(int(num))

        self.circles_point=[]
        self.font_point=[]
        self.line_point=[]
        self.setPoint(self.myTree.root,rootx,rooty,Rx,Ry)
        self.setFont(self.myTree.root,rootx,rooty,Rx,Ry)
        self.setLine(self.myTree.root,rootx,rooty,Rx,Ry)
        self.draw()

    def getTextList(self):
        nums=self.lineEdit.text().split(',')
        return nums

    def setPoint(self,root,x,y,rx,ry):
        if root:
            self.setPoint(root.left_child,x-rx,y+ry,rx/1.5,ry/1.5)
            self.circles_point.append([[QPoint(x,y),Radix,Radix],root.color])
            self.setPoint(root.right_child,x+rx,y+ry,rx/1.5,ry/1.5)

    def setFont(self,root,x,y,rx,ry):
        if root:
            self.setFont(root.left_child,x-rx,y+ry,rx/1.5,ry/1.5)
            self.font_point.append([QRectF(x-Radix,y-Radix,2*Radix,2*Radix),str(root.data)])
            self.setFont(root.right_child,x+rx,y+ry,rx/1.5,ry/1.5)

    def setLine(self,root,x,y,rx,ry):
        if root:
            if root.left_child:
                self.line_point.append([x,y,x-rx,y+ry])
            if root.right_child:
                self.line_point.append([x,y,x+rx,y+ry])
            self.setLine(root.left_child,x-rx,y+ry,rx/1.5,ry/1.5)
            self.setLine(root.right_child,x+rx,y+ry,rx/1.5,ry/1.5)

    def draw(self):
        cir=draw_circle(self.circles_point,self.font_point,self.line_point)
        self.scrollArea.setWidget(cir)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Win()
    window.show()
    sys.exit(app.exec_())
