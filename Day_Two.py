def input_collector(fileName):
    file = open(fileName, "r")
    lines = []

    for line in file:
        lines.append(line)

    return lines


def total_horizontal(lines, aim):
    position = 0
    depth = 0
    for line in lines:
        if "forward" in line:
            position += int(line[8])
            depth += aim*int(line[8])

    return position, depth


def total_depth(lines):
    aim = 0
    for line in lines:
        if "down" in line:
            aim += int(line[5])
        if "up" in line:
            aim -= int(line[3])
    return aim


def main():
    lines = input_collector("input2.txt")
    aim = total_depth(lines)
    horizontal, depth2 = total_horizontal(lines, aim)
    print(depth2*horizontal)


main()