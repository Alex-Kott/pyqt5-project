import sys
import pickle
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Vehicle_Store:

	vehicles = dict()

	def __init__(self):
		super().__init__()

	def addVehicle(self):
		print("lol")



class Interface_Instance(QWidget):
	def __init__(self):
		super().__init__()
		self.main_window()

	def main_window(self):
		self.newVehicleBtn = QPushButton("New vehicle", self)
		self.newVehicleBtn.move(30, 50)

		self.exitBtn = QPushButton("Exit", self)
		self.exitBtn.move(150, 50)

		self.newVehicleBtn.clicked.connect(self.add_vehicle)
		self.exitBtn.clicked.connect(QCoreApplication.instance().quit)

		self.grid = QGridLayout()
		self.grid.setSpacing(1)
		self.clearLayout(self.grid)

		self.grid.addWidget(self.newVehicleBtn, 1, 0)
		self.grid.addWidget(self.exitBtn, 0, 1)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Review')
		self.show()


	def add_vehicle(self):
		self.brand = QLabel("Марка")
		self.model = QLabel("Модель")
		self.color = QLabel("Цвет")

		self.brandEdit = QLineEdit()
		self.modelEdit = QLineEdit()
		self.colorEdit = QLineEdit()

		self.clearLayout(self.grid)

		self.grid.addWidget(self.brand, 1, 0)
		self.grid.addWidget(self.brandEdit, 1, 1)

		self.grid.addWidget(self.model, 2, 0)
		self.grid.addWidget(self.modelEdit, 2, 1)

		self.grid.addWidget(self.color, 3, 0)
		self.grid.addWidget(self.colorEdit, 3, 1)

		self.saveItemBtn = QPushButton("Сохранить", self)
		self.grid.addWidget(self.saveItemBtn, 4, 3)

		self.setLayout(self.grid)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Добавить автомобиль')
		self.show()

	def clearLayout(self, layout):
		while layout.count():
			child = layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Interface_Instance()
    sys.exit(app.exec_())
