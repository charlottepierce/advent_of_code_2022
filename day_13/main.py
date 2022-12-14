#!/usr/bin/env python3
import ast

def compare(left, right):
    # If both values are integers, the lower integer should come first.
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True # If the left integer is lower than the right integer, the inputs are in the right order
        elif left > right:
            return False # If the left integer is higher than the right integer, the inputs are not in the right order.
        else:
            return None

    # Otherwise, the inputs are the same integer; continue checking the next part of the input.
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            # If the right list runs out of items first, the inputs are not in the right order.
            if i >= len(right):
                return False

            # If both values are lists, compare the first value of each list, then the second value, and so on.
            result = compare(left[i], right[i])
            if result == False:
                return False
            elif result == True:
                return True
            

        # If the left list runs out of items first, the inputs are in the right order
        if len(left) < len(right):
            return True

    # If the lists are the same length and no comparison makes a decision about the order (or both are not lists), continue checking the next part of the input.
    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
    if isinstance(left, int) and not isinstance(right, int):
        return compare([left], right)
    elif not isinstance(left, int) and isinstance(right, int):
        return compare(left, [right])


def part1(pairs):
    sum = 0
    for i in range(len(pairs)):
        left, right = pairs[i]
        if compare(left, right):
            sum += i + 1

    return sum


def part2(pairs):
    packets = [i for pair in pairs for i in pair]
    packets.append([[2]])
    packets.append([[6]])

    # run bubble sort
    n = len(packets)
    while True: # dammit python, no repeat until loop
        swapped = False

        for i in range(1, n):
            if not compare(packets[i - 1], packets[i]):
                packets[i - 1], packets[i] = packets[i], packets[i - 1]
                swapped = True

        if not swapped:
            break
    
    # find indices of decoder packets and multiply for answer
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    

if __name__ == "__main__":
    lines = []
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    pairs = []
    while len(lines) > 0:
        item1 = ast.literal_eval(lines.pop(0).strip())
        item2 = ast.literal_eval(lines.pop(0).strip())
        if len(lines) > 0: lines.pop(0)
        pairs.append((item1, item2))

    print(f"Part 1: {part1(pairs)}")
    print(f"Part 2: {part2(pairs)}")