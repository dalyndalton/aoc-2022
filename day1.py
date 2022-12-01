with open(r"C:\Users\dalyn\Code\Advent\input.txt") as file:
    elves = []
    elves.append(0)
    
    for line in file:
        line = line.strip()
        
        if not line:
            elves.append(0)
        else:
            elves[-1] += int(line)

    print(sum(sorted(elves)[-3:]))        
