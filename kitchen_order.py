import csv
import time
import msvcrt

def read_csv(filename):
    # Open the CSV file in read mode
    with open(filename, 'r', newline='') as csvfile:
        # Lock the file
        msvcrt.locking(csvfile.fileno(), msvcrt.LK_LOCK, 1)
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
        # Unlock the file
        msvcrt.locking(csvfile.fileno(), msvcrt.LK_UNLCK, 1)

# Example usage
while True:
    # Read from CSV file every second
    read_csv("data.csv")
    time.sleep(1)

