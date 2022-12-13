from functools import cmp_to_key
import copy
idx = 1
correct = []

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    elif type(left) == list and type(right) == list:
        # FK PYTHON WTF
        tl = copy.deepcopy(left)
        tr = copy.deepcopy(right)
        
        while tl and tr:
            l = tl.pop(0)
            r = tr.pop(0)
            
            c = compare(l, r)
            if c == -1:
                return -1
            if c == 1:
                return 1
        # Right runs out first if left left over
        if tl:
            return 1
        elif tr:
            return -1
        else:
            return 0

    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(right) == int and type(left) == list:
        return compare(left, [right])
    
packets = []
with open("input.txt") as file:
    lines = [x.strip() for x in file]
    while lines:
        # Read lines
        left = eval(lines.pop(0))
        right = eval(lines.pop(0))

        packets += [left]
        packets += [right]
        if lines:
            _ = lines.pop(0)

        if compare(left, right) == -1:
            correct.append(idx)

        idx += 1

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(lambda l, r: compare(l, r)))

t_pack = 1
for idx, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        t_pack *= idx + 1
print("Part 1:", sum(correct))
print("Part 2: ", t_pack)
