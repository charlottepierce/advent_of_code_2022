#!/usr/bin/env python3

if __name__ == "__main__":
    calories_per_elf = []
    with open("input.txt", 'r') as f:
        calorie_count = 0
        for line in f:
            if line.strip() == "":
                calories_per_elf.append(calorie_count)
                calorie_count = 0
            else:
                calorie_count += int(line.strip())
        calories_per_elf.append(calorie_count)

    # part 1: max calories held by one elf
    print("Part 1:", max(calories_per_elf))

    # part 2: sum of the top 3
    calories_per_elf.sort()
    print("Part 2:", sum(calories_per_elf[-3:]))