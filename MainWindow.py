from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = "Calculator"
		self.top = 100
		self.left=100
		self.width = 400
		self.height = 260
		self.label=""


		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		self.CreateButton(1,5,5)
		self.CreateButton(2,35,5)
		self.CreateButton(3,70,5)
		self.CreateButton(4,5,40)
		self.CreateButton(5,35,40)
		self.CreateButton(6,70,40)
		self.CreateButton(7,5,75)
		self.CreateButton(8,35,75)
		self.CreateButton(9,70,75)
		self.CreateButton(0,35,110)
		self.CreateButton('.',70,110)
		self.CreateButton('+',110,5)
		self.CreateButton('-',110,40)
		self.CreateButton('*',110,75)
		self.CreateButton('/',110,110)
		self.CreateButton('^',110,145)
		self.CreateEqual(110,180)
		self.CreateClear(110,215)
		self.labelWidget = QLabel(self)
		self.labelWidget.setGeometry(180,5,300,35)
		self.show()

	def CreateButton(self,which,x,y):
		button = QPushButton(str(which),self)
		button.setGeometry(QRect(x,y,40,40))
		button.clicked.connect(lambda: self.on_button(which))


	def CreateEqual(self,x,y):
		button = QPushButton('=',self)
		button.setGeometry(QRect(x,y,40,40))
		button.clicked.connect(self.equal)

	def CreateClear(self,x,y):
		button = QPushButton('C',self)
		button.setGeometry(QRect(x,y,40,40))
		button.clicked.connect(self.clear)

	def clear(self):
		self.label = ""
		self.labelWidget.setText(self.label)

	def equal(self):
		self.label = str(self.calc(self.label))
		self.labelWidget.setText(self.label)



	def on_button(self,i):
		self.label = self.label + str(i)
		self.labelWidget.setText(self.label)

	def calc(self,string):
		if '^' in string:
			args = string.split('^',2)
			return self.calc(args[0])**self.calc(args[1])
		if '+' in string:
			args = string.split('+',2)
			return self.calc(args[0]) + self.calc(args[1])
		if '-' in string:
			args = string.split('-',2)
			return self.calc(args[0]) - self.calc(args[1])
		if '*' in string:
			args = string.split('*',2)
			return self.calc(args[0]) * self.calc(args[1])
		if '/' in string:
			args = string.split('/',2)
			if float(args[1]) == 0:
				return "Divide by 0"
			return (self.calc(args[0]) / self.calc(args[1]))

		r=float(string)
		return r

App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())