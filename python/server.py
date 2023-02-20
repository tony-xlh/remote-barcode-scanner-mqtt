import paho.mqtt.client as mqtt
import pyautogui

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("barcode")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    pyautogui.write(msg.payload.decode())
    pyautogui.press('enter')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()