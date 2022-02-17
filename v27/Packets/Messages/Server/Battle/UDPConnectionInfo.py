from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class UDPConnectionInfo(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24112
        self.player = player


    def encode(self):
        self.writeVint(9339) # Server Port
        self.writeString() # Server IP
        self.writeInt(0)
        self.writeByte(0)
        self.writeInt(0)
        self.writeByte(0)


