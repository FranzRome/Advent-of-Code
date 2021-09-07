"""
--- Day 13: Shuttle Search ---
"""


from math import inf


def part_one():
    with open('../inputs/day13.txt') as f:
        lines = f.read().split()

    lines[0] = int(lines[0])
    bus_ids = lines[1].replace('x,', '').split(',')

    # print(lines)

    earliest_departure = inf
    earliest_bus_id = -1

    for bus_id in bus_ids:
        # print(type(bus_id))
        bus_id = int(bus_id)
        next_timestamp = lines[0] - (lines[0] % bus_id) + bus_id
        # print(f'Bus id: {bus_id}   Next departure: {next_timestamp}')
        if next_timestamp < earliest_departure:
            earliest_departure = next_timestamp
            earliest_bus_id = bus_id

    waiting_time = earliest_departure - lines[0]
    # print(f'Waiting time: {waiting_time}  Earliest bus id: {earliest_bus_id}')
    return waiting_time * earliest_bus_id


def part_two():
    with open('../inputs/day13.txt') as f:
        lines = f.read().split()

    bus_ids = lines[1].split(',')
    indexes = []
    temp_list = []

    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            indexes.append(i)
            temp_list.append(int(bus_id))
    bus_ids = temp_list

    # print(bus_ids, indexes)

    found = False
    result = 0
    counter = 0

    while not found:
        time_stamps = []
        for i in range(0, len(bus_ids)):
            time_stamps.append(bus_ids[i] * counter)
            # print(time_stamps[i])
            if len(time_stamps) > 1 and (time_stamps[0] + indexes[i]) % bus_ids[i] != 0:
                found = False
                break
            else:
                found = True
        result = time_stamps[0]
        counter += 1
        print(time_stamps)

    return result


if __name__ == '__main__':
    """ 
    Steps to calculate the next bus departure timestamp giving my_timestamp and bus_id
    my_timestamp = 939
    bus_id = 13
    rest = my_timestamp % bus_id
    next_departure = my_timestamp - rest + bus_id

    print(rest)
    print(next_departure)
    """
    # print(part_one())
    print(part_two())
