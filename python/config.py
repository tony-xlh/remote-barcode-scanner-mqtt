# MQTT broker. The web page connects over WebSockets
# (ws://broker:8083 or wss://broker:8084), this Python receiver connects over
# plain MQTT TCP (port 1883). Public brokers are fine for testing; run your own
# mosquitto for production, then set broker_hostname = "127.0.0.1" here and edit
# web/index.html.
broker_hostname = "broker.emqx.io"
broker_port = 1883

topic = "barcode"

# Text injected around every scan received from the phone
text_to_prepend = ""
text_to_append = ""
keys_to_prepend = []
keys_to_append = ["enter"]