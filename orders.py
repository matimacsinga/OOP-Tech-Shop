from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import order

class Encoder(JSONEncoder):
    ''' from a Python object we need to obtain a json representation'''

    def default(self, o: object) -> dict:
        return o.__dict__

class Orders:

    orders = []

    @classmethod
    def load_orders(cls) -> list:
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
        decoder = order.Decoder()

        try:
            with open('orders.txt') as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.decode(data)
                    if decoded_order not in cls.orders:
                        cls.orders.append(decoded_order)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.orders = []
        return cls.orders

    @classmethod
    def remove_order(cls, cat: order.Order) -> None:
        ''' Removes a product from the products collection. We pass the product
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'products'. Then, in a second step
            we iterate that collection and we serialize element by element
        '''
        cls.load_orders()
        if cat in cls.orders:
            cls.orders.remove(cat)
            with open('orders.txt', 'w') as f:
                for cat in cls.orders:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write('\n')
            print('Order succesfully removed')
        else:
            print('Order not in orders list')

    @classmethod
    def add_order(cls, cat: order.Order) -> None:
        ''' Adds a new product in the products collection. We need to save the
            new product on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        '''
        cls.load_orders()
        if cat not in cls.orders:
            with open('orders.txt', 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write('\n')
            print('Order succesfully added')
        else:
            print('Order already exists')