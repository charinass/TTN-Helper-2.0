import paho.mqtt.client as mqtt


class Authentication:
    def __init__(self, username, passphrase):
        self.username = username
        self.passphrase = passphrase
        self.is_user_valid = True
        self.client = mqtt.Client()

    def validate_user(self):
        try:
            self.client.username_pw_set(self.username, password=self.passphrase)
            self.client.on_connect = self.__on_connect
            self.client.connect("random", 1883, 60)
        except:
            self.is_user_valid = False
            print(self.is_user_valid)

    def __on_connect(self, client, userdata, flags, rc):
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
        print("Connected to ", client._host, "port: ", client._port)
        print("Flags: ", flags, "return code: ", rc)
        if rc >= 1 and rc <= 5:
            self.is_user_valid = False
            print("Failed to connect.")
