import csv
from bs4 import BeautifulSoup
import requests

dive_log = open("divelog.csv", "wt")
url_page = "https://en.divelogs.de/log/Mark_Gosling"
r = requests.get(url_page)
soup = BeautifulSoup(r.content)

dive_data1 = soup.find_all("tr", {"class": "td2"})
#dive_data2 = soup.find_all("td", {"class": "td"})
locations = []
depths = []

try:
    for i in range(0,1000):
        location = dive_data1[((9*i)-7)].text
        locations.append(location)
        #location = dive_data2[((9*i)-7)]
        #locations.append(location)
        depth = dive_data1[((9*i)-6)].text
        depths.append(depth)
        #depth = dive_data2[((9*i)-6)].text
        #depths.append(depth)

except:
    pass

try:
    writer = csv.writer(dive_log)
    writer.writerow( ("Locations and depths","") )
    writer.writerow( ("Sourced from:", str(url_page)) )
    writer.writerow( ("Location", "Depth") )
    for i in range(len(locations)):
        writer.writerow( (locations[i].decode("utf-8"), depths[i].decode("utf-8")) )

finally:
    dive_log.close()

print open("divelog.csv", "rt").read()
print "\n\n"
print locations
