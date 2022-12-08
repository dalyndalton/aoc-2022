from math import prod

with open("input.txt") as file:
    grid = [x.strip() for x in file]
    vis = 0
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            vis += (
                all(grid[y][j] < tree for j in range(0, x))
                or all(grid[y][j] < tree for j in range(x + 1, len(row)))
                or all(grid[i][x] < tree for i in range(0, y))
                or all(grid[i][x] < tree for i in range(y + 1, len(grid)))
            )
            
    ans = []
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            ans.append([0, 0, 0, 0])

            for j in range(x - 1, -1, -1):
                ans[-1][0] += 1
                if grid[y][j] >= tree:
                    break

            for i in range(y - 1, -1, -1):
                ans[-1][1] += 1
                if grid[i][x] >= tree:
                    break

            for j in range(x + 1, len(row)):
                ans[-1][2] += 1
                if grid[y][j] >= tree:
                    break

            for i in range(y + 1, len(grid)):
                ans[-1][3] += 1
                if grid[i][x] >= tree:
                    break
                
    sol = max(prod(x) for x in ans)   
    
    print(f"Visible Trees: {vis}")
    print(f"Other Thing: {sol}")
