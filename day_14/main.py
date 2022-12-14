#!/usr/bin/env python3

def part1(cavern):
    falling_endlessly = False
    sand_count = 0
    while not falling_endlessly:
        sand_x = 500
        sand_y = 0
        at_rest = False
        while not at_rest:
            # If moving down would put the sand off the map, it's going to fall forever
            if (sand_y + 1) >= len(cavern):
                falling_endlessly = True
                break
            # A unit of sand always falls down one step if possible.
            elif cavern[sand_y + 1][sand_x] == ".":
                sand_y += 1
            # If moving left would put the sand off the map, it's going to fall forever
            elif (sand_x - 1) < 0:
                falling_endlessly = True
                break
            # If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left.
            elif cavern[sand_y + 1][sand_x - 1] == ".":
                sand_y += 1
                sand_x -= 1
            # If moving right would put the sand off the map, it's going to fall forever
            elif (sand_x + 1) >= len(cavern[0]):
                falling_endlessly = True
                break
            # If down-left is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
            elif cavern[sand_y + 1][sand_x + 1] == ".":
                sand_y += 1
                sand_x += 1
            # not falling off the map, and can't move down, down-left, or down-right -- must be at rest
            else:
                at_rest = True
                sand_count += 1
                cavern[sand_y][sand_x] = "o"
                # print(f"Sand number {sand_count} has come to rest")
        
    return sand_count


def part2(cavern):
    # extend cavern height 2 rows
    cavern.append(['.' for col in range(len(cavern[0]))])
    cavern.append(['#' for col in range(len(cavern[0]))])

    last_resting_point = None
    resting_grains = 0
    while (last_resting_point != (500, 0)):
        sand_x = 500
        sand_y = 0
        at_rest = False
        while not at_rest:
            # A unit of sand always falls down one step if possible.
            if cavern[sand_y + 1][sand_x] == ".":
                sand_y += 1
                continue
            # Check if down-left exists, if not, create a new column of air, remember to add floor at the bottom
            if (sand_x - 1) < 0:
                for row in cavern:
                    row.insert(0, ".")
                cavern[-1][0] = "#"
            # If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left.
            if cavern[sand_y + 1][sand_x - 1] == ".":
                sand_y += 1
                sand_x -= 1
                continue
            # Check if down-right exists, if not, create a new column of air, remember to add floor at the bottom
            if (sand_x + 1) >= len(cavern[0]):
                for row in cavern:
                    row.append(".")
                cavern[-1][-1] = "#"
            # If down-left is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
            if cavern[sand_y + 1][sand_x + 1] == ".":
                sand_y += 1
                sand_x += 1
                continue
            # not falling off the map, and can't move down, down-left, or down-right -- must be at rest
            at_rest = True
            resting_grains += 1
            last_resting_point = (sand_x, sand_y)
            cavern[sand_y][sand_x] = "o"

    return resting_grains


if __name__ == "__main__":
    rock_paths = []
    with open("input.txt", 'r') as f:
        for line in f:
            path = []
            pairs = line.strip().split(" -> ")
            for p in pairs:
                x, y = [int(i) for i in p.split(",")]
                path.append((x, y))
            rock_paths.append(path)

    max_x = max([item[0] for path in rock_paths for item in path])
    max_y = max([item[1] for path in rock_paths for item in path])
    cavern = []
    for row in range(max_y + 1):
        cavern.append(['.' for col in range(max_x + 1)])

    cavern[0][500] = "+"

    for path in rock_paths:
        for i in range(1, len(path)):
            x1, y1 = path[i-1]
            x2, y2 = path[i]
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for x in range(x1, x2 + dx, dx):
                for y in range(y1, y2 + dy, dy):
                    cavern[y][x] = "#"

    print(f"Part 1: {part1([row[:] for row in cavern])}")
    print(f"Part 2: {part2([row[:] for row in cavern])}")