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
        self.threshold = str(conf['configuration']['threshold'])
        self.devices = str(conf['configuration']['devices'])

        self.hostname = str(conf['email']['hostname'])
        self.username = str(conf['email']['username'])
        self.sender = str(conf['email']['sender'])
        self.receivers = str(conf['email']['receivers'])
        self.password = str(conf['email']['password'])
        self.port = str(conf['email']['port'])
        self.tls = str(conf['email']['tls'])
        if self.tls.lower() == "true":
            self.tls = True
        else:
            self.tls = False



        # Turn devices into a usable array
        self.devices = self._create_array(self.devices)

        # Turn receivers into a usable array
        self.receivers = self._create_array(self.receivers)

