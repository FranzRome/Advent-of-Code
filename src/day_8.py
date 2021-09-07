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
        instruction = instruction.split(' ')
        instruction[1] = int(instruction[1])
        program.append(instruction)

    # print(program)

    for i, line in enumerate(program):
            prev = program[i]
            program[i] = flip(program[i])

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
                    acc = 0
                    pc = 0
                    visited = []
                    break
                else:
                    visited.append(pc)

                if pc >= len(program):
                    return acc

            program[i] = prev


def flip(val):
    return 'jmp' if val == 'nop' else 'nop'


if __name__ == '__main__':
    inputs = read_file("../inputs/day8.txt")

    print('Part 1: ' + str(part_one(inputs)))
    print('Part2: ' + str(part_two(inputs)))
