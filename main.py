#python 2.7
#initialisation de ma grille de jeu

grid = [[]]

x, y = 10, 12

grid = [[0 for i in xrange(x)] for i in xrange(y)]


#print de ma grille de jeu
for i in xrange(x):
	print grid[i]
