from time import strftime
from twisted.python import log

import requests

class PotFactory:
    def __init__(self, logfile=None, proto=None, logserver=None):
        self.logfile = logfile
        self.proto = proto
        self.logserver = logserver

    def update_pot(self, login, password, host):
        proto_str = ""
        if self.proto:
            proto_str = self.proto
        log.msg('Thank you %s - %s : %s' % (host, login.decode("utf8"), password.decode("utf8")))
        if self.logfile:
            line = "%s %s: %s : %s : %s\n" % (strftime('%F %T'), proto_str, host, login.decode("utf8"), password.decode("utf8"))

            open(self.logfile, 'a').write(line)

    def alert_defender(self, user, password, host):
        if self.logserver:
            data = {'type': 'service', 'protocol': self.proto, 'user': user, 'password': password, 'from_host': host}
            r = requests.post(self.logserver, data=data)
