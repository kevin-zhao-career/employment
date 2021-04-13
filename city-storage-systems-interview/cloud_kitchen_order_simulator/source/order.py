class Order:
    def __init__(self, order_dict : dict):
        self.order_dict = order_dict

    def __repr__(self):
        representation = """
        id: {id},
        name: {name},
        temperature: {temp},
        shelf life: {shelfLife},
        decay rate: {decayRate}""".format(**self.order_dict)
        return representation