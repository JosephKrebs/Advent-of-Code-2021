def part_one():
    file = open("input.txt", "r")
    lines = []
    conditional_array = []

    for line in file:
        lines.append(int(line))

    for i in range(len(lines)):
        if i != 0:
            if lines[i] > lines[i-1]:
                conditional_array.append(True)
            else:
                conditional_array.append(False)

    count = 0
    for i in conditional_array:
        if i is True:
            count += 1

    print(count)

def part_two():
    file = open("input.txt", "r")
    lines = []

    for line in file:
        lines.append(int(line))

    block = [lines[i:i+3] for i in range(len(lines) - 2)]
    count = 0
    for f, b in zip(block[:-1], block[1:]):
        if sum(f) < sum(b):
            count += 1
    print(count)

def main():
    part_one()
    part_two()

main()