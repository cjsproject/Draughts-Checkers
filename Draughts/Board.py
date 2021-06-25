"""

Rules of checkers:
https://www.officialgamerules.org/checkers

todo: 
	1/create a board
	2/put pieces on it
"""

BOARD_SIZE = 8

class Square:
	def __init__(self, color, piece):
		self.color = color
		self.piece = piece

	def __repr__(self):
		string = f"({str(self.color)}, {self.piece})"
		return string


class Piece:
	def __init__(self, color):
		self.color = color

	def __repr__(self):
		return self.color


# setting up board
# each Square() holds tile information (color of tile, Piece() object)
# Piece() objects have color info r/w
Board = [[Square((i+(j%2))%2, Piece('r')) if (j < 3 and (i+(j%2))%2) or (j > 4 and (i+(j%2))%2) else Square((i+(j%2))%2, False) for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

for i in range(BOARD_SIZE):
	for j in range(BOARD_SIZE):
		if Board[i][j].piece and i < 3:
			Board[i][j].piece = Piece('w')
		elif i > 3:
			break

for i in Board:
	print(i)
