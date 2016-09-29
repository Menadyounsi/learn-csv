import csv

"""f = open("Inventorylist.csv", "rt")

try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()"""

f = open("test.csv", "wt")

try:
    writer = csv.writer(f)
    writer.writerow( ("Title1", "Title2", "Title3") )
    for i in range(10):
        writer.writerow((i+1, chr(ord('a') + i), '09/%02d/16' % (i+1)))
finally:
    f.close()

print open("test.csv", "rt").read()
