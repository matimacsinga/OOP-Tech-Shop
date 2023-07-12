from category import Category
from product import Product


class Mouse(Product):
    def __init__(self, name: str, price: int, brand: str, dpi: int, extra_buttons: bool) -> object:
        #i know that it's a bit redundant to have a category linked to the product and also have child classes signifying the Categories, but i made it like this just to be a bit more complex
        super().__init__(name, price, brand, Category('Mouse'))
        self.dpi = dpi
        self.extra_buttons = extra_buttons