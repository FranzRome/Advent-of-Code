"""
--- Day 7: Handy Haversacks ---
"""
from input_reader import read_file
from regex import regex


def part_one(bag_collection):
    result = 0

    for bag_name in bag_collection.keys():
        if shiny_gold_bag_count(bag_collection, bag_name) > 0:
            result += 1

    return result


def part_two(bag_collection, bag_name):
    count = 0
    top_level_bag = bag_collection[bag_name]

    if len(top_level_bag) == 0:
        return count
    else:
        for current_bag in top_level_bag:
            # Add the number of bags of the current type
            # to the count.
            current_bag_type_count = current_bag['count']
            count += current_bag_type_count
            # Count the bags inside each bag of the current type,
            # multiply it by the number of the current type,
            # then add it to the count.
            bags_inside_current_bag_type_count = part_two(bag_collection, current_bag["type"])
            count += bags_inside_current_bag_type_count * current_bag_type_count

    return count


def shiny_gold_bag_count(bag_collection, bag_name):
    count = 0
    bag = bag_collection[bag_name]

    if len(bag) == 0:
        return count
    else:
        for sub_bag in bag:
            if sub_bag["type"] == "shiny gold":
                count += 1
            count += shiny_gold_bag_count(bag_collection, sub_bag["type"])

    return count


def get_rules(lines):
    result = {}

    for item in lines:
        bag_and_contents_regex = r"^(\w+ \w+) bags contain (.*)"
        bag_and_contents = regex.search(bag_and_contents_regex, item)
        bag_type = bag_and_contents[1]

        contents_string = bag_and_contents[2][:-1]  # [:-1] removes trailing period
        contents_regex = r"([0-9] )*(\w+ \w+) bag"
        contents_tuples = regex.findall(contents_regex, contents_string)

        bag_contents = []
        for contents_tuple in contents_tuples:
            if contents_tuple[1] != "no other":
                bag_contents.append({
                    "count": int(contents_tuple[0]),
                    "type": contents_tuple[1]
                })

        result[bag_type] = bag_contents

    return result


if __name__ == '__main__':
    inputs = read_file("../inputs/day7.txt")
    inputs = get_rules(inputs)

    print('Part 1: ' + str(part_one(inputs)))
    print('Part2: ' + str(part_two(inputs, "shiny gold")))
