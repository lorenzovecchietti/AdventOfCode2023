import time
start = time.time()

import numpy as np

## Load Input
map = []
input = "input.txt"
#input = "input_test.txt"
with open(input) as f:
  for l in f:
    map.append([i for i in l.rstrip()])
map.insert(0, ['#'] * len(map[0]))

## Part 1
start1 = time.time()
sum = 0
for j in range(len(map[0])):
  i = 0
  while i < len(map):
    if map[i][j] == '#':
      ii = i
      while i + 1 < len(map) and map[i + 1][j] != '#':
        i += 1
        if map[i][j] == 'O':
          sum += len(map) - 1 - ii
          ii += 1
    i += 1
print('Part 1:', sum)
end1 = time.time()

## Part 2
start2 = time.time()
iter = 1000000000

map.append(['#'] * len(map[0]))
map = np.asarray(map)
map = np.rot90(map, -1)
map = map.tolist()
map.append(['#'] * len(map[0]))
map.insert(0, ['#'] * len(map[0]))
map = np.asarray(map)
map = np.rot90(map, 1)


def move_rocks(map_to_rotate):
  for j in range(len(map_to_rotate[0])):
    i = 0
    while i < len(map_to_rotate):
      if map_to_rotate[i][j] == '#':
        ii = i + 1
        while i + 1 < len(map_to_rotate) and map_to_rotate[i + 1][j] != '#':
          i += 1
          if map_to_rotate[i][j] == 'O':
            map_to_rotate[i][j], map_to_rotate[ii][j] = '.', 'O'
            ii += 1
      i += 1
  return map_to_rotate


def mode_one_rotation(map_to_rotate):
  map_to_rotate = move_rocks(map_to_rotate)
  map_to_rotate = move_rocks(np.rot90(map_to_rotate, -1))
  map_to_rotate = move_rocks(np.rot90(map_to_rotate, -1))
  map_to_rotate = move_rocks(np.rot90(map_to_rotate, -1))
  map_to_rotate = np.rot90(map_to_rotate, -1)
  return map_to_rotate


def compute_weight(map):
  map = map[1:-1, 1:-1]
  sum = 0
  for i, line in enumerate(map):
    for j, el in enumerate(line):
      if el == 'O':
        sum += map.shape[0] - i
  return sum


sums = []
grids = {}
i = 0
found = False
while i < iter:
  map = mode_one_rotation(map)
  sums.append(compute_weight(map))
  i += 1
  map_b = map.tobytes()
  if not found and map_b in grids:
    cycle_len = i - grids[map_b]
    i = grids[map_b] + cycle_len* ((iter - grids[map_b]) // cycle_len)
    found = True
  else:
    grids[map_b] = i

print('Part 2:', sums[-1])
end2 = time.time()
print("\nTiming:")
print("Part 1 - ", end1 - start1)
print("Part 2 - ", end2 - start2)
print("Total - ", end2 - start)