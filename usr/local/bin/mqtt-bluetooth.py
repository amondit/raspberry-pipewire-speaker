# subscriber.py
import paho.mqtt.client as mqtt
import os
from bluetoothctl import Bluetoothctl

b = Bluetoothctl()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("raspberry/bluetooth/#")

# the callback function, it will be triggered when receiving messages
def on_message_connect(client, userdata, msg):
    address = msg.payload.decode("utf-8")
    print(f"Connecting to {address}")
    b.connect(address)

def on_message_disconnect(client, userdata, msg):
    address = msg.payload.decode("utf-8")
    print(f"Disconnecting from {address}")
    b.disconnect(address)

def on_message_pair(client, userdata, msg):
    address = msg.payload.decode("utf-8")
    print(f"Pairing {address}")
    b.pair(address)

def on_message_remove(client, userdata, msg):
    address = msg.payload.decode("utf-8")
    print(f"Removing {address}")
    b.remove(address)

def on_message_discoverable(client, userdata, msg):
    print(f"Making discoverable")
    b.make_discoverable()

def on_message_undiscoverable(client, userdata, msg):
    print(f"Making undiscoverable")
    b.make_undiscoverable()

def on_message_reset_class(client, userdata, msg):
    print(f"Resetting bluetooth class")
    os.system('hciconfig hci0 class 0x00240414')

client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add('raspberry/bluetooth/connect', on_message_connect)
client.message_callback_add('raspberry/bluetooth/disconnect', on_message_disconnect)
client.message_callback_add('raspberry/bluetooth/pair', on_message_pair)
client.message_callback_add('raspberry/bluetooth/remove', on_message_remove)
client.message_callback_add('raspberry/bluetooth/discoverable', on_message_discoverable)
client.message_callback_add('raspberry/bluetooth/undiscoverable', on_message_undiscoverable)
client.message_callback_add('raspberry/bluetooth/reset', on_message_reset_class)

# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.will_set('raspberry/status', b'{"status": "Off"}')

# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
#client.username_pw_set("mqtt-client", "PASSWORD")
#client.connect("192.168.2.100", 1883, 60)

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
