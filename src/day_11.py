"""
--- Day 11: Seating System ---
"""


def adj_occupied(seats, i, j):
    result = 0

    for k in range((i - 1 if i > 0 else i), (i + 2 if i < len(seats) - 1 else i + 1)):
        for l in range((j - 1 if j > 0 else j), (j + 2 if j < len(seats[i]) - 1 else j + 1)):
            # print(f'{len(seats)}  {len(seats[i])}  {k}  {l}')
            if not (k == i and l == j) and seats[k][l] == '#':
                result += 1

    return result


def at_sight_occupied(seats, i, j):
    result = 0

    for k in range((-1 if i > 0 else 0), (2 if i < len(seats) - 1 else 1)):
        for l in range((-1 if j > 0 else 0), (2 if j < len(seats[i]) - 1 else 1)):
            # print(f'k: {i}  l: {l}')
            if not(k == 0 and l == 0):
                m = 1
                while True:
                    point_to_analyze = [int(i + k * m), int(j + l * m)]
                    # print(point_to_analyze)
                    if point_to_analyze[0] < 0 or point_to_analyze[0] >= len(seats) or \
                       point_to_analyze[1] < 0 or point_to_analyze[1] >= len(seats[i]) or \
                       seats[point_to_analyze[0]][point_to_analyze[1]] == 'L':
                        break
                    elif seats[point_to_analyze[0]][point_to_analyze[1]] == '#':
                        result += 1
                        break
                        # print(f'Found occupied seat at {point_to_analyze}')
                    m += 1
    return result


def count_occupied(seats):
    result = 0

    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == '#':
                result += 1

    return result


def part_one():
    seats = [list(x) for x in open("../inputs/day11.txt").read().splitlines()]
    stabilized = False

    # Part one
    while not stabilized:
        next_state = []
        new_line = []
        # print(f'There are {len(seats)} lines')
        for i in range(0, len(seats)):
            # print(f'Line {i} has {len(seats[i])} elements')
            # print(seats[i])
            for j in range(0, len(seats[i])):
                if seats[i][j] == '.':
                    new_line.append('.')
                elif seats[i][j] == 'L':
                    if adj_occupied(seats, i, j) == 0:
                        new_line.append('#')
                    else:
                        new_line.append('L')
                elif seats[i][j] == '#':
                    if adj_occupied(seats, i, j) >= 4:
                        new_line.append('L')
                    else:
                        new_line.append('#')
            next_state.append(new_line)
            new_line = []
        if seats == next_state:
            stabilized = True
        seats = next_state
        # print('\n\n')
        # print(seats)
    return count_occupied(seats)


def part_two():
    seats = [list(x) for x in open("../inputs/day11.txt").read().splitlines()]
    stabilized = False

    while not stabilized:
        next_state = []
        new_line = []
        # print(f'There are {len(seats)} lines')
        # print(at_sight_occupied(seats, 0, 0))
        for i in range(0, len(seats)):
            # print(f'Line {i} has {len(seats[i])} elements')
            # print(seats[i])
            for j in range(0, len(seats[i])):
                if seats[i][j] == '.':
                    new_line.append('.')
                elif seats[i][j] == 'L':
                    if at_sight_occupied(seats, i, j) == 0:
                        new_line.append('#')
                    else:
                        new_line.append('L')
                elif seats[i][j] == '#':
                    if at_sight_occupied(seats, i, j) >= 5:
                        new_line.append('L')
                    else:
                        new_line.append('#')
            next_state.append(new_line)
            new_line = []
        if seats == next_state:
            stabilized = True
        seats = next_state
        # print('\n\n')
        # print(seats)
    return count_occupied(seats)


if __name__ == '__main__':
    # print(f'Occupied seats pt_1: {part_one()}')
    print(f'Occupied seats pt_2: {part_two()}')

    '''
    test_a = [list(x) for x in open("../inputs/day11_test_a.txt").read().splitlines()]
    # print(test_a)
    print(at_sight_occupied(test_a, 4, 3))

    test_b = [list(x) for x in open("../inputs/day11_test_b.txt").read().splitlines()]
    # print(test_b)
    print(at_sight_occupied(test_b, 1, 1))

    test_c = [list(x) for x in open("../inputs/day11_test_c.txt").read().splitlines()]
    # print(test_c)
    print(at_sight_occupied(test_c, 3, 3))
    '''