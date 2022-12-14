from enum import Enum


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    WIN = 4,
    LOSE = 5,
    DRAW = 6,


OPPONENT_DICT = {
    'A': Hand.ROCK,
    'B': Hand.PAPER,
    'C': Hand.SCISSORS
}

# what the game has to end in
END_DICT = {
    'X': Hand.LOSE,
    'Y': Hand.DRAW,
    'Z': Hand.WIN,
}

# what each hand beats
WIN_STATE_DICT = {
    Hand.ROCK: Hand.SCISSORS,
    Hand.PAPER: Hand.ROCK,
    Hand.SCISSORS: Hand.PAPER
}

# what each hand loses to
LOSE_STATE_DICT = {
    Hand.ROCK: Hand.PAPER,
    Hand.PAPER: Hand.SCISSORS,
    Hand.SCISSORS: Hand.ROCK
}

# what state to check
STATE_DICT = {
    Hand.WIN: LOSE_STATE_DICT,
    Hand.LOSE: WIN_STATE_DICT,
}


POINTS_DICT = {
    Hand.ROCK: 1,
    Hand.PAPER: 2,
    Hand.SCISSORS: 3,
    Hand.WIN: 6,
    Hand.DRAW: 3,
    Hand.LOSE: 0
}


def calculate_points(opponent: Hand, end: Hand) -> int:
    if end == Hand.DRAW:
        return POINTS_DICT[Hand.DRAW] + POINTS_DICT[opponent]
    state_dict = STATE_DICT[end]
    return POINTS_DICT[end] + POINTS_DICT[state_dict[opponent]]


txtInput = ''
with open('../inputs/day2.txt', 'r+') as f:
    txtInput = f.read()

total_points = 0


# split by the new line
strategies = txtInput.split('\n')
for strategy in strategies:
    opponent_encrypted, user_encrypted = strategy.split(' ')
    opponent, user = OPPONENT_DICT[opponent_encrypted], END_DICT[user_encrypted]
    total_points += calculate_points(opponent, user)

print(f'Total points achieved by strategy is: {total_points}')
