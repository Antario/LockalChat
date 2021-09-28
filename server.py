from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


class ServerProtocol(LineOnlyReceiver):
    factory = 'Server'

    def lineReceived(self, line):
        print(f"Message {line}")


class Server(ServerFactory):
    protocol = ServerProtocol

    def startFactory(self):
        print("Server Start")


reactor.listenTCP(1234, Server())
reactor.run()
