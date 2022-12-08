#!/usr/bin/env python3

def part1(stacks, move_commands):
    for c in move_commands:
        count, from_crate, to_crate = c
        for i in range(int(count)):
            crate = stacks[from_crate].pop()
            stacks[to_crate].append(crate)

    top_crates = ""
    for c, s in stacks.items():
        top_crates += s[-1]

    print(top_crates)


def part2(stacks, move_commands):
    for c in move_commands:
        count, from_crate, to_crate = c
        count = int(count)
        stacks[to_crate].extend(stacks[from_crate][-count:])
        stacks[from_crate] = stacks[from_crate][:-count]

    top_crates = ""
    for c, s in stacks.items():
        top_crates += s[-1]

    print(top_crates)


if __name__ == "__main__":
    stack_info = [] # {crate label: stack}

    crate_labels = None
    move_commands = [] # (how many, from, to)
    with open("input.txt", 'r') as f:
        for line in f:
            if '[' in line:
                stack_info.append(line.replace("\n", "")) # save these lines to process when we know how many stacks there are
            else:
                line = line.strip()
                if line.strip() == "": continue # skip empty lines

                if crate_labels is None:
                    crate_labels = [l for l in line.split(" ") if l != ""]
                else:
                    count, from_crate, to_crate = [e for e in line.replace("move", "").replace("from", "").replace("to", "").split(" ") if e != ""]
                    move_commands.append((count, from_crate, to_crate))

    stacks = {label:[] for label in crate_labels}
    stack_info.reverse() # load state from bottom up
    for row in stack_info:
        crate_label_index = 0
        for i in range(0, len(row), 4):
            crate = row[i:i+4].replace("[", "").replace("]", "")
            crate_label = crate_labels[crate_label_index]
            if crate.strip() != "":
                stacks[crate_label].append(crate.strip())
            crate_label_index += 1

    # part1(stacks, move_commands)
    part2(stacks, move_commands)