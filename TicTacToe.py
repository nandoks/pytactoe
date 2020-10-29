
"""starts a game defining a board of a 3x3 array filled with 0

"""
def init_partida():
	grelha = [[0,0,0],[0,0,0],[0,0,0]]
	jogador = 1
	rodada = 1
	while ganhar_partida(grelha, jogador, rodada) is False:
		imprime_grelha(grelha)
		jogar(grelha, jogador, rodada)
		rodada += 1
		if jogador == 1:
			jogador = 2
		else:
			jogador = 1
	if jogar_outra():
		init_partida()
	else:
		print("Volte sempre!")

# prints the board on the screen
def imprime_grelha(grelha):
	for x in range(0,3):
		for y in range(0,3):
			print(grelha[x][y],end='')
		print(' ')

# makes a play on the board
def jogar(grelha, jogador, rodada):
	pos_x = int(input("Escolha a linha: ")) -1
	pos_y = int(input("Escolha a coluna: ")) -1
	if 0 <= pos_x <= 2 and 0 <= pos_y <=2:
		jogada(grelha, jogador, pos_x, pos_y, rodada)
	else:
		print("Posição inválida")
		jogar(grelha,jogador, rodada)

# tries a move, make the move if the position is empty, else returns en error and calls itself again
def jogada(grelha, jogador, pos_x, pos_y, rodada):
	if grelha[pos_x][pos_y] == 0:
		grelha[pos_x][pos_y] = jogador
	else:
		print("Jogada já feita,escolha outra posição")
		jogar(grelha, jogador, rodada)

""" 
this function call the other functions to see if
the player won after a move
"""
def ganhar_partida(grelha, jogador,rodada):
	if ganhou_vertical(grelha, jogador):
		return True
	elif ganhou_horizontal(grelha,jogador):
		return True
	elif ganhou_diagonal(grelha,jogador):
		return True
	elif rodada > 9:
		print("Ninguem ganhou!")
		return True
	else:
		return False

# checks if the player won vertically
def ganhou_vertical(grelha, jogador):
	for x in range(0,3):
		for y in range(0,3):
			if grelha[x][y] != 0:
				if grelha[x][0] == grelha[x][1] == grelha[x][2]:
					print("Jogador {} ganhou!\n".format(jogador))
					return True
	return False

# checks if the player won horizontally
def ganhou_horizontal(grelha, jogador):
	for x in range(0,3):
		for y in range(0,3):
			if grelha[x][y] != 0:
				if grelha[0][y] == grelha[1][y] == grelha[2][y]:
					print("Jogador {} ganhou!\n".format(jogador))
					return True
	return False

# checks if the player won diagonaly
def ganhou_diagonal(grelha, jogador):
	pass

# asks if you want to play another game and return the answer as True or False
def jogar_outra():
	outra = input("Deseja jogar outra partida? s / n\n")
	if outra == "s":
		return True
	elif outra == "n":
		return False

init_partida()
