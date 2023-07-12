from json import JSONEncoder, JSONDecoder, loads
from unicodedata import category
from categories import Categories
from category import Category

class Product:
    def __init__(self):
        pass

    def __init__(self, name: str, price: int, brand: str, category: Category) -> object:
        self.name = name
        self.price = price
        self.brand = brand
        categories = Categories.load_categories()
        # i assumed that when you add a product with a category that does not exist, the category will be added as well
        if category in categories:
            self.category = category
        else:
            Categories.add_category(category)
            self.category = category
    
    def __eq__(self, other: object) -> bool:
        ''' Overloaded in order to verify the membership inside a collection '''
        if type(other) == type(self):
            # i assumed that there could be two products with the same name but different categories
            return self.name == other.name and self.category == other.category
        else:
            return False

    def __hash__(self):
        return hash(self.name)

    def __str__(self) -> str:
        return f'{self.name} {self.category.name} from {self.brand} cost/costs + {self.price}'

# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> dict:
        return o.__dict__

    # define the Product class, which is the base class for all the  products in the store
class Decoder(JSONDecoder):
    ''' We have to transform the serialized string into Python objects'''

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            # category is handled below since it's a more complex object
            if key == 'category':
                break
            vals.append(data[key])
        product = Product(*vals, Category(data['category']['name']))
        return product
