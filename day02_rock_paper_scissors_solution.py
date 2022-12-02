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
- 2. column = what you should play in response: 
    X = Rock, 
    Y = Paper, 
    Z = Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner has the highest score. 
- The score for a single round is the score for the shape you selected: 
    1 = Rock, 2 = Paper, 3 = Scissors
    plus 0 = you lost, 3 = draw, 6 = you won.

What would your total score be if everything goes exactly according to your strategy guide?
"""
import re

total_score = 0

def game_evaluation(opponents_move, my_move): 
    """Return who won. 
    Rock(A, X) defeats Scissors(C, Z), Scissors defeats Paper(B, Y), and Paper defeats Rock. 
    Draw if the same shape. 
    """
    print(f'Moves: {opponents_move}{my_move}')
    if opponents_move == 'A' and my_move == 'X': 
        return 'draw'
    elif opponents_move == 'B' and my_move == 'Y': 
        return 'draw'
    elif opponents_move == 'C' and my_move == 'Z': 
        return 'draw'
    elif opponents_move == 'A': 
        if my_move == 'Z': 
            return 'opponent_won'
        else: 
            return 'i_won'
    elif opponents_move == 'B': 
        if my_move == 'X': 
            return 'opponent_won'
        else: 
            return "i_won"
    elif opponents_move == 'C': 
        if my_move == 'X': 
            return 'i_won'
        else: 
            return 'opponent_won'
    

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
        my_move = re.findall('\s([XYZ])', line)
        opponents_move = opponents_move[0]
        my_move = my_move[0]
        winner = game_evaluation(opponents_move, my_move)
        print(f'The game state: {winner}')
        total_score += score(my_move, winner)
        print(f'Total score for new line: {total_score}\n')
    print(f'SCORE: {total_score}')
        


