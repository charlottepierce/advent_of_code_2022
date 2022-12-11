#!/usr/bin/env python3

def _blocked_vertically(tree_height, tree_grid, row, col_start, col_end):
    for test_col in range(col_start, col_end):
        if tree_grid[row][test_col] >= tree_height:
            return True
    return False


def _blocked_horizontally(tree_height, tree_grid, col, row_start, row_end):
    for test_row in range(row_start, row_end):
        if tree_grid[test_row][col] >= tree_height:
            return True
    return False


def part1(tree_grid):
    num_visible = 0
    for row in range(len(tree_grid)):
        for col in range(len(tree_grid[0])):
            if (row == 0) or (row == (len(tree_grid) - 1)) or (col == 0) or (col == (len(tree_grid[0]) - 1)):
                num_visible += 1 # tree is on the outside, always going to be visible
            else:
                tree_height = tree_grid[row][col]
                visible = (
                    not _blocked_vertically(tree_height, tree_grid, row, 0, col) or # check up
                    not _blocked_vertically(tree_height, tree_grid, row, col + 1, len(tree_grid[0])) or # check down
                    not _blocked_horizontally(tree_height, tree_grid, col, 0, row) or # check left
                    not _blocked_horizontally(tree_height, tree_grid, col, row + 1, len(tree_grid)) # check right
                )
                num_visible = num_visible + 1 if visible else num_visible

    return num_visible


def _viewing_distance(tree_grid, row, col, row_start, row_end, col_start, col_end, hstep=1, vstep=1):
    tree_height = tree_grid[row][col]
    distance = 0
    for test_row in range(row_start, row_end, hstep):
        for test_col in range(col_start, col_end, vstep):
            if tree_grid[test_row][test_col] >= tree_height:
                distance += 1
                return distance
            distance += 1
    return distance


def part2(tree_grid):
    highest_scenic_score = 0
    for row in range(len(tree_grid)):
        for col in range(len(tree_grid[0])):
            scenic_score = 1
            scenic_score *= _viewing_distance(tree_grid, row, col, row, row+1, col - 1, -1, vstep=-1) # up
            scenic_score *= _viewing_distance(tree_grid, row, col, row, row+1, col + 1, len(tree_grid[0])) # down
            scenic_score *= _viewing_distance(tree_grid, row, col, row - 1, -1, col, col + 1, hstep=-1) # left
            scenic_score *= _viewing_distance(tree_grid, row, col, row + 1, len(tree_grid), col, col + 1) # right
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score    


if __name__ == "__main__":
    tree_grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            tree_grid.append([int(x) for x in line.strip()])

    print(f"Part 1: {part1(tree_grid)}")
    print(f"Part 2: {part2(tree_grid)}")