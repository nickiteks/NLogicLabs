import random as r


class Product:

    def __init__(self, name, countChar):
        self.name = "Продукт № " + str(name)
        self.price = r.randint(1, 5000)
        self.data = []
        for i in range(countChar):
            self.data.append(r.randint(1, 100))
