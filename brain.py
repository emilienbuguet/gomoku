"""This is where the brain algorithm is implemented"""
from game import Game, Players, Board
from win import win_coordinates, has_won
from random import randint, choice
from copy import deepcopy


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def run_one_random_game(board: Board):
    player = Players['ENNEMY']
    while not has_won(board, Players['ENNEMY']) and not has_won(board, Players['ME']):
        x, y = win_coordinates(board, player)
        if x == -1:
            x, y = win_coordinates(board, Players['ME'] if player == Players['ENNEMY'] else Players['ENNEMY'])
        if x < 0 and y < 0:
            possible_hits: list = list(filter(lambda c: c is not None, list([
                (i, n) if board[n][i] == 0 else None for i in range(board.length) for n in
                range(board.height)
            ])))
            if not possible_hits:
                break
            x, y = choice(possible_hits)
        board.add_stone(player.value, x, y)
        player = Players['ME'] if player == Players['ENNEMY'] else Players['ENNEMY']


def run_random_games(nb_games: int, board: Board) -> int: # todo opti with number of looses
    victories = 0

    for i in range(nb_games):
        copied_board = deepcopy(board)
        run_one_random_game(copied_board)
        if has_won(copied_board, Players['ME']):
            victories += 1

    return victories


def monte_carlo(game: Game) -> (int, int):
    possible_hits: iter = filter(lambda c: c is not None, list([
        (x, y) if game.board[y][x] == 0 else None for x in range(game.board.length) for y in range(game.board.height)
    ]))
    winner = {
        'x': -1,
        'y': -1,
        'score': -1
    }
    for (x, y) in possible_hits:
        board = deepcopy(game.board)
        board.add_stone(Players['ME'], x, y)
        victories = run_random_games(50, board)
        if victories > winner['score']:
            winner = {'x': x, 'y': y, 'score': victories}

    return winner['x'], winner['y']


def evaluate(game: Game) -> (int, int):
    x, y = win_coordinates(game.board, Players['ME'])
    if x == -1:
        x, y = win_coordinates(game.board, Players['ENNEMY'])
    while x < 0 and y < 0 or game.board.stones[y][x] != 0:
        x, y = monte_carlo(game)
        print("Monte Carlo gave %d, %d" % (x, y))
    return x, y
