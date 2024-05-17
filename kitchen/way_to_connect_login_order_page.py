import csv
import time
import order_display




def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data


def detect_csv_changes(filename):
    flag = False
    previous_data = read_csv(filename)

    while True:
        kitchen = order_display.Order_display()
        current_data = read_csv(filename)

        if current_data != previous_data:
            print("CSV file has been modified.")
            previous_data = current_data
            flag = True

        if flag:
            kitchen = order_display.Order_display()
            flag = False



detect_csv_changes('../customer_side/order.csv')

