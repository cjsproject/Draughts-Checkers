"""

Rules of checkers:
https://www.officialgamerules.org/checkers

todo: 
	1/create a board *done
	2/put pieces on it *done
	3/number green tiles 1-32 *done
	4/implement 4 fundamental movements: move of man, move of king, capture of man, capture of king

"""

BOARD_SIZE = 8

class Player:
	def __init__(self, color):
		self.color = color

	def _valid_piece(self):
		same_color = piece.color == self.color
		movable = piece.can_move()
		if same_color and moveable:
			return True
		return False


	def move(self, piece):
		if self._valid_piece(piece):
			return
		return


class Board:
	def __init__(self):
		self.Board = None
		self._createBoard()

	def _createBoard(self):
		# setting up board
		# each Tile() holds tile information (color of tile, Piece() object)
		# Piece() objects have color info r/w 
		self.Board = [[Tile((i+(j%2))%2, Piece('w')) if (j < 3 and (i+(j%2))%2) or (j > 4 and (i+(j%2))%2) else Tile((i+(j%2))%2, False) for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

		Board = self.Board
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if Board[i][j].piece and i < 3:
					Board[i][j].piece = Piece('r')
				if Board[i][j].color == 1:
					Board[i][j].number = int((BOARD_SIZE*(i) + j)/2) + 1

	def __repr__(self):
		string = ''
		for i in self.Board:
			string += str(i) + '\n'
		return string


class Tile:
	def __init__(self, color, piece):
		self.color = color
		self.piece = piece
		self.number = None

	def __repr__(self):
		string = f"({str(self.number)}, {self.piece})"
		return string


class Piece:
	def __init__(self, color):
		self.color = color
		self.king = False

	def __repr__(self):
		if self.king:
			return self.color + 'k'
		return self.color

	def movable(self):
		pass


main_board = Board()
print(main_board)