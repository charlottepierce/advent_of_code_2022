#!/usr/bin/env python3

def find_pos_of_char_in_grid(elevation_grid, character):
    for row in range(len(elevation_grid)):
        for col in range(len(elevation_grid[0])):
            if elevation_grid[row][col] == character:
                return (row, col)


def get_neighbours(pos, elevation_grid):
    row = pos[0]
    col = pos[1]
    max_row = len(elevation_grid) - 1
    max_col = len(elevation_grid[0]) - 1

    neighbours = []
    
    if (row - 1) >= 0:
        neighbours.append((row - 1, col)) # up
    if (row + 1) <= max_row:
        neighbours.append((row + 1, col)) # down
    if (col - 1) >= 0:
        neighbours.append((row, col - 1)) # left
    if (col + 1) <= max_col:
        neighbours.append((row, col + 1)) # right

    return neighbours


def part1(elevation_grid):
    start = find_pos_of_char_in_grid(elevation_grid, "S")
    end = find_pos_of_char_in_grid(elevation_grid, "E")

    queue = [(start, 0)]
    visited = []
    visited.append(start)

    best = None

    while len(queue) > 0:
        curr, score = queue.pop(0)

        if curr == end:
            if (best == None) or (score < best):
                best = score

        for neighbour in get_neighbours(curr, elevation_grid):
            height_at_curr = elevation_grid[curr[0]][curr[1]]
            height_at_neighbour = elevation_grid[neighbour[0]][neighbour[1]]
            if height_at_curr == "S": height_at_curr = "a"
            if height_at_neighbour == "E": height_at_neighbour = "z"
            if (ord(height_at_curr) + 1 >= ord(height_at_neighbour)) and (neighbour not in visited):
                queue.append((neighbour, score + 1))
                visited.append(neighbour)

    return best


if __name__ == "__main__":
    elevation_grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            elevation_grid.append([c for c in line.strip()])

    print(f"Part 1: {part1(elevation_grid)}")