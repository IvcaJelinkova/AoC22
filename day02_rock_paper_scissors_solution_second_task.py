# task: 
""" 
Play Rock Paper Scissors according to a strategy in "day02_input.txt". 
Game is for 2 players. 
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. Draw if the same shape. 
STRATEGY: 
- 1. column = what your opponent is going to play: 
    A = Rock, 
    B = Paper, 
    C = Scissors.
- 2. column = how the round needs to end: 
    X = opponent won, 
    Y = a draw, 
    Z = i won. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner has the highest score. 
- The score for a single round is the score for the shape you selected: 
    1 = Rock, 2 = Paper, 3 = Scissors
    plus 0 = you lost, 3 = draw, 6 = you won.

What would your total score be if everything goes exactly according to your strategy guide?
"""
import re

total_score = 0

def transfer_game_result(game_result): 
    """Returns game_result transfer to text. Input game_result is X, Y or Z. 
    X = opponent won, 
    Y = a draw, 
    Z = i won.
    """
    if game_result == 'X': 
        game_result = 'opponent_won'
    elif game_result == 'Y': 
        game_result = 'draw'
    else: 
        game_result = 'i_won'
    return game_result


def what_is_my_move(opponents_move, game_result): 
    """Return what is my move. 
    Rock(A, X) defeats Scissors(C, Z), Scissors defeats Paper(B, Y), and Paper defeats Rock. 
    Draw if the same shape. 
    X = opponent won, 
    Y = a draw, 
    Z = i won.
    If I know the game_result, it returns my move --> 
        X = rock
        Y = paper
        Z = scissors. 
    """
    print(f'Move and game result: {opponents_move}, {game_result}', end='\t')

    if opponents_move == 'A' and game_result == 'draw': 
        return 'X'
    elif opponents_move == 'B' and game_result == 'draw': 
        return 'Y'
    elif opponents_move == 'C' and game_result == 'draw': 
        return 'Z'
    elif opponents_move == 'A': 
        if game_result == 'opponent_won': 
            return 'Z'
        else: 
            return 'Y'
    elif opponents_move == 'B': 
        if game_result == 'i_won': 
            return 'Z'
        else: 
            return "X"
    elif opponents_move == 'C': 
        if game_result == 'i_won': 
            return 'X'
        else: 
            return 'Y'
    

def score(my_move, winner): 
    """Returns the actual score according to winner and your shape. 
    0 = you lost, 3 = draw, 6 = you won
    1 = Rock, 2 = Paper, 3 = Scissors
    """
    #print(f'My move and winner: {my_move}{winner}')
    if winner == 'opponent_won': 
        winner_score = 0
    elif winner == 'i_won': 
        winner_score = 6
    elif winner == 'draw': 
        winner_score = 3

    if my_move == 'X': 
        move_score = 1
    elif my_move == 'Y': 
        move_score = 2
    elif my_move == 'Z': 
        move_score = 3
    print(f'Winner score: {winner_score}, Move score: {move_score}')
    return winner_score + move_score


with open('day02_input.txt') as file: 
    for line in file: 
        opponents_move = re.findall('^[ABC]', line)
        game_result = re.findall('\s([XYZ])', line)
        opponents_move = opponents_move[0]
        game_result = game_result[0]
        game_result = transfer_game_result(game_result)
        my_move = what_is_my_move(opponents_move, game_result)
        print(f'My move: {my_move}')
        total_score += score(my_move, game_result)
        print(f'Total score for new line: {total_score}\n')
    print(f'SCORE: {total_score}')
        


