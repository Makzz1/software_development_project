"""
about element:
ele = {'move': 0, "order": {'briyani': 10, 'dosa': 5}}
should be in this format
"""


class Queue:
    def __init__(self):
        self.order = []
        self.priority = 3
        self.pos = 0
        self.move = 0

    def add(self, ele):
        order_count = ele['order'].values()
        length = sum(order_count)
        if self.move >= 3:
            self.pos = len(order_count) - self.move
            self.order.append(ele)
            self.move = 0
        elif length > self.priority and self.move < 3:
            # elments are added to the array
            self.order.append(ele)
        else:
            self.order.insert(self.pos, ele)
            self.pos += 1
            self.move += 1

    def remove(self):
        # elements to be removed
        if len(self.order) > 0:
            self.order.pop(0)
            self.pos -= 1
        else:
            print("there is not enough elements")

    def display(self):
        print(self.order)
