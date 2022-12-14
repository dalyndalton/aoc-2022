import numpy as np
from pprint import pprint

lines = [x.strip() for x in open("input.txt")]

point_set = []

EMPTY = "~"
ROCK = "="
SAND = "`"


def sandstorm(point: tuple[int, int], ground: np.array, max_x) -> bool:
    sx, sy = point

    try:

        postions = [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]
        for p in postions:
            nx, ny = p

            if ground[ny, nx] == EMPTY and nx >= 0 and nx < max_x:
                return sandstorm((nx, ny), ground, max_x)

        # If all above moves fail
        ground[sy, sx] = SAND
        return False

    except IndexError as e:
        # Index error means sand has fallen off the map
        ground[sy, sx] = SAND
        print(e)
        return True


# parse input
for line in lines:
    l = []
    points = line.split(" -> ")
    for p in points:
        x, y = (int(i) for i in p.split(","))
        l.append((x, y))

    point_set.append(l)
# possible bug of falling off right side
max_x, _ = max((max(sub, key=lambda x: x[0]) for sub in point_set), key=lambda x: x[0])
_, max_y = max((max(sub, key=lambda x: x[1]) for sub in point_set), key=lambda x: x[1])

min_x, _ = min((min(sub, key=lambda x: x[0]) for sub in point_set))
_, min_y = min((min(sub, key=lambda x: x[1]) for sub in point_set))

ground = np.full((max_y + 3, max_x - min_x + 1 + (2 * max_y)), EMPTY, dtype=str)
sand = 500 - min_x + max_y


# Build walls
# -1 is a wall
for pts in point_set:
    sx, sy = pts[0]
    sx -= min_x
    sx += max_y
    
    for p in pts[1:]:
        nx, ny = p
        nx -= min_x
        nx += max_y
        # If x value goes backwards
        if sx > nx:
            for i in range(sx, nx - 1, -1):
                ground[sy, i] = ROCK
        # If x value goes forward
        elif sx < nx:
            for i in range(sx, nx + 1):
                ground[sy, i] = ROCK
        elif sy > ny:
            for i in range(sy, ny - 1, -1):
                ground[i, sx] = ROCK
        elif sy < ny:
            for i in range(sy, ny + 1):
                ground[i, sx] = ROCK

        sx, sy = nx, ny

# Build floor
for i in range(max_x - min_x + 1 + (2 * max_y)):
    ground[max_y + 2, i] = ROCK
# Sand loop
i = 0
while True:
    if ground[0, sand] == SAND:
        print(f"finished {i}")
        break
    
    sandstorm((sand, 0), ground, max_x + 1)

    
    i += 1
    
for i in ground:
    for j in i:
        print(j if j != EMPTY else " ", end="")
    print()
