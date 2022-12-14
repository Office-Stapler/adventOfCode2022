txtInput = ''
with open('../inputs/day5.txt', 'r+') as f:
    txtInput = f.read()

MOVE = 0
FROM = 1
TO = 2

# split by the empty lines
initialState, moves = txtInput.split('\n\n')
cargo = {}
initialState = initialState.split('\n')
for num in initialState[-1].split(' '):
    if num == '':
        continue
    cargo[num] = []
for state in initialState[:-1]:
    index = 0
    while index < len(state):
        if state[index] == '[':
            cargo[str((index // 4) + 1)].insert(0, state[index + 1])
        index += 4
moves = moves.replace('move ', '')
moves = moves.replace(' from', '')
moves = moves.replace(' to', '')

for move in moves.split('\n'):
    move_instructions = move.split(' ')
    move_instruction, move_from, move_to = (
        move_instructions[MOVE], move_instructions[FROM], move_instructions[TO]
    )
    cargo[move_to].extend(cargo[move_from][-int(move_instruction):])
    del cargo[move_from][-int(move_instruction):]

for i in range(1, 10):
    print(cargo[str(i)][-1], end='')
print()