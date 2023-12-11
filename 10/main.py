import numpy as np
import matplotlib.pyplot as plt

filename = "input.txt"
#filename = "test_input.txt"

lines = []
with open(filename, "r") as f:
  for line in f:
    lines.append(list(line.rstrip()))
lines = np.asarray(lines)

start_pos = np.where(lines == 'S')
start_pos = [i[0] for i in start_pos]

up = np.asarray([-1, 0])
down = np.asarray([1, 0])
right = np.asarray([0, 1])
left = np.asarray([0, -1])
dir_mapping = {
    '|': [down, up],
    '-': [right, left],
    'L': [up, right],
    'J': [up, left],
    '7': [down, left],
    'F': [down, right],
}

ref_mat = np.empty(lines.shape)
ref_mat[:] = np.nan
i = 0
solution_to_be_found = True
for current_direction in [down, up, right, left]:
  current_position = start_pos
  while solution_to_be_found:
    i += 1
    ref_mat[current_position[0], current_position[1]] = 1
    current_position += current_direction
    if lines[current_position[0]][current_position[1]] == 'S':
      solution_to_be_found = False
      break
    possible_directions = dir_mapping[lines[current_position[0],
                                            current_position[1]]]
    if all(i == 0 for i in possible_directions[0] + current_direction):
      current_direction = possible_directions[1]
    else:
      current_direction = possible_directions[0]
    if lines[current_position[0]][current_position[1]] == '.':
      i = 0
      ref_mat = np.empty(lines.shape)
      ref_mat[:] = np.nan
      break

print(i // 2)

plt.imshow(ref_mat)
plt.show()

# expand the loop map with 3x3 tiles for the pipe elements

map_expansion = {
    "|": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "-": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    "L": [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
    "J": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    "7": [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
    "F": [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
    "S": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
}

grid_expanded = np.zeros((3 * len(ref_mat), 3 * len(ref_mat[0])), dtype=int)
for i, line in enumerate(ref_mat):
  for j, element in enumerate(line):
    if not np.isnan(element):
      grid_expanded[3 * i:3 * i + 3,
                    3 * j:3 * j + 3] = map_expansion[lines[i][j]]

plt.imshow(grid_expanded)
plt.show()


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


start_point = (len(grid_expanded)//2, len(grid_expanded[0])//2)
flood_fill(grid_expanded, start_point, -1)

plt.imshow(grid_expanded)
plt.show()

sum_inside = 0
for i, line in enumerate(ref_mat):
  for j, element in enumerate(line):
    if grid_expanded[i * 3 + 1, j * 3 + 1] == -1:
      ref_mat[i][j] = -1
      sum_inside += 1

print(sum_inside)
plt.imshow(ref_mat)
plt.show()
