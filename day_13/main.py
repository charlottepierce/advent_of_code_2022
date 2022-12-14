#!/usr/bin/env python3
import ast

def compare(left, right):
    print(f" - Compare {left} vs {right}")
    # If both values are integers, the lower integer should come first.
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("    - both ints, left is lower -- they are in order")
            return True # If the left integer is lower than the right integer, the inputs are in the right order
        elif left > right:
            print("    - both ints, left is higher -- they are NOT in order")
            return False # If the left integer is higher than the right integer, the inputs are not in the right order.
        else:
            print("    - both ints, both the same -- move on")
            return None

    # Otherwise, the inputs are the same integer; continue checking the next part of the input.
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            # If the right list runs out of items first, the inputs are not in the right order.
            if i >= len(right):
                print("    - both lists, right ran out of items first -- they are NOT in order")
                return False

            # If both values are lists, compare the first value of each list, then the second value, and so on.
            result = compare(left[i], right[i])
            if result == False:
                print(f"    - both lists, comparing items {left[i]} and {right[i]} failed -- they are NOT in order")
                return False
            elif result == True:
                return True
            

        # If the left list runs out of items first, the inputs are in the right order
        if len(left) < len(right):
            print("    - both lists, left ran out of items first -- they are in order")
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
        print(f"Pair {i + 1}")
        left, right = pairs[i]
        if compare(left, right):
            print("YEP")
            sum += i + 1
        else:
            print("NOPE")

    return sum


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