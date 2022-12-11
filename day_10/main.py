#!/usr/bin/env python3

def part1(commands):
    cycle_num = 0
    x = 1

    signal_sum = 0

    while len(commands) > 0:
        operation, amount = commands.pop(0)
        cycle_num += 1
        signal_strength = cycle_num * x
        if (cycle_num == 20) or ((cycle_num - 20) % 40 == 0):
            signal_sum += signal_strength

        if operation == "addx":
            cycle_num += 1
            signal_strength = cycle_num * x
            if (cycle_num == 20) or ((cycle_num - 20) % 40 == 0):
                signal_sum += signal_strength

            x += amount

    return signal_sum

if __name__ == "__main__":
    commands = []
    with open("input.txt", 'r') as f:
        for line in f:
            elements = line.strip().split()
            if len(elements) == 1:
                commands.append((elements[0], None))
            else:
                commands.append((elements[0], int(elements[1])))

    print(f"Part 1: {part1(commands)}")