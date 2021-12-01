def part_one():

    file = open("input.txt", "r")

    lines = []
    conds = []
    count = 0
    for line in file:
        lines.append(int(line))

    for i in range(len(lines)):
        if i != 0:
            if lines[i] > lines[i-1]:
                conds.append(True)
            else:
                conds.append(False)

    for i in conds:
        if i is True:
            count += 1

    print(count)

def main():
    part_one()
    part_two()

main()