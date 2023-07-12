from product import Product
from product import Decoder as ProductDecoder
from json import JSONEncoder, JSONDecoder, loads
from category import Category

class Order:
    def __init__(self, product: Product, quantity: int, address: str) -> object:
        self.product = product
        self.quantity = quantity
        self.address = address

    def __eq__(self, other: object):
        # i assumed two orders are equal when the product, quantity, and address are equal
        if type(other) == type(self):
            return self.address == other.address and self.product == other.product and self.quantity == other.quantity
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f'{self.quantity} of {self.product.brand} {self.product.name} {self.product.category.name} at address {self.address}'

class Encoder(JSONEncoder):
    def default(self, o: object) -> dict:
        return o.__dict__

class Decoder(JSONDecoder):
    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            # product is handled below since it's a more complex object
            if key == 'product':
                continue
            vals.append(data[key])
        product_data = data['product']
        product = Product(product_data['name'], product_data['price'], product_data['brand'], Category(product_data['category']['name']))
        order = Order(product, *vals)
        return order