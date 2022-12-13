txtInput = ''


def build_priority_dict(is_capital: bool) -> dict:
    priority_dict = {}
    start_num = 1
    start_char = 'a'
    if is_capital:
        start_num = 27
        start_char = 'A'
    for i in range(26):
        priority_dict[chr(ord(start_char) + i)] = start_num + i
    return priority_dict


def find_common(l1: list, l2: list) -> str:
    print(l1)
    print(l2)
    s1 = set(l1)
    s2 = set(l2)
    common = s1.intersection(s2)
    return common.pop()


LOWER_CASE_PRIO = build_priority_dict(False)
UPPER_CASE_PRIO = build_priority_dict(True)

total_prio = 0

with open('day3input.txt', 'r+') as f:
    items = f.readlines()
    for item in items:
        middle = len(item) // 2
        common = find_common(item[:middle], item[middle:])
        if common in LOWER_CASE_PRIO:
            total_prio += LOWER_CASE_PRIO[common]
        else:
            total_prio += UPPER_CASE_PRIO[common]

print(f'Total priority is {total_prio}')
