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


def part2(commands):
    cycle_num = 0
    x = 1 # represents the middle of a 3 pixel-wide sprite

    pixels = []
    drawing_at = 0

    while len(commands) > 0:
        operation, amount = commands.pop(0)
        cycle_num += 1

        # draw pixel
        sprite_pixels = [x - 1, x, x + 1]
        if drawing_at in sprite_pixels:
            pixels.append("#")
        else:
            pixels.append(".")
        drawing_at += 1
        if drawing_at > 39:
            drawing_at = 0

        if operation == "addx":
            cycle_num += 1
            # draw pixel
            sprite_pixels = [x - 1, x, x + 1]
            if drawing_at in sprite_pixels:
                pixels.append("#")
            else:
                pixels.append(".")
            drawing_at += 1
            if drawing_at > 39:
                drawing_at = 0

            x += amount

    return pixels


if __name__ == "__main__":
    commands = []
    with open("input.txt", 'r') as f:
        for line in f:
            elements = line.strip().split()
            if len(elements) == 1:
                commands.append((elements[0], None))
            else:
                commands.append((elements[0], int(elements[1])))

    print(f"Part 1: {part1(commands[:])}")
    print(f"Part 2")
    pixels = part2(commands[:])
    for i in range(len(pixels)):
        print(pixels[i], end="")
        if (i + 1) % 40 == 0:
            print()