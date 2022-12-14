txt_input = ''
with open('day6input.txt', 'r+') as f:
    txt_input = f.read()
data_stream = txt_input
checked_index = 0

def is_marker(chars: str) -> bool:
    return len(set(chars)) == len(chars)

while checked_index < len(data_stream):
    processed_chars = data_stream[checked_index:checked_index + 14]
    if is_marker(processed_chars):
        print(data_stream[checked_index:checked_index + 14])
        print(f'Processed characters: {checked_index + 14}')
        break
    checked_index += 1
    