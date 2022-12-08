#!/usr/bin/env python3

def find_marker(buffer, num_unique_chars):
    for i in range(0, len(buffer) - (num_unique_chars - 1)):
        substr = buffer[i:i+num_unique_chars]
        if len(substr) < num_unique_chars:
            continue
        if len(set(substr)) == num_unique_chars:
            return i + num_unique_chars


if __name__ == "__main__":
    buffer = ""
    with open("input.txt", 'r') as f:
        for line in f:
            buffer += line.strip()

    print(f"Part 1: {find_marker(buffer, 4)}")
    print(f"Part 2: {find_marker(buffer, 14)}")
    