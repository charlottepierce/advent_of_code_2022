#!/usr/bin/env python3

lowercase_priority_offset_from_ordinal = 96
uppercase_priority_offset_from_ordinal = 38


def _priority_of_char(char):
    offset = lowercase_priority_offset_from_ordinal if char.islower() else uppercase_priority_offset_from_ordinal
    return ord(char) - offset


if __name__ == "__main__":
    rucksacks = []
    with open("input.txt", 'r') as f:
        for line in f:
            rucksacks.append(line.strip())



    # part 1
    priority_sum = 0
    for r in rucksacks:
        midpoint = int(len(r) / 2)
        compartment_1, compartment_2 = r[:midpoint], r[midpoint:]
        for overlapping_item in set(compartment_1).intersection(compartment_2):
            priority_sum += _priority_of_char(overlapping_item)

    print("Part 1:", priority_sum)

    # part 2
    priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        bag1, bag2, bag3 = rucksacks[i:i+3]
        badge = list(set(bag1).intersection(bag2).intersection(bag3))[0]
        priority_sum += _priority_of_char(badge)

    print("Part 2:", priority_sum)