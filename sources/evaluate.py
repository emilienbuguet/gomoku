"""This is where the evaluation function of our algorithm is implemented"""

from .game import Board, ME, ENEMY
from .dictionary import pattern_list

def evaluate_line(line : str) -> int:
    score_total = 0
    for size in range(5):
        score_me = line.count(ME * size) ** 2 if ENEMY + ME * size + ENEMY not in line else 0
        score_enemy = line.count(ENEMY * size) ** 2 if ME + ENEMY * size + ME not in line else 0
        score_total += score_me - score_enemy
    return score_total

def evaluate(board: Board) -> int:
    total = 0
    for row in board:
        total += evaluate_line(row)

    for col in board.stones_cols:
        total += evaluate_line(col)

    for diag in board.left_diags:
        total += evaluate_line(diag)

    for diag in board.right_diags:
        total += evaluate_line(diag)

    return total
