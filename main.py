#!/usr/bin/python3

import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags, rc):
    #hier alle Topics hinzufügen auf welche man höhren möchte
    #die Zahl im Tuple ist egal, da sie nicht vom Module verwendet wird
    client.subscribe([("test/Pfad/1",0),("test/Pfad/2",0)])

#In dieser Funktion werden alle Nachrichten empfanden zu denen Subscribed wurde
#Es werden nur die Topics ausgegeben welche nicht durch spezielle Callbacks abgefangen werden
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def specific_callback(client, userdata, msg):
    print("Specific Topic: "+msg.topic+" "+str(msg.payload))

if __name__ == "__main__": # pragma: no cover
    #aufbau der MQTT-Verbindung
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    #Wird aufgerufen für ein spezielles Topic
    client.message_callback_add("test/Pfad/2", specific_callback)

    client.connect("localhost",1883,60)
    client.loop_start()

    #In diesen Teil können andere Sachen gemacht werden
    #Muss kein Loop sein es können auch Threads erstellt werden
    while True:
        time.sleep(5)
        client.publish("test/Pfad/1", "asdf")
        time.sleep(5)
        client.publish("test/Pfad/2", "jklm")

    #immer am Ende. Beendet die Verbindung mit MQTT
    client.loop_stop()
    client.disconnect()