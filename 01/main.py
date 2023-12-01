import re

#### Part 1 ####
print("#PART ONE")
b = 0
with open("input.txt", "r") as f:
  for line in f:
    i = 0
    j = 1
    a = []
    while i < len(line):
      try:
        a.append(int(line[i]))
        break
      except:
        i += 1
    while j <= len(line):
      try:
        a.append(int(line[-j]))
        break
      except:
        j += 1
    b += a[0] * 10 + a[1]

print(b)

#### Part 2 ####
print("\n#PART TWO")
dict_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}
max_len = sorted([len(i) for i in dict_nums.keys()])[-1]
pattern = r'(?:' + '|'.join(re.escape(word)
                            for word in dict_nums.keys()) + r'|\d)'

b = 0
with open("input.txt", "r") as f:
  for line in f:
    nums = []
    for i in range(2):
      matches = re.finditer(pattern, line)
      for match in matches:
        matched_text = match.group()
        start_index = match.start()
        ch = dict_nums.get(matched_text, matched_text)
        if i == 1:
          nums.append(ch)
        else:
          line = line[:start_index] + str(ch) + line[start_index + 1:]
    b += 10 * int(nums[0]) + int(nums[-1])

print(b)
