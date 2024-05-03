class Queue:
    def __init__(self):
        self.order = [] #
        self.priority = 3
        self.pos = 0
        self.

    def add(self, ele):
        if len(ele) > self.priority:
        # elments are added to the array
            self.order.append(ele)
        else:
            self.order.insert(self.pos, ele)
            self.pos += 1

    def remove(self):
        # elements to be removed
        if len(self.order) > 0:
            self.order.pop(0)
            self.pos -= 1
        else:
            print("there is not enough elements")


