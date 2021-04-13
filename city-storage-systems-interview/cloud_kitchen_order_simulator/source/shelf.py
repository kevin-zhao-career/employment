from order import Order
from typing import Final

class Shelf:
    OVERFLOW_TEMP : Final = "overflow"
    TEMPERATURE_KEY : Final = "temp"

    def __init__(self, shelf_type_to_capacity_dict : dict):
        self._shelf_type_to_capacity_dict = shelf_type_to_capacity_dict
        self.shelves = {
            shelf_type : []
            for shelf_type, shelf_capacity in self._shelf_type_to_capacity_dict.items()
        }

    def add_order(self, order: Order):
        order_temp = order.order_dict[self.TEMPERATURE_KEY]
        
        if order_temp not in self.shelves:
            raise KeyError

        if order_temp not in self._shelf_type_to_capacity_dict:
            raise KeyError
        
        capacity = self._shelf_type_to_capacity_dict[order_temp]
        while len(self.shelves[order_temp]) >= capacity:
            if order_temp == self.OVERFLOW_TEMP:
                raise Exception
            order_temp = self.OVERFLOW_TEMP

        self.shelves[order_temp].append(order)

        return
    
    def remove_order(self, order: Order):
        order_temp = order.order_dict[self.TEMPERATURE_KEY]
        
        if order_temp not in self.shelves:
            raise KeyError

        try:
            self.shelves[order_temp].remove(order)
        except ValueError:
            self.shelves[self.OVERFLOW_TEMP].remove(order)
            
        return

    def __repr__(self):
        representation = str(self.shelves)
        return representation
        