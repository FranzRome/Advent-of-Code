"""
--- Day 9: Encoding Error ---
"""
from input_reader import read_file


def part_one(lines):
    result = 0
    preamble_len = 25

    for i in range(preamble_len, len(lines)):
        preamble = lines[i - preamble_len: i]
        x = lines[i]
        match = False
        # print(f'Preamble length: {(len(preamble))}')
        # print(preamble)
        for j in range(0, len(preamble)):
            for k in range(0, len(preamble)):
                y = preamble[j]
                z = preamble[k]

                if y != z:
                    # print(f'x + y = {x + y}')
                    if y + z == int(x):
                        match = True
                if match:
                    break
            if match:
                break
        if not match:
            return x

    return result


def part_two(lines, weakness):

    for set_len in range(2, len(lines)):
        for i in range(0, len(lines) - set_len):
            contiguous_set = set(lines[i: i + set_len])
            if sum(contiguous_set) == weakness:
                return max(contiguous_set) + min(contiguous_set)


if __name__ == '__main__':
    inputs = read_file("../inputs/day9.txt")

    for i in range(0, len(inputs)):
        inputs[i] = int(inputs[i])

    pt_1 = part_one(inputs)

    print('Part 1: ' + str(pt_1))
    print('Part2: ' + str(part_two(inputs, pt_1)))
