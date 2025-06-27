try:
    import configparser as ConfigParser
except:
    import ConfigParser


class settings(object):
    def __init__(self, filename='/etc/diskalert.conf'):
        self.filename = filename
        self.read_settings()

    def _create_array(self, value):
        value = value.split(',')
        if value[-1] == '':
            value = value[:-1]
        return value

    def read_settings(self):
        conf = ConfigParser.ConfigParser()
        conf.read(self.filename)
        self.threshold = conf.get('configuration', 'threshold')
        self.devices = conf.get('configuration', 'devices')
        self.long_hostname = conf.get('configuration', 'long_hostname')

        self.hostname = conf.get('email', 'hostname')
        self.username = conf.get('email', 'username')
        self.sender = conf.get('email', 'sender')
        self.receivers = conf.get('email', 'receivers')
        self.password = conf.get('email', 'password')
        self.port = conf.get('email', 'port')
        self.tls = conf.get('email', 'tls')
        if self.tls.lower() == "true":
            self.tls = True
        else:
            self.tls = False



        # Turn devices into a usable array
        self.devices = self._create_array(self.devices)

        # Turn receivers into a usable array
        self.receivers = self._create_array(self.receivers)

