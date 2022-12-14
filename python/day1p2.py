txtInput = ''
with open('../inputs/day1.txt', 'r+') as f:
    txtInput = f.read()

# split by the empty lines
elves = txtInput.split('\n\n')

# to store the max 3
maxCalories = [(float('-inf'), 0),
               (float('-inf'), 0),
               (float('-inf'), 0)]

for idx, elf in enumerate(elves):
    calory = 0
    for calories in elf.split('\n'):
        calory += int(calories)
    if calory > maxCalories[0][0]:
        maxCalories[2] = maxCalories[1]
        maxCalories[1] = maxCalories[0]
        maxCalories[0] = (calory, idx)
    elif calory > maxCalories[1][0]:
        maxCalories[2] = maxCalories[1]
        maxCalories[1] = (calory, idx)
    elif calory > maxCalories[2][0]:
        maxCalories[2] = (calory, idx)
    
    
print('The following elves have the most calories: ')
for maxCalory in maxCalories:
    print(f'Elf {maxCalory[1]} with {maxCalory[0]} calories')

print(f'With a total sum of {sum([x[0] for x in maxCalories])} calories')