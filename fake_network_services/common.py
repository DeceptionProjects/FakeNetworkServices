from time import strftime
from twisted.python import log

from datetime import datetime
from elasticsearch import Elasticsearch

import requests

class PotFactory:
    def __init__(self, logfile=None, proto=None, logserver=None, api_key=None):
        self.logfile = logfile
        self.proto = proto
        self.logserver = logserver
        self.api_key = api_key

        if self.logserver:
            self.es = Elasticsearch(
                "https://localhost:9200",
                #api_key=("X8XE5YYBT-Nm0yE218vE", "WDhYRTVZWUJULU5tMHlFMjE4dkU6N3B6eWRBUmVRNDJXdEpmRnZESV9CUQ=="),
                basic_auth=("elastic", "-97z1wUJcnE_Y31SuYg-"),
                verify_certs=False
            )

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
            doc = {
                'type': 'honey_service',
                'protocol': self.proto,
                'user': user,
                'password': password,
                'from_host': host,
                'timestamp': datetime.now(),
            }

            resp = self.es.index(index="deception_alerts", document=doc)
