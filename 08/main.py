from math import gcd

filename = "input.txt"
#filename = "test_input.txt"

with open(filename, "r") as f:
  lines = f.readlines()

rl = [1 if char == 'R' else 0 for char in lines[0].rstrip()]
path_dict = {}
for l in lines[2:]:
  path_dict.update({l.split()[0]: l.split('(')[1].split(')')[0].split(', ')})

current = "AAA"
nstep = 0
while current != "ZZZ":
  for i in range(len(rl)):
    nstep += 1
    current = path_dict[current][rl[i]]
    if current == "ZZZ":
      break

print('Part 1: ', nstep)



current_list = [k for k in path_dict.keys() if k[2] == "A"]
nsteps = []
for current in current_list:
  nstep = 0
  while current[2] != "Z":
    for i in range(len(rl)):
      nstep += 1
      current = path_dict[current][rl[i]]
      if current[2] == "Z":
        nsteps.append(nstep)
        break

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x * ans) // gcd(x, ans)
  return ans

print('Part 2: ', lcm(nsteps))