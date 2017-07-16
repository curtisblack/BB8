import os
import time
import socket
import logging

class Network:
    def __init__(self):
        self.IP = None
        self.lastUpdateTime = time.time()
        self.incoming = None
        self.MACs = { "b8:27:eb:fa:26:48": "BB8",
                      "b8:27:eb:c4:25:de": "R2D2",
                      "b8:27:eb:91:70:8b": "R2D2" }
        self.IPs = { "R2D2": None, "BB8": None }
        self.outgoing = socket.socket(socket.AF_INET, socket.DGRAM)
        self.messages = { "R2D2": [], "BB8": [] }
        self.port = 5000

    def Update(self):
        t = time.time()

        if t > self.lastUpdateTime + 1:
            ip = None
            try:
                ip = os.popen("ip addr show wlan0").read().split("inet ")[1].split("/")[0]# + " " + os.popen("iwgetid -r").read()
            except:
                try:
                    ip = os.popen("ip addr show eth0").read().split("inet ")[1].split("/")[0]
                except:
                    ip = None
            if self.IP != ip:
                self.IP = ip
                if self.incoming != None:
                    self.incoming.close()
                if self.IP != None:
                    print "opening port on", self.IP
                    self.incoming = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    self.incoming.bind((self.IP, self.port))
                    for i in range(255):
                        self.outgoing.sentto("hi", ("192.168.0." + str(i), self.port))
                else:
                    self.incoming = None

        if self.incoming != None:
            try:
                data, (address, port) = self.incoming.recvfrom(1024)
                mac = os.popen("arp -na | grep " + address + " | cut -d' ' -f4").read().split("\n")[0]
                if mac in self.MACs:
                    droid = self.MACs[mac]
                    if self.IPs[droid] != address:
                        print "Discovered", droid
                        self.IPs[droid] = address
                    if data == "hi":
                        self.Send(droid, "return")
                    else:
                        self.messages[droid].append(data)
            except socket.error:
                pass

    def Receive(self, droid):
        if len(self.messages[droid]) > 0:
            msg = self.messages[droid][0]
            del self.messages[droid][0]
            return msg
        return None

    def Send(self, droid, message):
        ip = self.IPs[droid]
        if ip != None:
            self.outgoing.sendto(message, (ip, self.port))
