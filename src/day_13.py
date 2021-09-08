"""
--- Day 13: Shuttle Search ---
"""


from math import inf
from time import perf_counter
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


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
    with open('../inputs/day13_test.txt') as f:
        lines = f.read().split()

    bus_ids = lines[1].split(',')
    indexes = []
    tmp = []

    # print(bus_ids)

    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            indexes.append(i)
            tmp.append(int(bus_id))

    bus_ids = tmp

    # print(bus_ids, indexes)

    found = False
    counter = 0
    time_stamp = 0

    while not found:
        #time_stamp += bus_ids[0]
        time_stamp = bus_ids[0] * counter
        # print(time_stamp)
        for i in range(1, len(bus_ids)):
            # print(time_stamps[i])
            if (time_stamp + indexes[i]) % bus_ids[i] != 0:
                found = False
                break
            else:
                found = True
        # print(time_stamps)
        counter += 1
    return time_stamp


def part_two_optimized():
    with open('../inputs/day13.txt') as f:
        lines = f.read().split()

    bus_ids = lines[1].split(',')
    # indexes = []
    tmp = []
    offsets = [int(b) - i for i, b in enumerate(bus_ids) if b != "x"]
    # print(offsets)
    # print(len(bus_ids))
    # print(bus_ids)

    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            # indexes.append(i)
            tmp.append(int(bus_id))

    bus_ids = tmp

    return chinese_remainder(bus_ids, offsets)


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
    """
    start = perf_counter()
    for i in range(0, 10):
        # print(part_one())
        print(part_two())

    end = perf_counter()
    print(f'Execution time part_two(): {end - start}ns')
    """
    print(part_one())

    start = perf_counter()

    print(part_two_optimized())

    end = perf_counter()
    print(f'Execution time part_two_optimized(): {end - start}s')
