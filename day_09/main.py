#!/usr/bin/env python3

def resolve_position(head, tail):
    chebyshev_distance = max(abs(head[1] - tail[1]), abs(head[0] - tail[0]))
    if chebyshev_distance <= 1:
        return tail # close enough, don't need to move the tail

    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if dx == 0: # up or down
        if dy > 0:
            return [tail[0], tail[1] + 1] # head is above tail, move tail up
        else:
            return [tail[0], tail[1] - 1] # head is below tail, move tail down
    elif dy == 0: # left or right
        if dx > 0:
            return [tail[0] + 1, tail[1]] # head is to the right of tail, move tail right
        else:
            return [tail[0] - 1, tail[1]] # head is to the left of tail, move tail left
    else: # somehow diagonal - move diagonally to catch up
        if (dy > 0) and (dx < 0):
            return [tail[0] - 1, tail[1] + 1] # head is up and left from tail, move tail up and left
        elif (dy > 0) and (dx > 0):
            return [tail[0] + 1, tail[1] + 1] # head is up and right from tail, move tail up and right
        elif (dy < 0) and (dx < 0):
            return [tail[0] - 1, tail[1] - 1] # head is down and left from tail, move tail down and left
        elif (dy < 0) and (dx > 0):
            return [tail[0] + 1, tail[1] - 1] # head is down and right from tail, move tail down and right


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
            # tail_pos = _resolve_tail_pt1(head_pos, tail_pos, direction)
            tail_pos = resolve_position(head_pos, tail_pos)
            unique_tail_positions.add(tuple(tail_pos))
    
    return len(unique_tail_positions)


def part2(commands):
    knots = [[0, 0] for x in range(10)]

    unique_tail_positions = set()
    unique_tail_positions.add(tuple(knots[-1]))

    for direction, amount in commands:
        for x in range(amount):
            match direction:
                case "U":
                    knots[0][1] += 1
                case "D":
                    knots[0][1] -= 1
                case "L":
                    knots[0][0] -= 1
                case "R":
                    knots[0][0] += 1
            
            for x in range(1, len(knots)):
                knots[x] = resolve_position(knots[x-1], knots[x])
            unique_tail_positions.add(tuple(knots[-1]))
    
    return len(unique_tail_positions)


if __name__ == "__main__":
    commands = []
    with open("input.txt", 'r') as f:
        for line in f:
            direction, amount = line.strip().split(" ")
            amount = int(amount)
            commands.append((direction, amount))

    print(f"Part 1: {part1(commands)}")
    print(f"Part 2: {part2(commands)}")
