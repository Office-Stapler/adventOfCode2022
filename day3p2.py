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


def find_common(l1: list, l2: list, l3: list) -> str:
    s1 = set(l1)
    s2 = set(l2)
    s3 = set(l3)
    common = s1.intersection(s2).intersection(s3)
    return common.pop()


LOWER_CASE_PRIO = build_priority_dict(False)
UPPER_CASE_PRIO = build_priority_dict(True)

total_prio = 0

with open('day3input.txt', 'r+') as f:
    # remove newline from readlines
    items = [x[:-1] for x in f.readlines()]
    # split it into 3
    groups = [items[i:i + 3] for i in range(0, len(items), 3)]
    for group in groups:
        common = find_common(group[0], group[1], group[2])
        if common in LOWER_CASE_PRIO:
            total_prio += LOWER_CASE_PRIO[common]
        else:
            total_prio += UPPER_CASE_PRIO[common]

print(f'Total priority is {total_prio}')
