import numpy as np

input = "input.txt"
#input = "input_test.txt"

with open(input, 'r') as file:
  lines = file.readlines()

directions = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}

maxs = (0, 0)
mins = (0, 0)
pos = (0, 0)
for line in lines:
  d, v, _ = line.split()
  pos = tuple(pos[i] + directions[d][i] * int(v) for i in range(2))
  maxs = tuple(max(maxs[i], pos[i]) for i in range(2))
  mins = tuple(min(mins[i], pos[i]) for i in range(2))

dims = tuple(maxs[i] - mins[i] + 1 for i in range(2))
map = np.zeros(dims)

pos = tuple(-p for p in mins)
for line in lines:
  d, v, _ = line.split()
  v = int(v)
  for i in range(1, v + 1):
    map[pos[0] + directions[d][0] * i, pos[1] + directions[d][1] * i] = 1
  pos = tuple(pos[i] + directions[d][i] * int(v) for i in range(2))

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
axs[0].imshow(map, cmap='hot', interpolation='nearest')


def flood_fill(image, start_point, new_color):
  rows, cols = len(image), len(image[0])
  start_color = image[start_point[0]][start_point[1]]

  if start_color == new_color:
    return

  stack = [start_point]

  while stack:
    x, y = stack.pop()

    if image[x][y] == start_color:
      image[x][y] = new_color

      if x > 0:
        stack.append((x - 1, y))
      if x < rows - 1:
        stack.append((x + 1, y))
      if y > 0:
        stack.append((x, y - 1))
      if y < cols - 1:
        stack.append((x, y + 1))


flood_fill(map, (80, 45), 1)

axs[1].imshow(map, cmap='hot', interpolation='nearest')
#plt.show()
print("Part1: ", np.sum(map))

# Part 2
A = 0
l = 0
num_dir = {0: "R", 1: "D", 2: "L", 3: "U"}
pos = (0, 0)
prev_pos = (0, 0)
for line in lines:
  _, _, hexa = line.split()
  v = int(hexa[2:-2], 16)
  d = num_dir[int(hexa[-2])]
  pos = tuple(pos[i] + directions[d][i] * int(v) for i in range(2))
  A += -pos[0] * prev_pos[1] + pos[1] * prev_pos[0]
  l += int(v)
  prev_pos = pos

print("Part2: ", 0.5 * (A + l) + 1)
