#!/usr/bin/python
import sys
import datetime
import Adafruit_DHT
import MySQLdb
import time

database = MySQLdb.connect(host='localhost',user='root',passwd='root',db='Project_Database')# link to database




cursor = database.cursor()
tempList = []
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

Epoch = int(time.time())
print "The Epoch is:  %s." % Epoch
for x in range(0, 10):
	tempList = [temperature]
	

newTempVar = sum(tempList) / float(len(tempList))

#cursor.execute(''' INSERT INTO `temperature`(`temp`) VALUES (%s,CURRENT_TIMESTAMP) ''',(newTempVar))
cursor.execute(''' INSERT INTO `temperature`(`epoch`, `temp`) VALUES (%s,%s) ''',(Epoch,newTempVar))


database.commit()
#time.sleep(1)
#print newTempVar
#print dateTime	



   
