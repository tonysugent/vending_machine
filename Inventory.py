import sqlite3
import Product


class Inventory:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def loadinventory(self):
        results = []
        invinput = self.c.execute('select * from items')

        for i in invinput:
            results.append(Product.Product(i[0], i[1], i[2]))

        return results





