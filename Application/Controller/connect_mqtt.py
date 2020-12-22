import base64, json, requests, struct
from paho.mqtt import client as mqtt


class Connect:
    def __init__(self, username, passphrase, the_broker, the_topic):
        self.client = mqtt.Client()
        self.username = username
        self.passphrase = passphrase
        self.the_broker = the_broker
        self.the_topic = the_topic
        self.json_msg = None

    def start_connecting(self):
        self.client.username_pw_set(self.username, password=self.passphrase)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.the_broker, 1883, 60)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to ", client._host, "port: ", client._port)
        print("Flags: ", flags, "return code: ", rc)
        client.subscribe(self.the_topic)

    def on_message(self, client, userdata, msg):
        self.json_msg = json.loads(msg.payload.decode("utf-8"))
        payload_plain = base64.b64decode(self.json_msg["payload_raw"])

    def get_message(self):
        return {} if self.json_msg is None else self.json_msg

    def stop_connecting(self):
        self.client.disconnect()
