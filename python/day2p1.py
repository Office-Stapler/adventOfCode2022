from enum import Enum


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


OPPONENT_DICT = {
    'A': Hand.ROCK,
    'B': Hand.PAPER,
    'C': Hand.SCISSORS
}

USER_DICT = {
    'X': Hand.ROCK,
    'Y': Hand.PAPER,
    'Z': Hand.SCISSORS,
}

# what each hand beats
WIN_STATE_DICT = {
    Hand.ROCK: Hand.SCISSORS,
    Hand.PAPER: Hand.ROCK,
    Hand.SCISSORS: Hand.PAPER
}

POINTS_DICT = {
    Hand.ROCK: 1,
    Hand.PAPER: 2,
    Hand.SCISSORS: 3,
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}


def calculate_points(opponent: Hand, user: Hand) -> int:
    strategy_state = "LOSE"
    if opponent == user:
        strategy_state = "DRAW"
    if WIN_STATE_DICT[user] == opponent:
        strategy_state = "WIN"
    return POINTS_DICT[strategy_state] + POINTS_DICT[user]


txtInput = ''
with open('../inputs/day2.txt', 'r+') as f:
    txtInput = f.read()

total_points = 0


# split by the new line
strategies = txtInput.split('\n')
for strategy in strategies:
    opponent_encrypted, user_encrypted = strategy.split(' ')
    opponent, user = OPPONENT_DICT[opponent_encrypted], USER_DICT[user_encrypted]
    total_points += calculate_points(opponent, user)

print(f'Total points achieved by strategy is: {total_points}')
