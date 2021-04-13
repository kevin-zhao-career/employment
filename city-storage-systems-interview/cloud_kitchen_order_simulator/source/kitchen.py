from order import Order
from shelf import Shelf

class Kitchen:
    def __init__(self, shelf : Shelf):
        self._shelf = shelf
        return

    def cook_order(self, order: Order):
        self._shelf.add_order(order)
        print(self._shelf)
        return
