#!/usr/bin/env python3

class Directory(object):
    def __init__(self, name, indentation_level, parent=None):
        self.name = name
        self.indentation_level = indentation_level
        self.subdirs = []
        self.files = [] # (name, size)
        self.parent = parent

    def find_subdir(self, name):
        for dir in self.subdirs:
            if dir.name == name:
                return dir

    def size(self):
        size = sum([d.size() for d in self.subdirs])
        size += sum([int(f[1]) for f in self.files])
        return size

    def __str__(self):
        indentation = "  " * self.indentation_level
        result = f"{indentation}{self.name} (dir, size={self.size()})\n"
        for dir in self.subdirs:
            result += str(dir)
        for f in self.files:
            result += f"{indentation}  {f[0]} (file, size={f[1]})\n"
        return result


if __name__ == "__main__":
    buffer = ""
    root_dir = Directory("/", 0)
    curr_dir = root_dir

    with open("input.txt", 'r') as f:
        for line in f:
            if line.strip() == "$ cd /":
                curr_dir = root_dir
            elif line.strip()[0] == "$":
                # process command
                elements = line.strip().split(" ")
                if elements[1] == "cd":
                    if elements[2] == "..":
                        curr_dir = curr_dir.parent
                    else:
                        curr_dir = curr_dir.find_subdir(elements[2])
            else:
                # line must be ls output
                specifier, name = line.strip().split(" ")
                if specifier == "dir":
                    curr_dir.subdirs.append(Directory(name, curr_dir.indentation_level + 1, parent=curr_dir))
                else:
                    curr_dir.files.append((name, int(specifier)))

    dir_sizes = {}
    to_check = [root_dir]
    while len(to_check) > 0:
        check = to_check.pop(0)

        if isinstance(check, Directory):
            dir_sizes[check] = check.size()
            for d in check.subdirs:
                to_check.append(d)

    print(root_dir)

    # part 1
    print(f"Part 1: {sum([size for d, size in dir_sizes.items() if size <= 100000])}")

    # part 2
    space_needed = 30000000 - (70000000 - root_dir.size())    
    print(f"Part 2: {min({d:size for d, size in dir_sizes.items() if size >= space_needed}, key=lambda d: dir_sizes[d]).size()}")