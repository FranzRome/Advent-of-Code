"""
--- Day 2: Password Philosophy ---
"""
from input_reader import read_file


def part_one(lines):
    valid_count = 0

    for line in lines:
        parts = line.split()
        min_c = int(parts[0].split('-')[0])
        max_c = int(parts[0].split('-')[1])
        char_match = parts[1].strip(':')
        pw = parts[2]

        # print(f"{min} {max} {char_match} {pw}")
        if is_pw_valid_1(min_c, max_c, char_match, pw):
            valid_count += 1
    return valid_count


def is_pw_valid_1(min_c, max_c, char_match, pw):
    count = 0

    for char in pw:
        if char == char_match:
            count += 1

    if min_c <= count <= max_c:
        return True
    else:
        return False


def part_two(lines):
    valid_count = 0

    for line in lines:
        parts = line.split()
        index_1 = int(parts[0].split('-')[0])
        index_2 = int(parts[0].split('-')[1])
        char_match = parts[1].strip(':')
        pw = parts[2]

        if is_pw_valid_2(index_1, index_2, char_match, pw):
            valid_count += 1
    return valid_count


def is_pw_valid_2(index_1, index_2, char_match, pw):
    index_1 -= 1
    index_2 -= 1

    if pw[index_1] == pw[index_2]:
        return False
    elif pw[index_1] == char_match or pw[index_2] == char_match:
        return True
    else:
        return False


if __name__ == '__main__':
    inputs = read_file("../inputs/day2.txt")

    print(part_one(inputs))
    print(part_two(inputs))
