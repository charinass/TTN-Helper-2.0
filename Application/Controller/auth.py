import paho.mqtt.client as mqtt
import logging
import time

from ..Models.TTN_User import TTN_User


class Authentication:
    """
    Those who log in must have an account registered.
    Call check_if_user_exist() with parameters of username and passphrase created in TTN.
    """

    def check_if_user_exist(username, passphrase):
        query_if_exist = TTN_User.query.filter(username == TTN_User.username).first()
        if (
            query_if_exist.username == username
            and query_if_exist.password == passphrase
        ):
            return True
        else:
            return False


class User:
    """
    Add a non-existing user for the app.
    Call check_if_user_valid() to check if user is registered in TTN.
    """

    def __init__(self):
        self.client = mqtt.Client()
        self.rc_checker = ""

    def check_if_user_valid(self, username, passphrase, the_broker, the_topic):
        self.username = username
        self.passphrase = passphrase
        self.the_broker = the_broker
        self.the_topic = the_topic

        self.client.username_pw_set(self.username, password=self.passphrase)
        try:
            self.client.on_connect = self.on_connect
            self.client.connect(self.the_broker, 1883, 60)
            self.client.loop_forever()
        except:
            logging.error("Error in connecting.")

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
        if not self.rc_checker == 0:
            logging.info("Account not found")
            self.client.disconnect()
        else:
            time.sleep(7)
            self.client.disconnect()
