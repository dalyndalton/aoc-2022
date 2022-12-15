import sys

# checks if a cell is covered by a sensor by testing if the distance
# is greater than the one found for the beacon
def check(x, y, sensor_set):
    for sx, sy, dist in sensor_set:
        d = abs(x - sx) + abs(y - sy)
        if d <= dist:
            return False
    return True


with open("input.txt") as file:
    # parse input like im crazy
    lines = [x.strip() for x in file]
    lines = [
        l.replace("Sensor at ", "").replace(" closest beacon is at ", "") for l in lines
    ]
    lines = [l.split(":") for l in lines]
    lines = [[j.split(", ") for j in l] for l in lines]
    lines = [[[int(p[2:]) for p in pair] for pair in l] for l in lines]

sensors = set()
beacons = set()

for idx, l in enumerate(lines):
    sensor, beacon = l
    taxi_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    sx, sy = sensor
    sensors.add((sx, sy, taxi_dist))
    beacons.add(tuple(beacon))


p1 = 0
for x in range(-int(1e7), int(1e7)):
    if x % 100_000 == 0:
        print(f"running {x}", end='\r')
    y = 2000000
    if not check(x, y, sensors) and (x, y) not in beacons:
        p1 += 1
        
print()
print("P1: ", p1)

cells_checked = 0
for sx, sy, d in sensors:
    
    for dx in range(d + 2):
        dy = (d+1) - dx
        for cx, cy in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            cells_checked += 1
            x = sx + (dx * cx)
            y = sy + (dy * cy)
            
            if not(0<=x<=4_000_000 and 0<=y<=4_000_000):
                continue
            
            if check(x,y,sensors):
                # Tune frequency
                print("P2: ", x*4000000 + y)
                sys.exit()