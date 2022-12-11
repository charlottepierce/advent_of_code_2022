#!/usr/bin/env python3

def _resolve_tail(head_pos, tail_pos, last_move_dir):
    chebyshev_distance = max(abs(head_pos[1] - tail_pos[1]), abs(head_pos[0] - tail_pos[0]))
    if chebyshev_distance <= 1:
        return tail_pos # close enough, don't need to move the tail
        
    # move the tail based on the direction the head last moved
    match last_move_dir:
        case "U":
            return [head_pos[0], head_pos[1] - 1]
        case "D":
            return [head_pos[0], head_pos[1] + 1]
        case "L":
            return [head_pos[0] + 1, head_pos[1]]
        case "R":
            return [head_pos[0] - 1, head_pos[1]]


def part1(commands):
    head_pos = [0, 0]
    tail_pos = [0, 0]

    unique_tail_positions = set()
    unique_tail_positions.add(tuple(tail_pos))

    for direction, amount in commands:
        for x in range(amount):
            match direction:
                case "U":
                    head_pos[1] += 1
                case "D":
                    head_pos[1] -= 1
                case "L":
                    head_pos[0] -= 1
                case "R":
                    head_pos[0] += 1
            tail_pos = _resolve_tail(head_pos, tail_pos, direction)
            unique_tail_positions.add(tuple(tail_pos))
    
    return len(unique_tail_positions)


if __name__ == "__main__":
    commands = []
    with open("input.txt", 'r') as f:
        for line in f:
            direction, amount = line.strip().split(" ")
            amount = int(amount)
            commands.append((direction, amount))

    print(f"Part 1: {part1(commands)}")
