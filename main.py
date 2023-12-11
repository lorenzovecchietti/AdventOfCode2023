import numpy as np

filename = "input.txt"
#filename = "test_input.txt"
exp_ratio = 1000000-1

lines = []
with open(filename, "r") as f:
  for line in f:
    lines.append(list(line.rstrip()))
lines = np.asarray(lines)

## Part 1
expanded_lines = np.copy(lines)
for ax, lines_t in zip([0, 1], [lines, lines.T]):
  l_idx = 0
  for l in lines_t:
    if all(i == "." for i in l):
      expanded_lines = np.insert(
          expanded_lines,
          l_idx, ['.'] *
          [len(expanded_lines[0]), len(expanded_lines)][ax],
          axis=ax)
      l_idx += 1
    l_idx += 1

galaxy = np.where(expanded_lines == '#')
sum_paths = 0
for i in range(len(galaxy[0])):
  for j in range(i + 1, len(galaxy[0])):
    sum_paths += abs(galaxy[0][i] - galaxy[0][j]) + abs(galaxy[1][i] -
                                                        galaxy[1][j])

print("Part 1: " + str(sum_paths))

## Part 2
expand = [[], []]
for ax, lines_t in zip([0, 1], [lines, lines.T]):
  l_idx = 0
  for l in lines_t:
    if all(i == "." for i in l):
      expand[ax].append(l_idx)
    l_idx += 1

galaxy = np.where(lines == '#')
sum_paths = 0
for i in range(len(galaxy[0])):
  for j in range(i + 1, len(galaxy[0])):
    if galaxy[0][i] < galaxy[0][j]:
      add_row = np.sum((galaxy[0][i] <= expand[0])
                       & (expand[0] <= galaxy[0][j]))
    else:
      add_row = np.sum((galaxy[0][i] > expand[0]) & (expand[0] > galaxy[0][j]))
    if galaxy[1][i] < galaxy[1][j]:
      add_col = np.sum((galaxy[1][i] < expand[1]) & (expand[1] < galaxy[1][j]))
    else:
      add_col = np.sum((galaxy[1][i] > expand[1]) & (expand[1] > galaxy[1][j]))
    sum_paths += abs(galaxy[0][i] - galaxy[0][j]) + abs(
        galaxy[1][i] - galaxy[1][j]) + (add_row + add_col) * exp_ratio

print("Part 2: " + str(sum_paths))
