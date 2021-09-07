"""
--- Day 3: Toboggan Trajectory ---
"""
from input_reader import read_file


def part_one(lines):
    tree = '#'
    slope = (3, 1)
    i = 0
    j = 0
    count = 0

    while i < len(lines):
        if j >= len(lines[i]) - 1:
            j -= len(lines[i])

        if lines[i][j] == tree:

            count += 1
        i += slope[1]
        j += slope[0]

    return count


def part_two(lines):
    tree = '#'
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    result = 1

    for slope in slopes:
        i = 0
        j = 0
        count = 0
        while i < len(lines):
            if j >= len(lines[i]) - 1:
                j -= len(lines[i])

            if lines[i][j] == tree:
                count += 1
            i += slope[1]
            j += slope[0]
        result *= count

    return result


if __name__ == '__main__':
    inputs = read_file("../inputs/day3.txt")

    print(part_one(inputs))
    print(part_two(inputs))
