from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand

from Utils.Reader import BSMessageReader

class LogicBrawlPassCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        LogicBoxDataCommand(self.client, self.player).send()
        newLVL = self.player.free_pass_level + 1
        DataBase.replaceValue(self, 'FreePassLVL', newLVL)