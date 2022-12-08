#!/usr/bin/env python3

if __name__ == "__main__":
    assignment_pairs = []
    with open("input.txt", 'r') as f:
        for line in f:
            range1_start, range1_end, range2_start, range2_end = [int(i) for a in line.strip().split(",") for i in a.split("-")]
            assignment_pairs.append(((range1_start, range1_end), (range2_start, range2_end)))

    # part 1
    count = 0
    for range1, range2 in assignment_pairs:
        if (
            (range2[0] >= range1[0]) and
            (range2[0] <= range1[1]) and
            (range2[1] >= range1[0]) and
            (range2[1] <= range1[1])
        ):
            count += 1 # range 2 is contained in range 1

        elif (
            (range1[0] >= range2[0]) and
            (range1[0] <= range2[1]) and
            (range1[1] >= range2[0]) and
            (range1[1] <= range2[1])
        ):
            count += 1 # range 1 is contained in range 2
    
    print("Part 1:", count)

    # part 2
    count = 0
    for range1, range2 in assignment_pairs:
        if (
            (range1[1] >= range2[0] >= range1[0]) or # start of range 2 is somewhere within range 1
            (range1[1] >= range2[1] >= range1[0]) or # end of range 2 is somewhere within range 1
            (range2[1] >= range1[0] >= range2[0]) or # start of range 1 is somewhere within range 2
            (range2[1] >= range1[1] >= range2[0]) # end of range 1 is somewhere within range 2
        ):
            count += 1

    print("Part 2:", count)