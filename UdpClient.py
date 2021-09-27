import socket 
class UdpClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def SendUdp(self,IP,port, message):
        self.sock.sendto(bytes(message, "utf-8"), (IP, port))

    def SendUdpData(self,IP,port, data):
        self.sock.sendto(data, (IP, port))
    