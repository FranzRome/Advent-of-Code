"""
--- Day 4: Passport Processing ---
"""
from input_reader import read_passport_file
import re


def part_one(passports):
    result = 0
    for passport in passports:
        if is_fields_count_valid(passport):
            result += 1
    return result


def part_two(passports):
    result = 0
    for passport in passports:
        if is_fields_count_valid(passport) and \
           is_byr_valid(passport['byr']) and \
           is_iyr_valid(passport['iyr']) and \
           is_eyr_valid(passport['eyr']) and \
           is_hgt_valid(passport['hgt']) and \
           is_hcl_valid(passport['hcl']) and \
           is_ecl_valid(passport['ecl']) and \
           is_pid_valid(passport['pid']):
            result += 1
            # print(passport)
    return result


def is_fields_count_valid(passport):
    return (len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport)


def is_byr_valid(byr):
    return 1920 <= int(byr) <= 2002


def is_iyr_valid(iyr):
    return 2010 <= int(iyr) <= 2020


def is_eyr_valid(eyr):
    return 2020 <= int(eyr) <= 2030


def is_hgt_valid(hgt):
    return ('cm' in hgt and 150 <= int(hgt[:-2]) <= 193) or ('in' in hgt and 59 <= int(hgt[:-2]) <= 76)


def is_hcl_valid(hcl):
    # print(hcl)
    return hcl[0] == '#' and len(hcl[1:]) == 6 and re.compile('\d[a-f]')


def is_ecl_valid(ecl):
    return ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'


def is_pid_valid(pid):
    return len(pid) == 9


if __name__ == '__main__':
    inputs = read_passport_file("../inputs/day4.txt")

    print(part_one(inputs))
    print(part_two(inputs))
