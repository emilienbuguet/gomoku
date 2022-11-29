"""Here are all the gomoku moves and their values"""

pattern_list = [
    {"pattern": "ooooo", "value": 1000, "symm": True},
    {"pattern": "_oooo_", "value": 95, "symm": True},
    {"pattern": "_oooo", "value": 50, "symm": False},
    {"pattern": "o_ooo", "value": 50, "symm": False},
    {"pattern": "oo_oo", "value": 50, "symm": True},
    {"pattern": "_ooo_", "value": 35, "symm": True},
    {"pattern": "_oo_o_", "value": 35, "symm": False},
    {"pattern": "ooo__", "value": 30, "symm": False},
    {"pattern": "oo_o_", "value": 30, "symm": False},
    {"pattern": "o_o_o", "value": 30, "symm": True},
    {"pattern": "_oo__", "value": 15, "symm": False},
    {"pattern": "oo___", "value": 15, "symm": False},
    {"pattern": "_o_o_", "value": 15, "symm": True},
    {"pattern": "o_o__", "value": 12, "symm": False},
    {"pattern": "ooo_", "value": 1, "symm": False},
    {"pattern": "oooo", "value": 1, "symm": True},
    {"pattern": "ooo", "value": 1, "symm": True},
    {"pattern": "oo", "value": 1, "symm": True},
]
