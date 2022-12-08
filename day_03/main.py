#!/usr/bin/env python3

if __name__ == "__main__":
    rucksacks = []
    with open("input.txt", 'r') as f:
        for line in f:
            line = line.strip()
            midpoint = int(len(line) / 2)
            rucksacks.append((line[:midpoint], line[midpoint:]))

    # part 1
    lowercase_priority_offset_from_ordinal = 96
    uppercase_priority_offset_from_ordinal = 38

    priority_sum = 0
    for r in rucksacks:
        for overlapping_item in set(r[0]).intersection(r[1]):
            offset = lowercase_priority_offset_from_ordinal if overlapping_item.islower() else uppercase_priority_offset_from_ordinal

            priority_sum += ord(overlapping_item) - offset

    print("Part 1:", priority_sum)