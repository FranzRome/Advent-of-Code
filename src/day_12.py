"""
--- Day 12: Rain Risk ---
"""


from math import sin, cos, atan2, radians, degrees, sqrt


def manhattan_distance(x: int, y: int):
    # print(f'Calculating {x} + {y}')
    return abs(x) + abs(y)


def part_one():
    with open("../inputs/day12.txt", 'r') as f:
        instructions = f.read().splitlines()

    position = [0, 0]
    rotation = 0

    # print(instructions)
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            position[1] += value
        elif action == 'S':
            position[1] -= value
        elif action == 'E':
            position[0] += value
        elif action == 'W':
            position[0] -= value
        elif action == 'L':
            rotation += value
        elif action == 'R':
            rotation -= value
        elif action == 'F':
            position[0] += cos(radians(rotation)) * value
            position[1] += sin(radians(rotation)) * value
        # print(f'Action: {action}  Value: {value}  Position: {position}  Rotation: {rotation}')

    return manhattan_distance(position[0], position[1])


def part_two():
    with open("../inputs/day12.txt", 'r') as f:
        instructions = f.read().splitlines()

    ship_position = [0, 0]
    waypoint_position = [10, 1]

    # print(instructions)
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            waypoint_position[1] += value
        elif action == 'S':
            waypoint_position[1] -= value
        elif action == 'E':
            waypoint_position[0] += value
        elif action == 'W':
            waypoint_position[0] -= value
        elif action == 'L' or action == 'R':
            distance = sqrt(waypoint_position[0] * waypoint_position[0] + waypoint_position[1] * waypoint_position[1])
            angle = atan2(waypoint_position[1], waypoint_position[0])
            # print(distance, angle)
            if action == 'L':
                angle += radians(value)
            elif action == 'R':
                angle -= radians(value)
            waypoint_position[0] = cos(angle) * distance
            waypoint_position[1] = sin(angle) * distance
            # print(waypoint_position)
        elif action == 'F':
            ship_position[0] += waypoint_position[0] * value
            ship_position[1] += waypoint_position[1] * value
        # print(f'Action: {action}  Value: {value}')

    return manhattan_distance(ship_position[0], ship_position[1])


if __name__ == '__main__':
    print(round(part_one()))
    print(round(part_two()))
