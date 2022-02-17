from Utils.Reader import BSMessageReader
from Packets.Commands.Client.LogicUpgradeBrawler import Upgrade_Brawler
from Packets.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Packets.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Packets.Commands.Client.LogicPurchaseBoxCommand import LogicPurchaseBoxCommand
from Packets.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Packets.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Packets.Commands.Client.LogicSetPlayerStarpowerCommand import LogicSetPlayerStarpowerCommand
from Packets.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Packets.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Packets.Commands.Client.LogicQuestCommand import LogicQuestCommand 
from Packets.Commands.Client.LogicBuyBrawlPassCommand import LogicBuyBrawlPassCommand
from Packets.Commands.Client.LogicBrawlPassCommand import LogicBrawlPassCommand
from Packets.Commands.Client.LogicBrawlPassTokensCommand import LogicBrawlPassTokensCommand



class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.commandID = self.read_Vint()


    def process(self):
        if self.commandID == 500 or self.commandID == 517:
            LogicPurchaseBoxCommand.decode(self)
            LogicPurchaseBoxCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 519:
            LogicPurchaseOfferCommand.decode(self)
            LogicPurchaseOfferCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 505:
            LogicSetPlayerThumbnailCommand.decode(self)
            LogicSetPlayerThumbnailCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 506:
            LogicSelectSkinCommand.decode(self)
            LogicSelectSkinCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 520:
            Upgrade_Brawler.decode(self)
            Upgrade_Brawler.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 521:
            LogicPurchaseHeroLvlUpMaterialCommand.decode(self)
            LogicPurchaseHeroLvlUpMaterialCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 533:
            LogicQuestCommand.decode(self)
            LogicQuestCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 534:
            LogicBuyBrawlPassCommand.decode(self)
            LogicBuyBrawlPassCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")

        elif self.commandID == 509:
            LogicPurchaseDoubleCoinsCommand.decode(self)
            LogicPurchaseDoubleCoinsCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")

        elif self.commandID == 527:
            LogicSetPlayerNameColorCommand.decode(self)
            LogicSetPlayerNameColorCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")

        elif self.commandID == 529:
            LogicSetPlayerStarpowerCommand.decode(self)
            LogicSetPlayerStarpowerCommand.process(self)
            print("Command ID: ", self.commandID, "has been handled")
        elif self.commandID == 535:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.boxID = self.read_Vint()
            print("Command ID: ", self.commandID, "has been handled")
            LogicBrawlPassCommand.decode(self)
            LogicBrawlPassCommand.process(self)
        elif self.commandID == 536:
            LogicBrawlPassTokensCommand.decode(self)
            LogicBrawlPassTokensCommand.process(self)

        elif self.commandID >= 0:
            print(self.commandID, "Is not handled!")