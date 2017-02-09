#python 2.7
#initialisation de ma grille de jeu

class Maps:
	def __init__(self, name, x, y):
		self.map = []


class Grid:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
		self.map = [[]]
		self.map = [[0 for i in xrange(x)] for i in xrange(y)]#writes Zeros at each position in the map

	def display(self):

		for i in xrange(self.x):
			print self.map[i]

firstMap = Grid("Alabama", 10, 12)

secondMap = Grid("Texas", 15, 30)

thirdMap = Grid("Montana", 3, 5)

print firstMap.name

firstMap.display()



print secondMap.name

secondMap.display()



print thirdMap.name

thirdMap.display()




	#print de ma grille de jeu
#for i in xrange(grid.x):
#	print grid.map[i]
