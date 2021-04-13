import io
import json
import logging
import time

import logger
from kitchen import Kitchen
from order import Order
from shelf import Shelf

#@logger.log_on_start(logging.DEBUG, "HI")
def read_json_file(filename : str) -> io.TextIOWrapper:
    order_json_file = open(filename)
    return order_json_file

#@logger.log_on_start(logging.DEBUG, "HI 2")
def get_json_data(json_file :  io.TextIOWrapper) -> list:
    json_data = json.load(json_file)
    return json_data

#@logger.log_on_start(logging.DEBUG, "HI 3")
def emit_every_time_interval(json_data, time_interval: int, kitchen: Kitchen):
    for data_object in json_data:
        order = Order(data_object)
        print(order)
        kitchen.cook_order(order)
        
        time.sleep(time_interval)
    return

def main():
    filename = 'orders.json'
    json_data = get_json_data(read_json_file(filename))
    shelf_type_to_capacity_dict = {
        "hot" : 10,
        "cold" : 10,
        "frozen" : 10,
        "overflow" : 10
    }

    shelf = Shelf(shelf_type_to_capacity_dict=shelf_type_to_capacity_dict)
    kitchen = Kitchen(shelf = shelf)

    emit_every_time_interval(json_data, 2, kitchen)

    return

    

