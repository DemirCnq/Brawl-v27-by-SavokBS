from Packets.Messages.Server.Battle.VisionUpdate import VisionUpdate
from Packets.Messages.Server.Battle.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.Battle.UDPConnectionInfo import UDPConnectionInfo

import time
from threading import Thread

class Battle(Thread):
    def __init__(self, client, player):
        Thread.__init__(self)
        self.client = client
        self.player = player
        self.subTick = 0
        self.tick = 0
        self.started = 0
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.client, self.player).send()
        UDPConnectionInfo(self.client, self.player).send()
        while self.started:
            if True:#self.subTick >= 4:
                self.tick += 1
                self.subTick = 0
                self.player.battleTick = self.tick
                #print("Tick: ", self.tick)
            self.process()
            time.sleep(0.045)

    def process(self):
        VisionUpdate(self.client, self.player).send()
        #self.subTick += 1