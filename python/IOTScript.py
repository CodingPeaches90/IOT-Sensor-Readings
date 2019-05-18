import dweepy, time
import time
import sqlite3
import grovepi
from grovepi import *

#We set up our ports
light_sensor = 0
grovepi.pinMode(light_sensor,"INPUT")
dht_sensor_port = 2

#Firstly we get the name of the thing from our config file
#as defined by the CA Descriptor

#get the name of the thing from our config file and store the string into a var
with open('config.txt','r') as f:
    nameOfThing = f.read().replace('\n','')

#Get our Temperature values, the temp|hum sensor returns both values so we seperate them
def getTemp():
    #we use a try except incase we get a ioerror, we want to output 0 so our submitted data does not fail
    try:
        [ temp,hum ] = dht(dht_sensor_port,0)
        t=temp
        return t
    except IOError:
        return 0
    
def getHumidity():
    try:
        [ temp,hum ] = dht(dht_sensor_port,0)
        h=hum
        return h
    except IOError:
        return 0
#Sensor data method
def getLightSensor():
    try:
        sensor_value = grovepi.analogRead(light_sensor)    
        s = sensor_value
        #print(s)
        return s
    except IOError:
        return 0
#post our dictionary with the values to Dweet.io at our described thing name
def post(dic):
    #thing = 'mymacbookandi'
    print(dweepy.dweet_for(nameOfThing, dic))
#store all values in one dictionary under the appropriate headings
def getReadings():
    dict = {}
    dict["temperature"] = getTemp();
    dict["humidity"] = getHumidity()
    dict["light"] = getLightSensor()
    #connect to out db, and execute our query and close the connection
    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    c.execute("INSERT INTO sensorValues (Temperature, Humidity, Light) VALUES(?, ?, ?)", (getTemp(), getHumidity(), getLightSensor()))
    conn.commit()
    print("Successfully Commited to Database")
   
    return dict

while True:
    #continously do this every 5 seconds
    dict = getReadings();
    post(dict)
    time.sleep(5)