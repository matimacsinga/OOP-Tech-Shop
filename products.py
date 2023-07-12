from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import product

class Encoder(JSONEncoder):
    ''' from a Python object we need to obtain a json representation'''

    def default(self, o: object) -> dict:
        return o.__dict__

class Products:

    products = []

    @classmethod
    def load_products(cls) -> list:
        ''' reads the products.txt file and re-compose the Python objects
            from the json representation of products. The content of the
            products.txt file should look something like:

            '{\'name\': \'Amplifiers\'}'
            '{\'name\': \'Receivers\'}'

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the products
            list. We have avoided this by overloading the __eq__() operator in
            Product class. More on this during the lectures.
        '''
        decoder = product.Decoder()

        try:
            with open('products.txt') as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def remove_product(cls, cat: product.Product) -> None:
        ''' Removes a product from the products collection. We pass the product
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'products'. Then, in a second step
            we iterate that collection and we serialize element by element
        '''
        cls.load_products()
        if cat in cls.products:
            cls.products.remove(cat)
            with open('products.txt', 'w') as f:
                for cat in cls.products:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write('\n')
            print('Product succesfully removed')
        else:
            print('Product not in products list')

    @classmethod
    def add_product(cls, cat: product.Product) -> None:
        ''' Adds a new product in the products collection. We need to save the
            new product on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        '''
        cls.load_products()
        if cat not in cls.products:
            with open('products.txt', 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write('\n')
            print('Product succesfully added')
        else:
            print('Product already exists')