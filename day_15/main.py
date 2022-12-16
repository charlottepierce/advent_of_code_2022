#!/usr/bin/env python3

def find_points_beacon_cannot_be_on_row(sensor_x, sensor_y, dist_to_closest_beacon, all_beacon_locs, row):
    points = set()

    dy = abs(sensor_y - row)
    dx = dist_to_closest_beacon - dy

    for x in range(sensor_x - dx, sensor_x + dx + 1):
        test_point = (x, row)
        if (test_point not in all_beacon_locs):
            points.add(test_point)

    return points


def part1(sensor_beacon_pairs):
    test_y = 2000000
    all_beacon_locs = [p[1] for p in sensor_beacon_pairs]

    pos_impossible_for_beacon = set()
    for sensor, beacon in sensor_beacon_pairs:
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon
        dist_sensor_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        
        pos_impossible_for_beacon.update(find_points_beacon_cannot_be_on_row(sensor_x, sensor_y, dist_sensor_beacon, all_beacon_locs, test_y))

    return len(pos_impossible_for_beacon)


def find_range_of_blocked_points(sensor_x, sensor_y, dist_to_closest_beacon, row):
    dy = abs(sensor_y - row)
    dx = dist_to_closest_beacon - dy

    if dx >= 0:
        blocked_start = sensor_x - dx
        blocked_end = sensor_x + dx
        return (blocked_start, blocked_end)
    else:
        return None


def part2(sensor_beacon_pairs, x_max, y_max):
    for y in range(y_max):
        blocked_intervals = []
        for sensor, beacon in sensor_beacon_pairs:
            sensor_x, sensor_y = sensor
            beacon_x, beacon_y = beacon
            dist_sensor_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            blocked = find_range_of_blocked_points(sensor_x, sensor_y, dist_sensor_beacon, y)
            if blocked:
                blocked_min, blocked_max = blocked
                if blocked_min < 0: blocked_min = 0
                if blocked_max > x_max: blocked_max = x_max
                blocked_intervals.append((blocked_min, blocked_max))
            
        # find union of blocked intervals - https://stackoverflow.com/questions/15273693/union-of-multiple-ranges
        blocked_intervals_union = []
        for begin,end in sorted(blocked_intervals):
            if blocked_intervals_union and blocked_intervals_union[-1][1] >= begin - 1:
                blocked_intervals_union[-1][1] = max(blocked_intervals_union[-1][1], end)
            else:
                blocked_intervals_union.append([begin, end])

        if len(blocked_intervals_union) > 1:
            # found the row with the blank
            x = blocked_intervals_union[0][1] + 1
            return x * 4000000 + y


if __name__ == "__main__":
    sensor_beacon_pairs = []
    with open("input.txt", 'r') as f:
        for line in f:
            line = line.strip().replace("Sensor at ", "").replace(" closest beacon is at ", "").replace(", ", "=")
            sensor_pos, beacon_pos = line.split(":")
            sensor_x, sensor_y = int(sensor_pos.split("=")[1]), int(sensor_pos.split("=")[3])
            beacon_x, beacon_y = int(beacon_pos.split("=")[1]), int(beacon_pos.split("=")[3])

            sensor_beacon_pairs.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))

    # print(f"Part 1: {part1(sensor_beacon_pairs)}")
    print(f"Part 2: {part2(sensor_beacon_pairs, 4000000, 4000000)}")