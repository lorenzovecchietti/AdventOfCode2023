filename = "input.txt"
#filename = "test_input.txt"

with open(filename, "r") as f:
  lines = f.readlines()

## Part 1
sum_history = 0
for line in lines:
  values = []
  values.append([int(i) for i in line.split()])
  while any(v != 0 for v in values[-1]):
    values.append(
        [values[-1][i] - values[-1][i - 1] for i in range(1, len(values[-1]))])
  for i in range(1, len(values)):
    values[len(values) - 1 - i].append(values[len(values) - i][-1] +
                                       values[len(values) - 1 - i][-1])
  sum_history += values[0][-1]

print("Part 1: ", sum_history)


## Part 2
sum_history = 0
for line in lines:
  values = []
  values.append([int(i) for i in line.split()])
  while any(v != 0 for v in values[-1]):
    values.append(
        [values[-1][i] - values[-1][i - 1] for i in range(1, len(values[-1]))])
  for i in range(1, len(values)):
    values[len(values) - 1 - i].insert(0, -values[len(values) - i][0] +
       values[len(values) - 1 - i][0])
  sum_history += values[0][0] 

print("Part 2: ", sum_history)