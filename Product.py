import random as r


class Product:

    def __init__(self, name):
        self.name = "Продукт № " + str(name)
        self.price = r.randint(1, 5000)
        self.nutritionalValue = r.randint(0, 100)
        self.energyValue = r.randint(0, 100)
        self.quality = r.randint(0, 100)
