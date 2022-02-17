from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Packets.Messages.Server.Battle.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.Battle.VisionUpdate import VisionUpdate
from Packets.Messages.Server.Battle.UDPConnectionInfo import UDPConnectionInfo
from Logic.Battle import Battle
import time
from Utils.Reader import BSMessageReader


class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.tick = 0


    def decode(self):
        self.read_Vint()
        self.CardID = self.read_Vint()

        self.read_Vint()
        self.MapIndex = self.read_Vint()

        print(self.CardID, self.MapIndex)

    def process(self):
        UDPConnectionInfo(self.client, self.player).send()
        battle = Battle(self.client, self.player)
        battle.start()