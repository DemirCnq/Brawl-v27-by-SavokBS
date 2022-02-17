from Utils.Writer import Writer

class LobbyInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        self.writeInt(666) # Players Online
