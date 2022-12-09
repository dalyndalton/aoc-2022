def fix(head, tail):
    hx, hy = head
    tx, ty = tail

    dx = hx - tx
    dy = hy - ty

    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif abs(dx) >= 2 and abs(dy) >= 2:
        tail = (hx - 1 if tx < hx else hx + 1, hy - 1 if ty < hy else hy + 1)
    elif abs(dx) >= 2:
        tail = (hx - 1 if tx < hx else hx + 1, hy)
    elif abs(dy) >= 2:
        tail = (hx, hy - 1 if ty < hy else hy + 1)
    return tail


with open("input.txt") as file:
    commands = [(a, int(b)) for a, b in [x.strip().split(" ") for x in file]]

    H = (0, 0)
    T = [(0, 0)] * 9

    board1 = set([T[0]])
    board2 = set([T[8]])

    X = {"L": 0, "U": -1, "R": 0, "D": 1}
    Y = {"L": -1, "U": 0, "R": 1, "D": 0}

    for direction, distance in commands:
        for _ in range(distance):
            H = (H[0] + X[direction], H[1] + Y[direction])

            T[0] = fix(H, T[0])

            # Tail takes old head position if its to far away
            for i in range(1, 9):
                T[i] = fix(T[i - 1], T[i])

            board1.add(T[0])
            board2.add(T[8])

    print(len(board1))
    print(len(board2))
