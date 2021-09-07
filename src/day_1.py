"""
--- Day 1: Report Repair ---
"""
from input_reader import read_file


def part_one(lines, target_value):
    for i in range(0, len(lines)):
        for j in range(1, len(lines)):
            if i != j:
                a = int(lines[i])
                b = int(lines[j])
                add = a + b

                if add == target_value:
                    output = a * b
                    return output


def part_two(lines, target_value):
    for i in range(0, len(lines)):
        for j in range(1, len(lines)):
            for k in range(2, len(lines)):
                if i != j != k:
                    a = int(lines[i])
                    b = int(lines[j])
                    c = int(lines[k])
                    add = a + b + c

                    if add == target_value:
                        output = a * b * c
                        return output


if __name__ == '__main__':
    inputs = read_file("../inputs/day1.txt")
    target_value = 2020

    print(part_one(inputs, target_value))
    print(part_two(inputs, target_value))
