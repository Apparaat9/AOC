game_input = open("input/day7_input.txt", "r").read().splitlines()

all_folders = []

class File:
  def __init__(self, size, name):
    self.size = size
    self.name = name

class Folder:
    def __init__(self, name, parent, depth):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = []
        self.folders = {}
        self.depth = depth

    def add_file(self, size, name):
        self.size += int(size)
        self.files.append(File(int(size), name))

    def add_folder(self, name):
        folder = Folder(name, self, self.depth + 1)
        all_folders.append(folder)
        self.folders[name] = folder


def check_sizes(folder, result):
    if folder.size < 100000:
        result += folder.size
    if folder.folders:
        for k,v in folder.folders.items():
            result = check_sizes(v, result)
    return result

def communicate_sizes():
    max_depth = max([f.depth for f in all_folders])
    for i in reversed(range(max_depth)):
        for f in all_folders:
            if f.depth == i + 1:
                f.parent.size += f.size

def build_files_system():
    folder = Folder("/", None, 0)
    c_folder = folder
    for input in game_input[1:]:
        commands = input.split(' ')
        if commands[0] == '$':
            if commands[1] == 'ls':
                continue
            elif commands[1] == 'cd':
                if commands[2] == '..':
                    c_folder = c_folder.parent
                else:
                    c_folder = c_folder.folders[commands[2]]
        elif commands[0] == "dir":
            c_folder.add_folder(commands[1])
        elif commands[0].isnumeric():
            c_folder.add_file(commands[0], commands[1])
    return folder

def find_folder(folder):
    best_solution = 70000000
    needed_size = 30000000
    size_used = folder.size
    needed_size = needed_size - (best_solution - size_used)
    for f in all_folders:
        if f.size > needed_size:
            if best_solution - needed_size > f.size - needed_size:
                best_solution = f.size
    return best_solution

folder = build_files_system()
communicate_sizes()

print(check_sizes(folder, 0))
print(find_folder(folder))
