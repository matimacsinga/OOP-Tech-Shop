from category import Category
from product import Product

class Microphone(Product):
	def __init__(self,name,price,brand,color,power,bluetooth) -> object:
		super().__init__(name,price,brand,Category('Microphone'))
		self.color = color
		self.power = power
		self.bluetooth = bluetooth
		