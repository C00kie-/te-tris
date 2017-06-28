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
		self.map = [[ 0 for i in range(x)] for i in range(y)]#writes Zeros at each position in the map

	def display(self):

		for i in xrange(self.x):
			print (self.map[i])

	def apply_gravity(self):
		print("\napply_gravity()")


class Piece:
	def __init__(self, x, y, shape):
		self.current_coords = []##comment je represente ma piece ?

	#shapes  [[,],[,],[,],[,]]
	I = [[0,1],[1,1],[2,1],[3,1]]
	O = [[0,1],[0,2],[1,1],[1,2]]
	T = [[0,1],[0,2],[0,3],[1,2]]
	S = [[0,0],[0,1],[1,1],[1,2]]
	Z = [[0,2],[0,3],[1,1],[1,2]]
	J = [[0,1],[0,2],[1,2],[2,2]]
	L = [[0,1],[0,2],[1,1],[2,1]]




	def move_piece(self):
		print("\nmove_piece()")
	# def move_piece_down():
	#
	# def move_grid_down():
	#
	def checkLines(self):
		game.status = 4
	#
	# def disolve_piece():
	#
	def generate_new(self):
		print("generate_new_piece()")


#for mainloop uses
class Game:
	def __init__(self):
		self.status = 1;
		self.ticket_counter = 0


class Player:
	def __init__(self, id):
		self.id = 1

	def get_controler(self): ## input
		print("\nget_controler()")


###########test bloc#######################################################
game = Game()
piece = Piece(1,6,1)
grid = Grid("example", 10,12)
player = Player(1)

#print(game)
#print(game.status)


def mainLoop():
	# while game.status != 0:
	# 	print(game.status)
	# 	game.status = 0
	#
	# if game.status == 0:
	# 	print("\nit's done ")


	print("let's start")

	while game.status != 0:
		game.ticket_counter += 1
		print("ticket counter : ", game.ticket_counter)

		if game.status == 0:
			piece.generate_new()
			game.status = 1

		elif game.status == 1:
			player.get_controler()
			grid.apply_gravity() ## if tick counter > 60%
			piece.move_piece()
			game.status = 2
			print(game.status)

		elif game.status == 2:
			piece.checkLines()
			print(game.status)


		elif game.status == 4:
			player.get_controler()
			game.status = 0
			print(game.status)


	piece.generate_new()




mainLoop()

############################################################################
#
# firstMap = Grid("Alabama", 10, 12)
#
# secondMap = Grid("Texas", 15, 30)
#
# thirdMap = Grid("Montana", 3, 5)
#
# print firstMap.name
#
# firstMap.display()
#
#
#
# print secondMap.name
#
# secondMap.display()
#
#
#
# print thirdMap.name
#
# thirdMap.display()
#



	#print de ma grille de jeu
#for i in xrange(grid.x):
#	print grid.map[i]
