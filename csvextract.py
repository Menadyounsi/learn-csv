import csv

f = open("Inventorylist.csv", "rt")

try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()
