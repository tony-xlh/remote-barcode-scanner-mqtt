import paho.mqtt.client as mqtt
import pyautogui
import config
import pyperclip
import sys
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("barcode")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    barcode = msg.payload.decode()
    if config.text_to_prepend != "":
      barcode = config.text_to_prepend + barcode
    if config.text_to_append != "":
      barcode = barcode + config.text_to_append
    for key in config.keys_to_prepend:
      pyautogui.press(key)
    pyperclip.copy(barcode)
    time.sleep(0.5)
    if sys.platform == 'darwin':
      pyautogui.hotkey('command', 'v')
    else:
      pyautogui.hotkey('ctrl', 'v')
    for key in config.keys_to_append:
      pyautogui.press(key)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()