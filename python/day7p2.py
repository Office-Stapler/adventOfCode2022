from __future__ import annotations
class Tree:
    def __init__(self, size: int or None, name: str, is_dir: bool) -> None:
        self.children: list[Tree] or None = [] if is_dir else None
        self.parent = None
        self.size = size
        self.name = name

    def get_size(self):
        self.update_size()
        return self.size

    def update_size(self):
        if self.children is not None:
            self.size = 0
            for child in self.children:
                self.size += child.get_size()
    
    def cd(self, name: str):
        if self.children is not None:
            for child in self.children:
                if child.name == name and child.children is not None:
                    return child
        return None
    
    def add(self, node: Tree):
        if self.children is not None:
            self.children.append(node)
            self.update_size()
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
MAX_USED_SPACE = TOTAL_SPACE - REQUIRED_SPACE

def find_smallest_directory_to_delete(
    tree: Tree, prev_threshold: int, used_space: int
) -> int:
    if tree is None or tree.children is None:
        return prev_threshold
    size = tree.get_size()
    new_prev_threshold = prev_threshold
    if used_space - size < MAX_USED_SPACE:
        if size < prev_threshold:
            new_prev_threshold = size
    for child in tree.children:
        child_size = find_smallest_directory_to_delete(child, new_prev_threshold, used_space)
        if child_size < new_prev_threshold:
            new_prev_threshold = child_size
    return new_prev_threshold

root = Tree(0, '/', True)
root.parent = root
curr_tree = None

txtInput = ''
with open('../inputs/day7.txt', 'r+') as f:
    txtInput = f.read()

commands = txtInput.split('\n')
for command in commands:
    if command.startswith('$'):
        if command[2:].startswith('ls'):
            continue
        dir = command[5:]
        if dir == '..':
            curr_tree = curr_tree.parent
        elif dir == '/':
            curr_tree = root
        else:
            curr_tree = curr_tree.cd(dir)
    elif command.startswith('dir'):
        tree = Tree(0, command[4:], True)
        tree.parent = curr_tree
        curr_tree.add(tree)
    else:
        size, name = command.split(' ')
        tree = Tree(int(size), name, False)
        tree.parent = curr_tree
        curr_tree.add(tree)

USED_SPACE = root.get_size()
print(f'Smallest directory to delete that gives the required size: ')
print(find_smallest_directory_to_delete(root, USED_SPACE, USED_SPACE))