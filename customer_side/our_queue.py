PUSH_LIMIT = 3


class Queue_node:
    def __init__(self,value):
        self.value = value
        self.len = sum(self.value['order'].values())
        self.move = 0
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.priority = 3
        self.pos = 0
        self.size = 0

    def add(self, ele):
        node = Queue_node(ele)

        if node.len <= self.priority:
            print(self.pos)

            if not self.head:
                self.head = node
                self.tail = node
                self.pos += 1
                self.size += 1
                return

            temp1 = self.head
            while temp1:
                if temp1.move >= PUSH_LIMIT:
                    temp1.move = 0
                    self.pos += 1

                temp1 = temp1.next

            if self.pos == 0:
                node.next = self.head
                self.head.move += 1
                self.head = node
                self.pos += 1
                self.size += 1
                return

            position = 0
            temp2 = self.head
            while position < self.pos - 1 and temp2.next:
                temp2 = temp2.next
                position += 1

            node.next = temp2.next
            temp2.next = node
            self.pos += 1

            temp2 = temp2.next.next
            while temp2:
                temp2.move += 1
                temp2 = temp2.next


        elif node.len > self.priority:
            if not self.head:
                self.head = node
                self.tail = node
                return

            self.tail.next = node
            self.tail = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.value,temp.move)
            temp = temp.next

if __name__ == "__main__":
    ele1 = {"order": {'briyani': 10, 'dosa': 5}}
    ele2 = {"order": {'briyani': 0, 'dosa': 1}}
    ele3 = {"order": {'briyani': 0, 'dosa': 2}}
    ele4 = {"order": {'briyani': 1, 'dosa': 1}}
    ele5 = {"order": {'briyani': 2, 'dosa': 3}}
    ele6 = {"order": {'briyani': 1, 'dosa': 1}}
    ele7 = {"order": {'briyani': 1, 'dosa': 1}}
    ele8 = {"order": {'briyani': 1, 'dosa': 1}}
    ele9 = {"order": {'briyani': 1, 'dosa': 1}}
    ele10 = {"order": {'briyani': 2, 'dosa': 3}}
    ele11 = {"order": {'briyani': 1, 'dosa': 1}}

    queue = Queue()
    queue.add(ele1)
    queue.add(ele2)
    queue.add(ele3)
    queue.add(ele4)
    queue.add(ele5)
    queue.add(ele6)
    queue.add(ele7)
    queue.add(ele8)
    queue.add(ele9)
    queue.add(ele10)
    queue.add(ele11)

    queue.display()
