p1 = 0
p2 = 0
with open("input.txt") as file:
    for line in file:
        a, b = [
            range(int(y[0]), int(y[1]) + 1)
            for y in [x.split("-") for x in line.strip().split(",")]
        ]
        if (a.start in b and a[-1] in b) or (b.start in a and b[-1] in a):
            p1 += 1
        if (a.start in b or a[-1] in b) or (b.start in a or b[-1] in a):
            p2 += 1

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")