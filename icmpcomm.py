from scapy.all import *

import threading

class MonitorThread(threading.Thread):
  def __init__(self):
    super().__init__()
    self.abort = False
    self.threadLock = threading.Lock()
    self.caughtPackets = []
  def run(self):
    print("Starting sniffing thread...")
    while not self.abort:
      tempPackets = sniff(filter="icmp[0]=8", count=1, timeout=1)
      self.threadLock.acquire()
      self.caughtPackets.extend(tempPackets)
      self.threadLock.release()
    print("Aborting sniffing thread...")
  def getPackets(self):
    self.threadLock.acquire()
    ret = self.caughtPackets
    self.caughtPackets = []
    self.threadLock.release()
    return ret
