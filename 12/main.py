import numpy as np

## Load Input
all_maps = []
map = []
input = "input.txt"
#input = "input_test.txt"
with open(input) as f:
  for l in f:
    if l == "\n":
      all_maps.append(np.asarray(map))
      map = []
    else:
      map.append([i for i in l.rstrip()])
all_maps.append(np.asarray(map))


## Part 1
def check_sym_line(map):
  for i in range(1, len(map[0])):
    is_reflect_line = False
    itest = min(i, len(map[0]) - i)
    a = map[:, i - itest:i]
    b = np.flip(map[:, i:itest + i], axis=1)
    if np.array_equal(a, b):
      is_reflect_line = True
      break
  if is_reflect_line:
    return i
  else:
    return None


total_sum = 0
for map in all_maps:
  i = check_sym_line(map)
  if i is not None:
    total_sum += i
  else:
    i = check_sym_line(map.T)
    total_sum += i * 100

print("Part 1: ", total_sum)


## Part 2
def check_sym_line_with_smudges(map):
  for i in range(1, len(map[0])):
    is_reflect_line = False
    itest = min(i, len(map[0]) - i)
    a = map[:, i - itest:i]
    b = np.flip(map[:, i:itest + i], axis=1)
    if np.sum(a!=b)==1:
      is_reflect_line = True
      break
  if is_reflect_line:
    return i
  else:
    return None


total_sum = 0
for map in all_maps:
  i = check_sym_line_with_smudges(map)
  if i is not None:
    total_sum += i
  else:
    i = check_sym_line_with_smudges(map.T)
    total_sum += i * 100

print("Part 2: ", total_sum)
