"""
about element:
ele = {"order": {'briyani': 10, 'dosa': 5}}
should be in this format
"""

PUSH_LIMIT = 3
class Queue:
    def __init__(self):
        self.order = []
        self.priority = 3
        self.pos = 0
        self.move = 0

    def add(self, ele):
        order_count = ele['order'].values()
        length = sum(order_count)
        if self.move >= PUSH_LIMIT:
            self.pos = len(order_count) - PUSH_LIMIT
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
        for i in self.order:
            print(i)
