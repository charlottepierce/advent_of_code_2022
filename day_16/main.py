#!/usr/bin/env python3

import functools

valve_info = {}

class Valve(object):
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.connected = tunnels

    def __str__(self):
        desc = f"Valve {self.name} has flow rate={self.flow_rate};"
        if len(self.connected) == 1:
            desc += f" tunnel leads to valve {self.connected[0]}"
        else:
            desc += " tunnels lead to valves"
            for t in self.connected:
                desc += f" {t},"
            desc = desc.rstrip(",")

        return desc


@functools.cache
def shortest_path(start_valve, end_valve):
    queue = [[start_valve, 0]] # node, distance of path
    seen = [start_valve]

    best = None

    while len(queue) > 0:
        curr, distance = queue.pop(0)

        if curr == end_valve:
            if (best == None) or (distance < best):
                best = distance

        for v in valve_info[curr].connected:
            if v not in seen:
                seen.append(v)
                queue.append([v, distance + 1])

    return best


def part1():
    time_limit = 30
    start_valve = "AA"
    maximum_pressure_released = 0

    valves_with_flow = [v.name for v in valve_info.values() if v.flow_rate > 0]

    queue = []
    queue.append([[start_valve], {}, 0]) # list path of valves, dict of valve name : minute it was opened, minutes passed

    while len(queue) > 0:
        path, open_valves, minutes_passed = queue.pop()
        # print(f"Queue length = {len(queue)}; at minute {minutes_passed} with {len(open_valves)} open valves of {len(valves_with_flow)}")

        if (minutes_passed >= time_limit) or (len(open_valves.keys()) == len(valves_with_flow)):
            # print(f"Found one possibility at minute {minutes_passed} with path {path}; queue still {len(queue)} long")
            # calculate pressure released on this path
            pressure_released = 0
            for valve, time_opened in open_valves.items():
                minutes_open = max(time_limit - time_opened, 0)
                pressure_released += minutes_open * valve_info[valve].flow_rate

            # check if it's better than the previously known best
            maximum_pressure_released = max(maximum_pressure_released, pressure_released)
        else:
            curr_valve = path[-1]

            # try to travel to each unopened valve with flow
            for v in valves_with_flow:
                if v not in open_valves.keys():
                    # valve isn't already opened in this path, so try to get to it
                    travel_time = shortest_path(curr_valve, v)
                    opening_time = 1

                    new_minutes_passed = minutes_passed + travel_time + opening_time

                    new_open_valves = open_valves.copy()
                    new_open_valves[v] = new_minutes_passed

                    new_path = path[:]
                    new_path.append(v)

                    queue.append([new_path, new_open_valves, new_minutes_passed])
            
    return maximum_pressure_released


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        for line in f:
            init_info, tunnel_info = line.strip().split(";")
            name = init_info.split(" ")[1]
            flow_rate = int(init_info.split("=")[-1])
            tunnels = tunnel_info.replace("tunnels", "tunnel").replace("leads", "lead").replace("valves", "valve").replace("tunnel lead to valve", "").split(",")
            tunnels = [t.strip() for t in tunnels]
            
            valve_info[name] = Valve(name, flow_rate, tunnels)

    print(f"Part 1: {part1()}")