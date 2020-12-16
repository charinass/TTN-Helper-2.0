import paho.mqtt.client as mqtt


class Authentication:
    """
    To make sure that each user who registers has an actual account in TTN.
    Call validate_user() with parameters of username and passphrase created in TTN.
    """

    def __init__(self):
        self.the_broker = "eu.thethings.network"
        self.the_topic = "+/devices/+/up"
        self.client = mqtt.Client()

    def validate_user(self, username, passphrase):
        self.username = username
        self.passphrase = passphrase
        self.client.username_pw_set(self.username, password=self.passphrase)
        self.client.on_connect = self.on_connect
        self.client.connect(self.the_broker, 1883, 60)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        """
        The value of rc determines success or not:
        0: Connection successful
        1: Connection refused - incorrect protocol version
        2: Connection refused - invalid client identifier
        3: Connection refused - server unavailable
        4: Connection refused - bad username or password
        5: Connection refused - not authorised
        6-255: Currently unused.
        """
        self.rc_checker = rc
        print("Connected to ", client._host, "port: ", client._port)
        print("Flags: ", flags, "return code: ", rc)
        if self.rc_checker > 0 and self.rc_checker < 6:
            print("Account not found")
            self.client.disconnect()
        else:
            self.client.subscribe(self.the_topic)
