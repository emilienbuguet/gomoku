"""Here are all the gomoku moves and their values

In a pattern: _ is empty, o is ally, x is enemy.
"""

pattern_list = [
    {"pattern": "ooooo", "value": 1000, "symm": True},
    {"pattern": "xxoxx", "value": 900, "symm": True},
    {"pattern": "oxxxx", "value": 900, "symm": False},
    {"pattern": "xoxxx", "value": 900, "symm": False},
    {"pattern": "oxxx__", "value": 600, "symm": False},
    {"pattern": "oxxx_", "value": 500, "symm": False},
    {"pattern": "_oooo_", "value": 450, "symm": True},
    {"pattern": "_oooo", "value": 200, "symm": False},
    {"pattern": "o_ooo", "value": 200, "symm": False},
    {"pattern": "oo_oo", "value": 200, "symm": True},
    {"pattern": "xxxo_", "value": 150, "symm": False},
    {"pattern": "xxx_o", "value": 150, "symm": False},
    {"pattern": "xxo__", "value": 100, "symm": False},
    {"pattern": "xx_o_", "value": 100, "symm": False},
    {"pattern": "xx__o", "value": 80, "symm": False},
    {"pattern": "_ooo_", "value": 35, "symm": True},
    {"pattern": "_oo_o_", "value": 35, "symm": False},
    {"pattern": "ooo__", "value": 30, "symm": False},
    {"pattern": "oo_o_", "value": 30, "symm": False},
    {"pattern": "o_o_o", "value": 30, "symm": True},
    {"pattern": "_oo__", "value": 15, "symm": False},
    {"pattern": "oo___", "value": 15, "symm": False},
    {"pattern": "_o_o_", "value": 15, "symm": True},
    {"pattern": "o_o__", "value": 12, "symm": False},
]
