import paho.mqtt.client as mqtt
import time
import configparser
import sys

config = configparser.RawConfigParser(allow_no_value=True)
config.read("watermeter_config.ini")

log_path = config.get('Logging', 'log_path', fallback='/var/log/solar/')
do_raw_log = config.getboolean('Logging', 'do_raw_log')

mqttBroker = config.get('watermeter', 'mqttBroker')
mqttPort = int(config.get('watermeter', 'mqttPort'))
mqttKeepAlive = int(config.get('watermeter', 'mqttKeepAlive'))

print(mqttBroker)
current_value = 0
pulse_count = 0

def on_message(client, userdata, msg):
    global current_value 
    global pulse_count
    print("test 1")
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))
    if msg.topic .lower() == "watermeter/reading/current_value" :
        current_value = int(str(msg.payload.decode("utf-8")))
    if msg.topic .lower() == "watermeter/reading/pulse_count" :
        pulse_count = int(str(msg.payload.decode("utf-8")))
    print("test 2")
    print( current_value )
    print ( pulse_count )
    
def getData():
    print("GetData")
    client = mqtt.Client("reader")
    client.connect(mqttBroker, mqttPort, mqttKeepAlive) 

    client.loop_start()

    client.subscribe("#")
    client.on_message=on_message 

#    client.loop_forever()

    time.sleep(10)
    client.loop_stop()

while True:
    try: 
        getData()
    except:
        pass
