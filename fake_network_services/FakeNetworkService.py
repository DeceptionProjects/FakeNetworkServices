import argparse

from .sshpot import PotSSHFactory
from .telnetpot import PotTelnetFactory
from .ftppot import PotFTPFactory
from twisted.internet import reactor

class FakeNetworkService:
    def __init__(self, port, log_path):
        self.port = port
        self.log_path = log_path

    def start_ssh(self):
        t = PotSSHFactory(self.log_path, "ssh")
        reactor.listenTCP(self.port, t)
        reactor.run()

    def start_telnet(self):
        t = PotTelnetFactory(self.log_path, "telnet")
        reactor.listenTCP(self.port, t)
        reactor.run()

    def start_ftp(self):
        t = PotFTPFactory(self.log_path, "ftp")
        reactor.listenTCP(self.port, t)
        reactor.run()

    def run(self, service_to_run: str):
        if service_to_run == 'ssh':
            self.start_ssh()
        elif service_to_run == 'ftp':
            self.start_ftp()
        elif service_to_run == 'telnet':
            self.start_telnet()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='Port')
    parser.add_argument('-s', '--service', help='Service')
    args = parser.parse_args()

    fakeService = FakeNetworkService(args.port, './local.log')
    fakeService.run(args.service)
