"""
--- Day 5: Binary Boarding ---
"""
from input_reader import read_file
from math import floor, ceil


def part_one(lines):
    return max(get_ids(lines))


def part_two(lines):
    ids = get_ids(lines)
    ids = sorted(ids)

    for i in range(0, len(ids)):
        if ids[i] != ids[i+1] - 1:
            return ids[i] + 1


def upper_half(part: tuple):
    return ceil(part[0] + ((part[1] - part[0])/2)), part[1]


def lower_half(part: tuple):
    return part[0], floor(part[1] - ((part[1] - part[0])/2))


def calculate_id(row, column):
    return row * 8 + column


def get_ids(lines):
    ids = []

    for line in lines:
        rows = (0, 127)
        columns = (0, 7)

        for ch in line:
            if ch == "F":
                rows = lower_half(rows)
            elif ch == "B":
                rows = upper_half(rows)
            elif ch == "L":
                columns = lower_half(columns)
            elif ch == "R":
                columns = upper_half(columns)

        ids.append(calculate_id(rows[0], columns[0]))
    return ids


if __name__ == '__main__':
    inputs = read_file("../inputs/day5.txt")

    print(part_one(inputs))
    print(part_two(inputs))
