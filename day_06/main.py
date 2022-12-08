#!/usr/bin/env python3

def part1(buffer):
    for i in range(0, len(buffer) - 3):
        substr = buffer[i:i+4]
        if len(substr) < 4:
            continue
        if len(set(substr)) == 4:
            return i + 4


if __name__ == "__main__":
    buffer = ""
    with open("input.txt", 'r') as f:
        for line in f:
            buffer += line.strip()

    print(part1(buffer))
    