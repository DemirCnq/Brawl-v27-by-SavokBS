from Packets.Messages.Server.Gameroom.TeamChatDataMessage import TeamChatDataMessage

from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader

class TeamChatMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        TeamChatDataMessage(self.client, self.player).send()