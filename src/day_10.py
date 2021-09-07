"""
--- Day 10: Adapter Array ---
"""


from input_reader import read_file
from functools import lru_cache

def part_one(adapters: list):
    jolts_output = 0
    differences_of_1 = 0
    # This variable starts at 1 cause the last output of the list is not included but it has to be counted
    differences_of_3 = 0

    # print(adapters)

    for adapter in adapters:
        difference = adapter - jolts_output
        # print(f'Evaluating {jolts_output} with {adapter}, difference {difference}')

        if difference == 1:
            differences_of_1 += 1
        elif difference == 3:
            differences_of_3 += 1

        jolts_output += difference

    # print(differences_of_1)
    # print(differences_of_3)
    return differences_of_1 * differences_of_3


def part_two(adapters: list):
    jolts_output = 0
    combinations = 1

    print(f'{adapters}')

    for j in range(0, (len(adapters) - 1)):
        difference = adapters[j + 1] - jolts_output
        # print(f'Difference: {adapters[j + 1]} - {jolts_output} = {difference}')
        if difference <= 3:
            new_list = adapters.copy()
            new_list.remove(adapters[j])
            combinations = combinations + part_two(new_list)

        jolts_output = adapters[j]

    print(f'Combinations: {combinations}')
    return combinations


@lru_cache(maxsize=256)
def paths_to_end(i):
    if i == len(inputs) - 1:
        return 1
    return sum(
        [
            paths_to_end(j)
            for j in range(i + 1, min(i + 4, len(inputs)))
            if inputs[j] - inputs[i] <= 3
        ]
    )


if __name__ == '__main__':
    inputs = read_file("../inputs/day10.txt")

    for i in range(0, len(inputs)):
        inputs[i] = int(inputs[i])

    # part_one and part_two work only with sorted list of values
    inputs = sorted(inputs + [0, max(inputs) + 3])

    test_input = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
    test_input = sorted(test_input)

    pt_1 = part_one(inputs)
    # pt_2 = part_two(test_input)
    pt_2 = paths_to_end(0)

    print(f'Part 1: {pt_1}')
    print(f'Part 2: {pt_2}')
