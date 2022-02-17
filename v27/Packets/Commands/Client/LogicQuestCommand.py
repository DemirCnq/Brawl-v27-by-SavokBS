from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicQuestDataCommand import LogicQuestDataCommand

from Utils.Reader import BSMessageReader

class LogicQuestCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        LogicQuestDataCommand(self.client, self.player).send()