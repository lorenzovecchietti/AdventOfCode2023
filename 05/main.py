lines_dict = {
    "seed-to-soil map:\n": [],
    "soil-to-fertilizer map:\n": [],
    "fertilizer-to-water map:\n": [],
    "water-to-light map:\n": [],
    "light-to-temperature map:\n": [],
    "temperature-to-humidity map:\n": [],
    "humidity-to-location map:\n": []
}

filename = "input.txt"
#filename = "test_input.txt"

with open(filename, "r") as f:
  lines = f.readlines()

lengths = [lines.index(k) for k in lines_dict.keys()] + [len(lines)]
for i, k in enumerate(lines_dict.keys()):
  lines_dict[k].append(lengths[i])
  lines_dict[k].append(lengths[i + 1])

seeds = [int(n) for n in lines[0].split(": ")[1].split(" ")]

lines_index = list(lines_dict.values())

print("#PART ONE")
min_loc = 1e10
for seed in seeds:
  print(seed)
  current_nb = seed
  for i in range(len(lines_index)):
    for j in range(lines_index[i][0] + 1, lines_index[i][1] - 1):
      destination, source, len_range = [int(i) for i in lines[j].split(" ")]
      if current_nb in range(source, source + len_range):
        current_nb = destination + (current_nb - source)
        break
    print("\t", current_nb)
  min_loc = min(current_nb, min_loc)
print(min_loc)

print("\n\n#PART TWO")

maps = []
for i in range(len(lines_index)):
  maps.append([])
  for j in range(lines_index[i][0] + 1, lines_index[i][1] - 1):
    destination, source, len_range = [int(i) for i in lines[j].split(" ")]
    maps[i].append([destination, source, len_range])


def map_ranges(ranges, maps):
  out_ranges = []
  for i, map in enumerate(maps):
    print("**", i, map)
    new_ranges = []
    for range in ranges:
      if map[1] <= range[0] and range[1] <= map[1] + map[2]:
        out_ranges.append(
            (map[0] + (range[0] - map[1]), map[0] + range[1] - range[0]))
      elif range[1] <= map[1] + map[2]:
        out_ranges.append((map[0], map[0] + range[1] - range[0]))
        new_ranges.append((range[0], map[1]))
      elif map[1] <= range[0]:
        out_ranges.append((map[0] + (range[0] - map[1]), map[0] + map[2]))
        new_ranges.append((map[1] + map[2], range[1]))
    #print(out_ranges)
    #print(new_ranges)
    print("===========")
    range = new_ranges
  if ranges:
    [out_ranges.append(r) for r in ranges]
  return out_ranges


min_loc = 1e10
seed_group = 0
for seed_start, seed_end in zip(seeds[::2], seeds[1::2]):
  seed_group += 1
  print(seed_group)
  ranges = [(seed_start, seed_end)]
  for i in range(len(lines_index)):
    ranges = map_ranges(ranges, maps[i])
    print(i)
  for r in ranges:
    min_loc = min(r[0], min_loc)
print(min_loc)

import numpy as np

lines = []
with open("input.txt", "r") as f:
  for line in f:
    lines.append(line.strip())
# lines = [l for l in lines if l != '']
seeds = [int(s) for s in lines[0].split()[1:]]

maps = []
for line in lines[2:]:
  if 'map' in line:
    maps.append([])
  elif line != '':
    maps[-1].append([int(l) for l in line.split()])


def resolve_map(map, index):
  for entry in map:
    if index >= entry[1] and index < (entry[1] + entry[2]):
      return index - entry[1] + entry[0]
  return index


def resolve_map_reverse(map, index):
  for entry in map:
    if index >= entry[0] and index < (entry[0] + entry[2]):
      return index - entry[0] + entry[1]
  return index


result = []
for seed in seeds:
  for map in maps:
    seed = resolve_map(map, seed)
  result.append(seed)
print(f"Part 1: {np.min(result)}")

from tqdm import trange

maps.reverse()
for i in trange(0, 100000000, 1000):
  seed = i
  for map in maps:
    seed = resolve_map_reverse(map, seed)
  for seeed, rang in np.array(seeds).reshape((-1, 2)):
    if seed >= seeed and seed < seeed + rang:
      iter_1 = i
      print(f"Part 2: {i} iteration 1")
      break
  else:
    continue
  break

for i in trange(iter_1 - 1000, iter_1 + 1):
  seed = i
  for map in maps:
    seed = resolve_map_reverse(map, seed)
  for seeed, rang in np.array(seeds).reshape((-1, 2)):
    if seed >= seeed and seed < seeed + rang:
      print(f"Part 2: {i}")
      break
  else:
    continue
  break
