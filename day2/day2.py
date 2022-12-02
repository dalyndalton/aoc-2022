# X = rock = 1
# Y = Paper = 2
# z = Scissors = 3

# A = Rock
# B = Paper
# C = Scissors
scoretable = {
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("A", "Z"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
    ("C", "Z"): 3 + 3,
}

resulttable = {
    "X": {
        "A": 3 + 0,
        "B": 1 + 0,
        "C": 2 + 0,
    },
    "Y": {
        "A": 1 + 3,
        "B": 2 + 3,
        "C": 3 + 3,
    },
    "Z": {
        "A": 2 + 6,
        "B": 3 + 6,
        "C": 1 + 6,
    },
}

with open("input.txt") as file:
    processed = [line.strip().split() for line in file]
    scores = [
        scoretable.get((x, y)) for x, y in processed
    ]
    scores2 = [
        resulttable.get(y).get(x) for x, y in processed
    ]
    print(scores2)
    print(f"Total sum: {sum(scores)}")
    print(f"Total new sum: {sum(scores2)}")


