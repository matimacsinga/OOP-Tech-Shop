from category import Category
from product import Product


class Speaker(Product):
    def __init__(self, name: str, price: int, brand: str, impedance: int, power: int) -> object:
        #i know that it's a bit redundant to have a category linked to the product and also have child classes signifying the Categories, but i made it like this just to be a bit more complex
        super().__init__(name, price, brand, Category('Speaker'))
        self.impedance = impedance
        self.power = power