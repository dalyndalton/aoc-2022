import sys

sys.setrecursionlimit(10000)


def path(position, grid):
    # Add positon to set
    queue = []
    queue.append(position)

    visited = dict()
    visited[position] = 0

    while queue:
        c = queue.pop(0)
        y, x = c

        if grid[y][x] == "E":
            return visited[c]

        # find paths
        possible_path = []
        v = ord(grid[y][x]) if grid[y][x] != "S" else ord("a")
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0 or (i != 0 and j != 0):
                    continue
                if (y + i) < 0 or (y + i) >= len(grid):
                    continue
                if (x + j) < 0 or (x + j) >= len(grid[0]):
                    continue

                tmp = ord(grid[y + i][x + j]) if grid[y + i][x + j] != "E" else ord("z")

                if abs(tmp - v) <= 1 or tmp <= v:
                    possible_path.append((y + i, x + j))

        for p in possible_path:
            if p not in visited:
                queue.append(p)
                visited[p] = visited[c] + 1


with open("input.txt") as file:
    print("running")
    grid = [x.strip() for x in file]
    position = tuple()

    # find start
    for i, x in enumerate(grid):
        if "S" in x:
            position = (i, x.index("S"))

    answer = path(position, grid)
    print("Part 1: ", answer)

    m = 400
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "a" or c == "S":
                t = path((y, x), grid)
                if t is not None and t < m:
                    m = t

    print("part 2: ", m)
