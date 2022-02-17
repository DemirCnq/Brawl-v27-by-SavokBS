from Utils.Writer import Writer
import random

class StartLoadingMessage(Writer):

	def __init__(self, client, player):
		super().__init__(client)
		self.id = 20559
		self.player = player

	def encode(self):
		self.writeInt(6) #6
		self.writeInt(0)
		self.writeInt(0)
		
		self.writeInt(6) #players count
		for i in range(6):
			self.writeInt(0) #High ID
			self.writeInt(self.player.low_id) #Low ID
			self.writeVint(i)
			teamIndex = 0
			if i > 2:
				teamIndex = 1
			self.writeVint(teamIndex)
			self.writeVint(0)
			
			self.writeInt(0) #unk
			
			self.writeScId(16, self.player.brawler_id)
			self.writeScId(29, self.player.brawlers_skins[str(self.player.brawler_id)])
			self.writeByte(0)
			self.writeString(self.player.name)
			self.writeVint(100)
			self.writeVint(28000000)
			self.writeVint(43000000)

		#PLAYERS SLOT END#
		
		self.writeInt(0) #count...
		
		self.writeInt(0) #Count
		
		self.writeInt(6) # Unknown
		
		self.writeVint(1)
		self.writeVint(1) #DrawMap
		self.writeVint(1)
		
		self.writeByte(0) #2, 39 - Spectating
		self.writeVint(0) # is Spectating
		self.writeVint(1)
		
		self.writeScId(15, 7) # map