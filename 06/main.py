import numpy as np

filename = "input.txt"

with open(filename, "r") as f:
  lines = f.readlines()

## Part 1
times = np.asarray([
    int(a) for a in lines[0].split("Time:")[-1].rstrip().split(" ") if a != ""
])
distances = np.asarray([
    int(a) for a in lines[1].split("Distance:")[-1].rstrip().split(" ")
    if a != ""
])

delta = np.sqrt(np.power(times, 2) - 4 * distances)
print(
    "Part 1: ",
    int(
        np.prod(
            np.ceil(0.5 * (times + delta)) - 1 - np.floor(0.5 *
                                                          (times - delta)))))

## Part 2
times = int("".join(
    [a for a in lines[0].split("Time:")[-1].rstrip().split(" ") if a != ""]))
distances = int("".join([
    a for a in lines[1].split("Distance:")[-1].rstrip().split(" ") if a != ""
]))

delta = np.sqrt(np.power(times, 2) - 4 * distances)
print(
    "Part 2: ",
    int(
        np.prod(
            np.ceil(0.5 * (times + delta)) - 1 - np.floor(0.5 *
                                                          (times - delta)))))
