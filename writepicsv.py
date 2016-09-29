import csv
import math

f = open("pi.csv", "wt")
pi = math.pi
pistr = (str(pi))[2:]

try:
    writer = csv.writer(f)
    writer.writerow( ("Pi decimal place", "Value") )
    writer.writerow( ("", "3") )
    writer.writerow( ("", ".") )
    count = 1
    for char in pistr:
        writer.writerow((count,char))
        print str(count) + " " + char
        count += 1
finally:
    f.close()

print open("pi.csv", "rt").read()
print pistr
