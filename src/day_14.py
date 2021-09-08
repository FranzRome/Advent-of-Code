"""
--- Day 14: Docking Data ---
"""


def part_one():
    with open('../inputs/day14.txt') as f:
        lines = f.read().split('\n')

    mem = {}
    mask = ''
    my_sum = 0

    for line in lines:
        closed_index = 0
        equal_index = 0

        if line[0:2] == 'ma':
            for i, char in enumerate(line):
                if char == "=":
                    mask = line[7:len(line)]
        elif line[0:2] == 'me':
            for i, char in enumerate(line):
                if char == "]":
                    closed_index = i
                elif char == "=":
                    equal_index = i
            mem[line[4:closed_index]] = apply_mask_1(int(line[equal_index + 2:]), mask)

    #print(mem)
    # print(mask)
    # print(lines)
    for m in mem.values():
        my_sum += m

    return my_sum


def apply_mask_1(value: int, mask: str):
    result = ''

    bin_str = str(bin(value))[2:]
    # print(bin_str)

    for i, char in enumerate(mask):
        if char == '0':
            result += '0'
        if char == '1':
            result += '1'

        if i < 36 - len(bin_str):
            if char == 'X':
                result += '0'
        else:
            if char == 'X':
                result += bin_str[i - (36 - len(bin_str))]
        # print(f'i: {i}  Bin str: {bin_str}  Result: {result}')

    # print(f'Bin str: {bin_str}  Result: {result}')

    return bin_str_to_decimal(result)


def part_two():
    with open('../inputs/day14.txt') as f:
        lines = f.read().split()


def bin_str_to_decimal(bin_str: str):
    result = 0

    for i, char in enumerate(bin_str):
        result += int(char) * pow(2, len(bin_str) - i - 1)
    # print(result)

    return result


if __name__ == '__main__':
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
