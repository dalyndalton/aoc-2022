with open("input.txt") as file:
    line = [x.strip() for x in file][0]
    # Part 1
    i = 4
    while i < len(line):
        section = set(line[i - 4 : i])
        if len(section) == 4:
            print(f"FOUND: {i}")
            print(section)
            break
        i += 1

    # Part 2
    i = 14
    while i := 14 < len(line):
        section = set(line[i - 14 : i])
        if len(section) == 14:
            print(f"FOUND: {i}")
            print(section)
            break
        i += 1
