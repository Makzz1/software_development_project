import csv
import time
import queue

'''DONT CHANGE MAIN
FOR NOW IT REPRESENT THE ORDER MENU PAGE'''

queue = queue.Queue()

def update_csv(filename):
    # Open the CSV file in append mode
    with open(filename, 'w', newline='') as csvfile:
        for i in queue.order:
            print(i)
            writer = csv.writer(csvfile)
            writer.writerow([list(i['order'].keys()), list(i['order'].values())])



# Example usage
while True:
    # Update CSV file with new data every second
    dish = input("dish:") # should be converted into dictionary
    no_dish = int(input("no of dishes:"))
    data_to_write = {'order':{dish:no_dish}}
    queue.add(data_to_write)
    update_csv("order.csv")
    time.sleep(1)

