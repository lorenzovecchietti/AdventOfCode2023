import re

print("#PART ONE")
symbol_pattern = r"[^.\d]"
numbers_pattern = r'(\d+)'
parts_sum = 0
with open("input.txt", "r") as f:
  lines = [l.rstrip().lstrip() for l in f.readlines()]
  for i, l in enumerate(lines):
    sym_matches = re.finditer(symbol_pattern, l)
    if sym_matches:
      for match in sym_matches:
        group = match.group(0)
        start_index = match.start()
        for ll in [i - 1, i + 1, i]:
          num_matches = re.finditer(numbers_pattern, lines[ll])
          for n_match in num_matches:
            n_group = n_match.group(0)
            n_start_index = n_match.start()
            n_end_index = n_match.end()
            if (start_index - 1 <= n_start_index <= start_index + 1) or (
                start_index - 1 <= n_end_index - 1 <= start_index + 1):
              string_list = list(lines[ll])
              for i in range(n_start_index, n_start_index):
                string_list[i] = "."
              lines[ll] = "".join(string_list)
              parts_sum += int(n_group)
print(parts_sum)


print("#PART TWO")
symbol_pattern = r"[^.\d]"
numbers_pattern = r'(\d+)'
gear_sum = 0
with open("input.txt", "r") as f:
  lines = [l.rstrip().lstrip() for l in f.readlines()]
  for i, l in enumerate(lines):
    sym_matches = re.finditer(symbol_pattern, l)
    if sym_matches:
      for match in sym_matches:
        group = match.group(0)
        start_index = match.start()
        num_matches_list = []
        for ll in [i - 1, i + 1, i]:
          num_matches = re.finditer(numbers_pattern, lines[ll])
          for n_match in num_matches:
            n_group = n_match.group(0)
            n_start_index = n_match.start()
            n_end_index = n_match.end()
            if (start_index - 1 <= n_start_index <= start_index + 1) or (
                start_index - 1 <= n_end_index - 1 <= start_index + 1):
              num_matches_list.append(int(n_group))
              string_list = list(lines[ll])
              for i in range(n_start_index, n_start_index):
                string_list[i] = "."
              lines[ll] = "".join(string_list)
        if len(num_matches_list)==2:
          gear_sum += num_matches_list[0]*num_matches_list[1]
          
print(gear_sum)