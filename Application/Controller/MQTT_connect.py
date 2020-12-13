import paho.mqtt.client as mqtt


class Authentication:
    def __init__(self, username, passphrase):
        self.username = username
        self.passphrase = passphrase
        self.is_user_valid = True
        self.callback = None

    def validate_user(self):
        client.username_pw_set(self.username, password=self.passphrase)

    def exec_callback(self):
        return self.callback


def test():
    print("Any message.")


if __name__ == "__main__":

    client = mqtt.Client()
    auth = Authentication("Charina", "Suzuki")
    auth.callback = test()
    auth.exec_callback()
