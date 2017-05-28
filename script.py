import sys
import pickle
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Vehicle_Store:

	data_file = "data.txt"
	pickle_file = "data.pickle"
	vehicles = []

	def __init__(self):
		with open(self.pickle_file, "rb") as pf:
			self.vehicles = pickle.load(pf)
		super().__init__()

	def add_vehicle(self, vehicle):
		vehicles = self.vehicles
		vehicles.append(vehicle)
		with open(self.pickle_file, "wb") as pf:
			pickle.dump(vehicles, pf)
		with open(self.data_file, "w") as df:
			df.write("Brand    Model    Color\n______________________\n")
			for i in vehicles:
				df.write("{0}    {1}    {2}\n".format(i['Brand'], i['Model'], i['Color']))
		df.close()

	def clean(self):
		self.vehicles.clear()
		with open(self.pickle_file, "wb") as pf:
			pickle.dump(self.vehicles, pf)


	def get_vehicles(self, criterion = None, value = None):
		response = []
		if criterion != None:
			for i in self.vehicles:
				if i[criterion] == value:
					response.append(i)
		else:
			response = self.vehicles
		return response

	def brand_filter(self, brand):
		response = []
		for i in self.vehicles:
			if i['Brand'] == brand:
				response.append(i)
		return response

	def model_filter(self, model):
		response = []
		for i in self.vehicles:
			if i['Model'] == model:
				response.append(i)
		return response

	def color_filter(self, color):
		response = []
		for i in self.vehicles:
			if i['Color'] == color:
				response.append(i)
		return response




class Interface_Instance(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.grid = QGridLayout()
		self.grid.setSpacing(1)
		self.main_window()

	def main_window(self):
		self.clearLayout(self.grid)
		self.newVehicleBtn = QPushButton("Добавить автомобиль", self)
		self.showAllBtn = QPushButton("Показать автомобили", self)
		self.removeAllBtn = QPushButton("Очистить список", self)
		self.exitBtn = QPushButton("Выход", self)

		store = Vehicle_Store()

		self.newVehicleBtn.clicked.connect(self.add_vehicle)
		self.showAllBtn.clicked.connect(lambda z: self.show_all(store.get_vehicles()))
		self.removeAllBtn.clicked.connect(self.remove_all)
		self.exitBtn.clicked.connect(QCoreApplication.instance().quit)

		self.grid.addWidget(self.newVehicleBtn, 1, 0)
		self.grid.addWidget(self.showAllBtn, 2, 0)
		self.grid.addWidget(self.removeAllBtn, 3, 0)
		self.grid.addWidget(self.exitBtn, 4, 0)
		self.setLayout(self.grid)

		self.setWindowTitle('Меню')
		self.setGeometry(300, 300, 350, 300)
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
		self.grid.addWidget(self.saveItemBtn, 4, 1)
		self.saveItemBtn.clicked.connect(self.save_vehicle)

		self.cancelBtn = QPushButton("Отмена", self)
		self.grid.addWidget(self.cancelBtn, 4, 2)
		self.cancelBtn.clicked.connect(self.main_window)

		self.setWindowTitle('Добавить автомобиль')
		self.setLayout(self.grid)

	def save_vehicle(self):
		brand = self.brandEdit.text()
		model = self.modelEdit.text()
		color = self.colorEdit.text()
		vehicle = dict()
		vehicle = {"Brand": brand, "Model": model, "Color":color}
		store = Vehicle_Store()
		store.add_vehicle(vehicle)
		self.main_window()

	def remove_all(self):
		store = Vehicle_Store()
		store.clean()

	def show_all(self, vehicles):
		store = Vehicle_Store()
		self.clearLayout(self.grid)

		self.listWidget = QListWidget()

		for i in vehicles:
			self.item = QListWidgetItem("{0} {1}, {2}".format(i['Brand'], i['Model'], i['Color']))
			self.listWidget.addItem(self.item)
		self.grid.addWidget(self.listWidget, 0, 1, 1, 3)

		brandFilterEdit = QLineEdit()
		brandFilterBtn = QPushButton("Показать только марки:", self)
		self.grid.addWidget(brandFilterBtn, 1, 1)
		self.grid.addWidget(brandFilterEdit, 2, 1)
		brandFilterBtn.clicked.connect(lambda x: self.show_all(store.get_vehicles("Brand", brandFilterEdit.text())))

		modelFilterEdit = QLineEdit()
		modelFilterBtn = QPushButton("Показать только модели:", self)
		self.grid.addWidget(modelFilterBtn, 1, 2)
		self.grid.addWidget(modelFilterEdit, 2, 2)
		modelFilterBtn.clicked.connect(lambda x: self.show_all(store.get_vehicles("Model", modelFilterEdit.text())))

		colorFilterEdit = QLineEdit()
		colorFilterBtn = QPushButton("Показать только цвета:", self)
		self.grid.addWidget(colorFilterBtn, 1, 3)
		self.grid.addWidget(colorFilterEdit, 2, 3)
		colorFilterBtn.clicked.connect(lambda x: self.show_all(store.get_vehicles("Color", colorFilterEdit.text())))

		self.cancelBtn = QPushButton("Отмена", self)
		self.grid.addWidget(self.cancelBtn, 4, 1, 1, 3)
		self.cancelBtn.clicked.connect(self.main_window)

		self.setWindowTitle('Показать автомобили')
		self.setGeometry(300, 300, 650, 300)
		self.setLayout(self.grid)
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