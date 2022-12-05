#             [J] [Z] [G]
#             [Z] [T] [S] [P] [R]
# [R]         [Q] [V] [B] [G] [J]
# [W] [W]     [N] [L] [V] [W] [C]
# [F] [Q]     [T] [G] [C] [T] [T] [W]
# [H] [D] [W] [W] [H] [T] [R] [M] [B]
# [T] [G] [T] [R] [B] [P] [B] [G] [G]
# [S] [S] [B] [D] [F] [L] [Z] [N] [L]
#  1   2   3   4   5   6   7   8   9

import copy

stack = [
    ["S", "T", "H", "F", "W", "R"],
    ["S", "G", "D", "Q", "W"],
    ["B", "T", "W"],
    ["D", "R", "W", "T", "N", "Q", "Z", "J"],
    ["F", "B", "H", "G", "L", "V", "T", "Z"],
    ["L", "P", "T", "C", "V", "B", "S", "G"],
    ["Z", "B", "R", "T", "W", "G", "P"],
    ["N", "G", "M", "T", "C", "J", "R"],
    ["L", "G", "B", "W"],
]

with open("input.txt") as file:
    commands = [
        (int(z[1]), int(z[3]), int(z[5]))
        for z in [y.split(" ") for y in [x.strip() for x in file]]
    ]

    p1 = copy.deepcopy(stack)
    for amount, start, end in commands:
        for _ in range(amount):
            p1[end - 1].append(p1[start - 1].pop())
    print("Part 1: ", [x[-1] for x in p1])

    p2 = copy.deepcopy(stack)
    for amount, start, end in commands:
        p2[end - 1] += p2[start - 1][-(amount):]
        p2[start - 1] = p2[start - 1][:-(amount)]

    print("Part 2: ", "".join([x[-1] for x in p2]))
