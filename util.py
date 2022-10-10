import json


class Util:

    @staticmethod
    def add_new_product():
        fd = open("inventory.json", 'r')
        txt = fd.read()
        data = json.loads(txt)
        fd.close()
        print("Enter New Product ID :- ")
        productId = input()
        if productId not in data.keys():
            print("Enter Product Name :- ")
            name = input()
            print("Enter Price of Product(price for product quantity) :- ")
            price = input()
            print("Enter Quantity of Product :- ")
            quantity = input()

            data[productId] = {'id': productId, 'name': name,
                               'unit_price': price, 'quantity_on_hand': quantity}
        else:
            print("Product ID already present.")
        js = json.dumps(data)
        inventoryFile = open("inventory.json", 'w')
        inventoryFile.write(js)
        inventoryFile.close()

    @staticmethod
    def display_all_data():
        inventoryFile = open("inventory.json", 'r')
        txt = inventoryFile.read()
        data = json.loads(txt)
        inventoryFile.close()
        print("---- Product list ------")
        for product in data:
            print(data[product])

    @staticmethod
    def search_product():
        inv_file = open("inventory.json", 'r')
        text = inv_file.read()
        data = json.loads(text)
        inv_file.close()
        print("Enter the name of the product you want to search: ")
        name = input()
        result = None
        for p in data:
            product = data[p]
            if product["name"].__eq__(name):
                result = product
                break

        if result is None:
            print("product with name: " + name + " not found")
        else:
            print(result)
