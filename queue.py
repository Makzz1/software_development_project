class Queue:
    def __init__(self):
        self.arr = []
        self.priority = 3
        self.pos = 9

    def add(self, ele):
        if len(ele) > self.priority:
        # elments are added to the array
            self.arr.append(ele)
        else:
            self.arr.insert(self.pos,ele)
            self.pos += 1

    def remove(self):
        # elements to be removed
        if len(self.arr) > 0:
            self.arr.pop(0)
            self.pos -= 1
        else:
            print("there is not enough elements")


