import queue
order = queue.Queue()


ele = {"order": {'briyani': 10, 'dosa': 5}}
ele1 = {"order": {'briyani': 1, 'dosa': 5}}
ele2 = {"order": {'briyani': 19, 'dosa': 5}}
ele3 = {"order": {'briyani': 1, 'dosa': 1}}
ele4 = {"order": {'briyani': 1, 'dosa': 2}}
ele5 = {"order": {'briyani': 1, 'dosa': 1}}
ele6 = {"order": {'briyani': 10, 'dosa': 50}}
ele7 = {"order": {'briyani': 1, 'dosa': 1}}

order.add(ele)
order.add(ele1)
order.add(ele2)
order.add(ele3)
order.add(ele4)
order.add(ele5)
order.add(ele6)
order.add(ele7)

order.display()