import datetime
import Adafruit_DHT
import MySQLdb
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

triggerPin = 23         ########## declare pin variables
echoPin = 24
humidity, temperature = Adafruit_DHT.read_retry(11, 4)     ######## call adafruit

GPIO.setup(triggerPin,GPIO.OUT)  ####### set triggerPin as output and echoPin as input
GPIO.setup(echoPin,GPIO.IN)

database = MySQLdb.connect(host='localhost',user='root',passwd='root',db='Project_Database')# link to database
cursor = database.cursor() 

tempList = []  ###### create a few  arrays to store tempreture/humidity/distance readings
#humidList = []   
#disList = [] 

epoch = int(time.time()) ###### return epoch value

for xx in range(0, 10):  ######### this for loop reads ten tempreture values into tempList and returns the average in newTempVar##
        tempList = [temperature]
newTempVar = sum(tempList) / float(len(tempList))

#for ii in range(0,10):
#	humidList = [humid]
#newHumidVar = sum(humidList) / float(len(humidList))


GPIO.output(triggerPin, False)     #### sets trigger low
time.sleep(5)                      ##### delay for 5 seconds to allow the sensor to calibrate a good reading

GPIO.output(triggerPin, True)      ##### sets the trigger high
time.sleep(0.00001)                #####allow for delay of 0.00001 seconds
GPIO.output(triggerPin, False)     ######sets the trigger back to low

while GPIO.input(echoPin)==0:
        lastLowPulse = time.time()
while GPIO.input(echoPin)==1:
        lastHighPulse = time.time()

difference = lastHighPulse - lastLowPulse

tempdistance = difference * 17150
distance = round(tempdistance, 2)
GPIO.cleanup()

cursor.execute(''' INSERT INTO `sensors`(`epoch`, `temp`,`distance`) VALUES (%s,%s,%s) ''',(epoch,newTempVar,distance)) ###### inserts data into my database

database.commit() ######### commits to database
database.close() ####### close connection

