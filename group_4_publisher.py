import json
import sys
import time
import group_4_display_bar
import paho.mqtt.client as mqtt
import tempStorage
import utils


def on_connect(mqttc, userdata, flags, rc):
    print('connected...rc=' + str(rc))


def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))


def on_message(mqttc, userdata, msg):
    print('message received...')
    print('topic: ' + msg.topic + ', qos: ' + 
          str(msg.qos) + ', message: ' + str(msg.payload))


def on_publish(mqttc, userdata, mid):
    print("Message published ID :{}".format(mid))


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.connect('mqtt.eclipseprojects.io')

max_msg = 2
count = 0
while True:
    try:
        msg_dict = tempStorage.temp1
        data = json.dumps(msg_dict)
        mqttc.publish(topic='network', payload=data, qos=0)
        print("Published msg: {}".format(msg_dict))
        # count += 1
        # if count >= max_msg:
        #     break  
        time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        mqttc.disconnect()
        sys.exit()

mqttc.disconnect()
