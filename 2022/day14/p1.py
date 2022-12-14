import numpy as np
from pprint import pprint

lines = [x.strip() for x in open("input.txt")]

point_set = []

EMPTY = "."
ROCK = "#"
SAND = "0"


def sandstorm(point: tuple[int, int], ground: np.array) -> bool:
    sx, sy = point

    try:

        postions = [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]
        for p in postions:
            nx, ny = p

            if ground[ny, nx] == EMPTY:
                return sandstorm((nx, ny), ground)

        # If all above moves fail
        ground[sy, sx] = SAND
        return False

    except IndexError as e:
        # Index error means sand has fallen off the map
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

ground = np.full((max_y + 1, max_x - min_x + 1), EMPTY, dtype=str)
sand = 500 - min_x


# Build walls
# -1 is a wall
for pts in point_set:
    sx, sy = pts[0]
    sx -= min_x

    for p in pts[1:]:
        nx, ny = p
        nx -= min_x
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


# Sand loop
i = 0
while True:
    ground[0, sand] = SAND
    if sandstorm((sand, 0), ground):
        print(f"finished {i}")
        break
    
    i += 1
    
for i in ground:
    for j in i:
        print(j, end="")
    print()
