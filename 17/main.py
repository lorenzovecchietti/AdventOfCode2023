import heapq

input = "input.txt"
#input = "input_test.txt"

with open(input, 'r') as file:
  lines = file.readlines()
  matrix = [list(map(int, list(line.strip()))) for line in lines]

start_node = (0, 0)
end_node = (len(matrix) - 1, len(matrix[0]) - 1)

## Part 1
possible_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = [(0, 0, 0, -1)] # costo, x, y, direzione non supp
seen = set()
final_cost=None
costs = {}
while q:
  cost, x, y, no_dir = heapq.heappop(q)
  if x == len(matrix[0]) - 1 and y == len(matrix) - 1: #if final node
    final_cost=cost
    break
  if (x, y, no_dir) in seen:
    continue
  seen.add((x, y, no_dir))
  for direction in range(4):
    costincrease = 0
    if direction == no_dir or (direction + 2) % 4 == no_dir:
      continue
    for distance in range(1, 3 + 1):
      xx = x + possible_directions[direction][0] * distance
      yy = y + possible_directions[direction][1] * distance
      if xx in range(len(matrix[0])) and yy in range(len(matrix)):
        costincrease += matrix[xx][yy]
        nc = cost + costincrease
        if costs.get((xx, yy, direction), 1e100) <= nc:
          continue
        costs[(xx, yy, direction)] = nc
        heapq.heappush(q, (nc, xx, yy, direction))

print("Part 1:", final_cost)



## Part 2
possible_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = [(0, 0, 0, -1)]
seen = set()
costs = {}
final_cost=None
while q:
  cost, x, y, no_dir = heapq.heappop(q)
  if x == len(matrix[0]) - 1 and y == len(matrix) - 1:
    final_cost=cost
    break
  if (x, y, no_dir) in seen:
    continue
  seen.add((x, y, no_dir))
  for direction in range(4):
    costincrease = 0
    if direction == no_dir or (direction + 2) % 4 == no_dir:
      continue
    for distance in range(1, 10 + 1):
      xx = x + possible_directions[direction][0] * distance
      yy = y + possible_directions[direction][1] * distance
      if xx in range(len(matrix[0])) and yy in range(len(matrix)):
        costincrease += matrix[xx][yy]
        if distance < 4:
          continue
        nc = cost + costincrease
        if costs.get((xx, yy, direction), 1e100) <= nc:
          continue
        costs[(xx, yy, direction)] = nc
        heapq.heappush(q, (nc, xx, yy, direction))

print("Part 2:", final_cost)