#!/usr/bin/env python3

def _blocked_vertically(tree_height, tree_grid, row, col_start, col_end):
    for test_col in range(col_start, col_end):
        if tree_grid[row][test_col] >= tree_height:
            # print(f" -- Blocked vertically by tree with height {tree_grid[row][test_col]} at ({row},{test_col})")
            return True
    return False


def _blocked_horizontally(tree_height, tree_grid, col, row_start, row_end):
    for test_row in range(row_start, row_end):
        if tree_grid[test_row][col] >= tree_height:
            # print(f" -- Blocked horizontally by tree with height ({tree_grid[test_row][col]}) at ({test_row},{col})")
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
                # print(f"Testing tree at ({row},{col}) with height {tree_height}")
                visible = (
                    not _blocked_vertically(tree_height, tree_grid, row, 0, col) or # check up
                    not _blocked_vertically(tree_height, tree_grid, row, col + 1, len(tree_grid[0])) or # check down
                    not _blocked_horizontally(tree_height, tree_grid, col, 0, row) or # check left
                    not _blocked_horizontally(tree_height, tree_grid, col, row + 1, len(tree_grid)) # check right
                )
                num_visible = num_visible + 1 if visible else num_visible

    return num_visible


if __name__ == "__main__":
    tree_grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            tree_grid.append([int(x) for x in line.strip()])

    # print(tree_grid)
    print(f"Part 1: {part1(tree_grid)}")