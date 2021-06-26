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

def tile_num_to_index(tile_num):
	# returns the board's index of the green tile with labeled tile_num
	evens = [0, 2, 4, 6]
	odds = [1, 3, 5, 7]

	row = int((tile_num - 1)*(1/4))
	if row%2 == 1:
		col = evens[((tile_num-1)%4)]
	elif row%2 == 0:
		col = odds[((tile_num-1)%4)]

	return row, col

def parse_move(move_string):
	# parses a move of the for '12-16' or '21x14' to indicate move or capture
	if 'x' in move_string:
		jump = True
		tile1, tile2 = move_string.split('x')
	elif '-' in move_string:
		jump = False
		tile1, tile2 = move_string.split('-')
	
	return int(tile1), int(tile2), jump


class Player:
	def __init__(self, player_color):
		self.player_color = player_color

	def select_tile(self, tile_num, board):
		# converts the tile number input to an index on mainboard
		i, j = tile_num_to_index(tile_num)
		# validates the tile has a piece which belongs to the player
		if not board.Board[i][j].validate_tile(self.player_color):
			return
		print(board.Board[i][j])

	def move(self, move_string):
		# Parses move, returns selected tile and the next tile to move to
		current_tile, nxt_tile, jump = parse_move(move_string)
		# checks to
		#self.select_tile(current_tile, mainboard)
		print()
		i, j = tile_num_to_index(current_tile)
		i1, j1 = tile_num_to_index(nxt_tile)
		mainboard.Board[i1][j1].piece = mainboard.Board[i][j].piece
		mainboard.Board[i][j].piece = False
		print(mainboard)


class Board:
	def __init__(self):
		self.Board = None
		self._createBoard()

	def _createBoard(self):
		# setting up board
		# each Tile() holds tile information (color of tile, Piece() object), 
		# tile no. updated for green tiles
		# Piece() objects have color info: r/w and king info
		self.Board = [[Tile((i+(j%2))%2, Piece('w')) if (j < 3 and (i+(j%2))%2) or (j > 4 and (i+(j%2))%2) else Tile((i+(j%2))%2, False) for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

		Board = self.Board
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if Board[i][j].piece and i < 3:
					Board[i][j].piece = Piece('r')
				if Board[i][j].tile_color == 1:
					Board[i][j].number = int((BOARD_SIZE*(i) + j)/2) + 1

	def __repr__(self):
		string = ''
		for i in self.Board:
			string += str(i) + '\n'
		return string


class Tile:
	def __init__(self, tile_color, piece):
		self.tile_color = tile_color
		self.piece = piece
		self.number = None

	def __repr__(self):
		string = f"({str(self.number)}, {self.piece})"
		return string

	def __eq__(self, other):
		# used to compare tiles in can_move?
		return self.color == other.color and self.number == other.number

	def tile_is_empty(self):
		return Bool(self.piece)

	def validate_tile(self, player_color):
		# validates the tile contains a piece which belongs to the player
		#piece_available = self.piece
		piece_on_tile = bool(self.piece)
		if piece_on_tile:
			player_owns_piece = (self.piece.color == player_color)

		#movable = self.piece.can_move() or not self.piece
		#if piece_available and same_color and movable:
		#	return True
		#return False
		if self.number and piece_on_tile:
			return True
		return False




class Piece:
	def __init__(self, color):
		self.color = color
		self.king = False

	def __repr__(self):
		if self.king:
			return self.color + 'k'
		return self.color

	def can_move(self):
		if self.king:
			pass
		else:
			pass
		return True
	
	def find_piece(self):
		pass


mainboard = Board()
print(mainboard)

print()
 
player = Player('r')
#player.select_tile(5, mainboard) # does not print anything, piece doesn't belong to player color
#player.select_tile(32, mainboard) # prints the value at board index [2, 3] which contains a red piece at tile num 10

player.move('11-15')
