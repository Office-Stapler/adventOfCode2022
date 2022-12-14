txtInput = ''
with open('../inputs/day4.txt', 'r+') as f:
    txtInput = f.read()
    
cleaned_sections = txtInput.split('\n')
num_enclosed = 0

for cleaned_section in cleaned_sections:
    elf_sections = cleaned_section.split(',')
    
    elf_1 = elf_sections[0].split('-')
    elf_2 = elf_sections[1].split('-')
    elf_1_nums = [int(elf_1[0]), int(elf_1[1])]
    elf_2_nums = [int(elf_2[0]), int(elf_2[1])]
    if elf_1_nums[0] <= elf_2_nums[0] and elf_1_nums[1] >= elf_2_nums[1]:
        num_enclosed += 1
    elif elf_2_nums[0] <= elf_1_nums[0] and elf_2_nums[1] >= elf_1_nums[1]:
        num_enclosed += 1

print(f'Num enclosed is: {num_enclosed}')