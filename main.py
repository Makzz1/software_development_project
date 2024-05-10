import csv
import time
import msvcrt

def update_csv(filename, data):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as csvfile:
        # Lock the file
        msvcrt.locking(csvfile.fileno(), msvcrt.LK_LOCK, 1)
        writer = csv.writer(csvfile)
        writer.writerow(data)
        # Unlock the file
        msvcrt.locking(csvfile.fileno(), msvcrt.LK_UNLCK, 1)

# Example usage
while True:
    # Update CSV file with new data every second
    data_to_write = [input("h:")]
    update_csv("order.csv", data_to_write)
    time.sleep(1)

