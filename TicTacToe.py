

def game_init():
	board = [[0,0,0],[0,0,0],[0,0,0]]

	player = 0
	turns = 0
	win = False
	print_board(board)
	while not win:
		player = change_player(player)
		make_a_move(board, player)
		print_board(board)
		if turns > 3:
			win = has_won(board)
			continue
		turns += 1
	print(f"Player {player} has won! Congratulations")

def print_board(board):
	print("\n")
	for x in range(0, 3):
		for y in range(0,3):
			if board[x][y] == 1:
				print("| X ", end="")
			elif board[x][y] == 2:
				print("| O ", end="")
			else:
				print("|  ", end=" ")
		print("|\n")


def change_player(player):
	if player == 1:
		return 2
	else:
		return 1

def make_a_move(board, player):
	print("Row: ", end="")
	x = get_play() -1
	print("Column: ", end="")
	y = get_play() -1
	if valid_play(board,x,y):
		board[x][y] = player
	else:
		print("Invalid position, position already taken")
		make_a_move(board, player)

def get_play():
	player_input = int(input())
	if 1 > player_input or player_input > 3:
		print("Invalid play, must choose a number between 1 and 3")
		get_play()
	return player_input

def valid_play(board, x, y):
	if board[x][y] != 0:
		return False
	return True


def has_won(board):
	if won_vertically(board) or won_horizontally(board) or won_diagonally(board):
		return True
	else:
		return False


def won_horizontally(board):
	for x in range(0,3):
		for y in range(0,3):
			if board[x][y] == 0:
				return False
		if board[x][0] == board[x][1] == board[x][2]:
			return True
	return false


def won_vertically(board):
	for x in range(0,3):
		for y in range(0,3):
			if board[x][y] == 0:
				return False
			if board[0][y] ==board[1][y] ==board[2][y] :
				return True
	return False

def won_diagonally(board):
	if board[0][0] == board[1][1] == board[2][2] != 0:
		return True
	if board[2][0] == board[1][1] == board[0][2] != 0:
		return True

if __name__ == "__main__":
	game_init()
