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
def find_smaller_dirs(tree: Tree, size_threshold: int, dirs: list[Tree]):
    if tree is None or tree.children is None:
        return
    size = tree.get_size()
    if size <= size_threshold:
        dirs.append(size)
    for child in tree.children:
        find_smaller_dirs(child, size_threshold, dirs)
    
root = Tree(0, '/', True)
root.parent = root
curr_tree = None

txtInput = ''
with open('day7input.txt', 'r+') as f:
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
print(f'Total file sizes: {root.get_size()}')
dirs = []
find_smaller_dirs(root, 100000, dirs)
print(f'Sum of all directories under 100000 is: {sum(dirs)}')