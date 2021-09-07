"""
--- Day 6: Custom Customs ---
"""
from input_reader import read_file


def part_one(lines):
    result = 0
    answers = set()
    for line in lines:
        if line != '':
            for ch in line:
                # print(ch)
                answers.update(ch)
        else:
            result += len(answers)
            # print(len(answers))
            # print('SPACE')
            answers = set()

    return result


def part_two(lines):
    result = 0
    intersection = set()
    group = []

    for line in lines:
        if line != '':
            group.append(line)

        else:
            # print(group)
            intersection.update(group[0])
            for answers in group:
                intersection.intersection_update(answers)
            result += len(intersection)
            intersection = set()
            group = []

    return result


if __name__ == '__main__':
    inputs = read_file("../inputs/day6.txt")

    print('Part 1: ' + str(part_one(inputs)))
    print('Part2: ' + str(part_two(inputs)))
