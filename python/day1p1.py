txtInput = ''
with open('../inputs/day1.txt', 'r+') as f:
    txtInput = f.read()

# split by the empty lines
elves = txtInput.split('\n\n')

maxCalories = {
    "calory": float('-inf'),
    "elfMax": 0
}

for idx, elf in enumerate(elves):
    calory = 0
    for calories in elf.split('\n'):
        calory += int(calories)
    if calory > maxCalories["calory"]:
        maxCalories['calory'] = calory
        maxCalories['elfMax'] = idx

print(
    f'Elf {maxCalories["elfMax"]} has the most calories with {maxCalories["calory"]} calories'
)
