def input_collector(fileName):
    file = open(fileName, "r")
    lines = []

    for line in file:
        lines.append(line)

    return lines


def total_horizontal(lines):
    position = 0
    for line in lines:
        if "forward" in line:
            position += int(line[8])
    return position


def total_depth(lines):
    depth = 0
    for line in lines:
        if "down" in line:
            depth += int(line[5])
        if "up" in line:
            depth -= int(line[3])
    return depth


def main():
    lines = input_collector("input2.txt")
    horizontal = total_horizontal(lines)
    depth = total_depth(lines)
    print(depth*horizontal)


main()