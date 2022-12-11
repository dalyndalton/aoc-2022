from math import prod


class Monkey:
    # Test = [number, true, false]
    def __init__(self, items: list, operation, test: tuple):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection = 0

    def turn(self):
        throws = []
        for item in self.items:
            item = self.operation(item)
            self.inspection += 1

            # Worry fade
            item = item // 3

            # Test
            if (item % self.test[0]) == 0:
                throws.append((self.test[1], item))
            else:
                throws.append((self.test[2], item))
        self.items = []

        return throws


if __name__ == "__main__":
    monkeys = [
        Monkey([73, 77], lambda x: x * 5, (11, 6, 5)),
        Monkey([57, 88, 80], lambda x: x + 5, (19, 6, 0)),
        Monkey([61, 81, 84, 69, 77, 88], lambda x: x * 19, (5, 3, 1)),
        Monkey([78, 89, 71, 60, 81, 84, 87, 75], lambda old: old + 7, (3, 1, 0)),
        Monkey([60, 76, 90, 63, 86, 87, 89], lambda x: x + 2, (13, 2, 7)),
        Monkey([88], lambda x: x + 1, (17, 4, 7)),
        Monkey([84, 98, 78, 85], lambda x: x * x, (7, 5, 4)),
        Monkey([98, 89, 78, 73, 71], lambda x: x + 4, (2, 3, 2)),
    ]

    for _ in range(20):
        for m in monkeys:
            items = m.turn()
            for m, item in items:
                monkeys[m].items.append(item)

    m1, m2, *_ = sorted(monkeys, key=lambda x: x.inspection)[::-1]
    print(m1.inspection * m2.inspection)
