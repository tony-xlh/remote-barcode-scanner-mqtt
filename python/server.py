import paho.mqtt.client as mqtt
import pyautogui
import config
import pyperclip
import sys
import time

def on_connect(client, userdata, flags, reason_code, properties):
    # Callback signature for paho-mqtt >= 2.0 (CallbackAPIVersion.VERSION2)
    if reason_code.is_failure:
        print(f"Connection failed: {reason_code}")
        return
    print(f"Connected to {config.broker_hostname}:{config.broker_port}")
    client.subscribe(config.topic)
    print(f"Subscribed to topic '{config.topic}'. Scan a barcode on the phone...")

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

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
try:
    client.connect(config.broker_hostname, config.broker_port, 60)
except OSError as e:
    print(
        f"Could not reach the MQTT broker at {config.broker_hostname}:{config.broker_port} ({e}).\n"
        "Check your network/firewall, or run a local broker (e.g. `mosquitto`) and set\n"
        "broker_hostname = '127.0.0.1' in config.py (and the matching ws:// URL in web/index.html)."
    )
    sys.exit(1)
client.loop_forever()