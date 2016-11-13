#!/usr/bin/python
import sys
import datetime
import Adafruit_DHT

today = datetime.date.today()
tempList = []
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

for x in range(0, 5):
	tempList = [temperature]
	
newTempVar = sum(tempList) / float(len(tempList))
print newTempVar
	



   
