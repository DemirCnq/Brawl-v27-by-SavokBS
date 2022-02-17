from Utils.Writer import Writer

class TeamChatDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24359
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("Player")
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("Test")        