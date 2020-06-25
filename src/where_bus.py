# where_bus.py
#
# Exercise 1.4

import urllib.request
from xml.etree.ElementTree import parse

source = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22")
doc = parse(source)

for pt in doc.findall(".//pt"):
    print(pt.text)
