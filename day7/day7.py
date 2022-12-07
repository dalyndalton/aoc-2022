# Returns local + grand total
def find_sizes(dir: dict) -> list[int, int]:
    total = 0
    grand_total = 0
    for _, val in dir.items():
        if type(val) == dict:
            t, gt = find_sizes(val)
            total += t
            grand_total += gt
        else:
            total += val

    if total > 100000:
        return [total, grand_total]
    else:
        return [total, grand_total + total]


def find_goal(dir: dict, goal, c_min=70000000) -> list[int, int]:
    total = 0
    for _, val in dir.items():
        if type(val) == dict:
            t, m = find_goal(val, goal, c_min)
            total += t
            c_min = min(m, c_min)
        else:
            total += val

    if total > goal and total < c_min:
        return [total, total]
    else:
        return [total, c_min]


# Helper function, not really needed
def sumall(dir):
    total = 0
    for _, val in dir.items():
        if type(val) == dict:
            total += sumall(val)
        else:
            total += val
    return total


with open("input") as file:
    lines = [l.strip() for l in file]

    home = {}
    current_directory: dict = home
    directory_stack = []

    # Parser
    while lines:
        line = lines.pop(0)

        match line.split():
            case ["$", "ls"]:
                while True:
                    if lines:
                        current_line = lines.pop(0)
                    else:
                        break
                    match current_line.split(" "):
                        # Create new directory
                        case ["dir", name]:
                            current_directory[name] = dict()
                        case [size, name]:
                            current_directory[name] = int(size)
                        case ["$", *args]:
                            lines.insert(0, current_line)
                            break

            case ["$", "cd", location]:
                if location == "..":
                    current_directory = directory_stack.pop()
                else:
                    directory_stack.append(current_directory)
                    current_directory = current_directory[location]

    # Calculator
    _, total = find_sizes(home)
    print(f"Size is: {total}")
    used_space = sumall(home)
    total_disk = 70_000_000
    update_space = 30_000_000
    goal = update_space - (total_disk - used_space)
    print(goal)
    print(f"Minimum found: {find_goal(home, goal)}")
