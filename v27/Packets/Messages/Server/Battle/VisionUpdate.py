from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Logic.Player import Players

from Utils.BitStream import BitStream

class VisionUpdate(Writer):

	def __init__(self, client, player):
		super().__init__(client)
		self.id = 24109
		self.player = player


	def encode(self):
		self.writeVint(self.player.battleTick) # Battle Ticks
		self.writeVint(self.player.dudu) # wifi posral jidko
		self.writeVint(0) # Commands Count
		self.writeVint(6974) # spectators
		self.writeBoolean(True) # Live Boolean
		
		stream = BitStream()
		
		stream.writePositiveInt(1000000 + 0, 21)
		stream.writePositiveVInt(0, 4)
		stream.writePositiveInt(20, 1)
		stream.writeInt(-1, 4) # понос

		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)


		stream.writePositiveInt(0, 5)
		stream.writePositiveInt(0, 6)
		stream.writePositiveInt(0, 5)
		stream.writePositiveInt(0, 6)

		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writeBoolean(False)

		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(9999, 12)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)

		for i in range(6):
			stream.writePositiveInt(0, 1)
			stream.writePositiveInt(0, 1)

		stream.writePositiveInt(0, 4) # unknown dudka

		# GameObjects start
		stream.writePositiveInt(1, 8) # count
		
		# objects config start
		stream.writePositiveInt(16, 5)
		stream.writePositiveInt(0, 8) # id
		# objects config end
		
		# IDs start
		stream.writePositiveInt(0, 14)
		# IDs end
			
		# player start
		stream.writePositiveVInt(self.player.battleX, 4) # x
		stream.writePositiveVInt(self.player.battleY, 4) # y
		stream.writePositiveVInt(0, 3) #i
		stream.writePositiveVInt(0, 4) # z
		stream.writePositiveInt(10, 4)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 3)
		stream.writePositiveInt(1, 1)
		stream.writeInt(63, 6)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 2)
		stream.writePositiveInt(3599, 13)
		stream.writePositiveInt(3600, 13)
		stream.writePVIntMax255OZ(10)
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 4)
		stream.writePositiveInt(0, 2)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 9)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		
		stream.writePositiveInt(0, 5)
		
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(0, 1)
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(3000, 12)
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(0, 1)
		stream.writePVIntMax255OZ(0)
		# GameObjects end

		stream.writePositiveInt(0, 8) # unknown dudka
		
		self.writeBytes(stream.getBuff())