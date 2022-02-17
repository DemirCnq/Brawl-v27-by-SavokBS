from Utils.Writer import Writer


class MatchmakingInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20405
        self.player = player

    def encode(self):
        self.writeInt(20) # Timer (but it's don't work in v12 :( )
        self.writeInt(3) # Players founded
        self.writeInt(6) # Max players
