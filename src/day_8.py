from input_reader import read_file


def part_one(instructions):
    acc = 0
    pc = 0
    visited = []
    program = []

    for instruction in instructions:
        program.append((instruction[0:3], int(instruction[3:])))

    while pc < len(program):
        instruction = program[pc]

        if instruction[0] == 'acc':
            acc += instruction[1]
            pc += 1
        elif instruction[0] == 'jmp':
            pc += instruction[1]
        else:
            pc += 1

        if pc in visited:
            break

        visited.append(pc)

    return acc


def part_two(instructions):
    acc = 0
    pc = 0
    visited = []
    program = []

    for instruction in instructions:
        program.append([instruction[0:3], int(instruction[3:])])

    while pc < len(program):
        instruction = program[pc]
        # print(f"Executing {program[pc]} line {pc + 1}")

        if instruction[0] == 'acc':
            acc += instruction[1]
            pc += 1
        elif instruction[0] == 'jmp':
            pc += instruction[1]
        else:
            pc += 1

        if pc in visited:
            print(f"Modifying {program[visited[-1]][0]} {program[visited[-1]][1]} line {visited[-1] + 1}")
            if program[visited[-1]][0] == 'jmp':
                program[visited[-1]][0] = 'nop'
            elif program[visited[-1]][0] == 'nop':
                program[visited[-1]][0] = 'jmp'

            acc = 0
            pc = 0
            visited = []

        else:
            visited.append(pc)

    return acc


def flip(val):
    return 'jmp' if val == 'nop' else 'nop'


def change_piece(lines):
    for idx, turn in enumerate(lines):
        if turn[0] == 'nop' or turn[0] == 'jmp':
            prev = turn[0]
            lines[idx][0] = flip(turn[0])
            if accumulator := part_one(lines):
                return accumulator
            lines[idx][0] = prev


if __name__ == '__main__':
    inputs = read_file("../inputs/day8.txt")

    print('Part 1: ' + str(part_one(inputs)))
    print('Part2: ' + str(part_two(inputs)))
