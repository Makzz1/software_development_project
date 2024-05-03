import queue
ele = {'move': 0, "order": {'briyani': 10, 'dosa': 5}}
order_list= queue.Queue()
order_list.add([1])
order_list.add([1,2,3])
order_list.add([1,2])
order_list.add([1, 3, 4, 4, 4, 4, 1])
order_count = ele['order']
length = sum(order_count)
print(length)
