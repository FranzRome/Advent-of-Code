import os

def read_file(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


def read_passport_file(path):
    with open(path, 'r') as f:
        #print(lines)
        passports = []
        passport = {}
        for line in f:
            if line != '\n':
                line = line.rstrip().split(" ")
                line = [field.split(":") for field in line]
                for field in line:
                    passport[field[0]] = field[1]
            else:
                passports.append(passport)
                passport = {}
        passports.append(passport)
        return passports

def read_tickets_file():
    os.path.dirname(__file__)
    print(read_file("./inputs/day16.txt"))

if __name__ == '__main__':
    # print(read_file("../inputs/day1.txt"))
    print(read_passport_file("../inputs/day4.txt"))
