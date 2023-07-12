from unicodedata import category
from category import Category
from categories import Categories
from order import Order
from orders import Orders
from product import Product
from products import Products
from speaker import Speaker
from mouse import Mouse
from keyboard import Keyboard
from json import JSONDecodeError

def add_category():
    #kind of had in mind making a cool feature that if you add a category it would create a python file with the class and attributes in it, just as an extra
    category_name = input('What category would you like to add?\n')
    category = Category(category_name)
    file_name = category_name.lower()
    Categories.add_category(category)
    new_class_string = 'from category import Category\nfrom product import Product\n\nclass '+category_name+'(Product):\n'
    default_attributes = ['name','price','brand']
    new_attributes = input('What new attributes should the category have? (separate them by comma and no spaces)\n').split(',')
    attributes = default_attributes+new_attributes
    new_class_string += '\tdef __init__(self'
    for att in attributes:
        new_class_string = new_class_string+','+att
    new_class_string = new_class_string + ') -> object:\n\t\tsuper().__init__(name,price,brand,Category(\''+category_name+'\'))\n\t\t'
    for att in new_attributes:
        new_class_string = new_class_string+'self.'+att+' = '+att+'\n\t\t'
    with open(file_name+'.py', 'w') as f:
        f.write(new_class_string)
        f.close()



def remove_category():
    category_name = input('What category would you like to remove?\n')
    category = Category(category_name)
    Categories.remove_category(category)


def list_categories():
    categories = Categories.load_categories()
    if categories:
        for cat in categories:  
            print(cat.name)
    else: 
        print('There are no categories yet\n')

def add_order():
    name, category, quantity, address = input('Type the product name, product category, quantity and your address to place an order\n').split(',')
    products = Products.load_products()
    possible_product = Product(name, 0, '', Category(category))
    # checking if product actually exists, price and brand are null since you can compare product without them
    for product in products:
        if product == possible_product:
            order = Order(Product(product.name, product.price, product.brand, product.category), int(quantity), address)
            Orders.add_order(order)
            return
    print('Product that you want to order doesn\'t exist')


def remove_order():
    name, category, quantity, address = input('Type the product name, product category, quantity and your address to remove an order\n').split(',')
    order = Order(Product(name, 0, '', Category(category)), int(quantity), address)
    Orders.remove_order(order)


def list_orders():
    orders = Orders.load_orders()

    if orders:
        for ord in orders:  
            print(ord)
    else: 
        print('There are no orders yet\n')

def add_product():
    type = int(input('Add a product of the three initial categories, one of the categories added by you or add a product of a new category?\n1.Existing\n2.New\n'))
    match type:
        case 1:
            choice = int(input('What type of product do you want to add?\n1.Speaker\n2.Mouse\n3.Keyboard\n'))
            match choice:
                case 1:
                    name, price, brand, impedance, power = input('Type the name, price, brand, impedance, and power of the speakers separated by commas and without spaces\n').split(',')
                    product = Speaker(name, int(price), brand, int(impedance), int(power))  
                case 2:
                    name, price, brand, dpi, extra_buttons = input('Type the name, price, brand, dpi of the mouse and if it has extra buttons (True or False), separated by commas and without spaces\n').split(',')
                    product = Mouse(name, int(price), brand, int(dpi), True) if extra_buttons == 'True' else Mouse(name, int(price), brand, int(dpi), False)
                case 3:
                    name, price, brand, weight, has_numpad = input('Type the name, price, brand, weight of the keyboard and if it has a numpad, separated by commas and without spaces\n').split(',')
                    product = Keyboard(name, int(price), brand, int(weight), True) if has_numpad == 'True' else Keyboard(name, int(price), brand, int(weight), False)
        case 2:
            name, price, brand, category = input('Type the name, price, brand, and category of the product separated by commas and without spaces\n').split(',')
            product = Product(name, int(price), brand, Category(category))
    Products.add_product(product)

def remove_product():
    name, category = input('What\'s the name and category (split them by comma)?\n').split(',')
    categories = Categories.load_categories()
    # can quickly check if the product exists or not by checkin if the category exists or not
    if Category(category) not in categories:
        print('Product not in products list')
    else:
        # price doesn't matter since it doesn't matter for the equality of two products
        product = Product(name, 0, '', Category(category))
        Products.remove_product(product)


def list_products():
    products = Products.load_products()
    if products:
        for product in products:  
            print(product)
    else: 
        print('There are no products yet\n')

def list_products_from_category():
    category_name = input("From what category should the products be?\n")

    products = Products.load_products()
    if products:
        for product in products:
            if product.category.name == category_name:
                print(product)


def error_action():
    print('Please select a valid option')


if __name__ == '__main__':
    while True:
        try:
            chosen_field = int(input('\nChoose a field:\n1.Categories\n2.Products\n3.Orders\n4.Exit\n'))
            match chosen_field:
                case 1:
                    category_functions = {1: add_category, 2: remove_category, 3: list_categories}
                    choice = int(input('Choose an action:\n1.Add a category\n2.Remove a category\n3.Display existing categories\n'))
                    chosen_function = category_functions.get(choice, error_action)
                    chosen_function()
                case 2:
                    product_functions = {1: add_product, 2: remove_product, 3: list_products, 4: list_products_from_category}
                    choice = int(input('Choose an action:\n1.Add a product\n2.Remove a product\n3.Display existing products\n4.Display products from a category\n'))
                    chosen_function = product_functions.get(choice, error_action)
                    chosen_function()
                case 3:
                    order_functions = {1: add_order, 2: remove_order, 3: list_orders}
                    choice = int(input('Choose an action:\n1.Add an order\n2.Remove an order\n3.Display existing orders\n'))
                    chosen_function = order_functions.get(choice, error_action)
                    chosen_function()
                case 4:
                    print('Goodbye!')
                    break
                case _:
                    print('Please select a valid option')

        except ValueError as e:
            print('Please input an integer that is a valid option')
            
