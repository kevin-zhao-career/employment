from order import Order
from shelf import Shelf

class Courier:
    def __init__(self, shelf : Shelf, order : Order, time_interval : int):
        self._shelf = shelf
        self._order = order
    
    def pick_up(self):
        self._shelf.remove_order(self._order)