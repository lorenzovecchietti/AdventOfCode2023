input = "input.txt"
#input = "input_test.txt"
with open(input) as f:
  strings=f.readlines()[0].rstrip().split(",")

hash_sum=0
for s in strings:
  count_s = 0
  for ch in s:
    count_s+=ord(ch)
    count_s*=17
    count_s%=256
  hash_sum+=count_s
print("Part 1: ",hash_sum)


def hash(s):
  count_s = 0
  for ch in s:
    count_s+=ord(ch)
    count_s*=17
    count_s%=256
  return count_s


boxes = {i:[[],[]] for i in range(256)}
for s in strings:
  if s[-2]=="=":
    label, fl = s.split("=")
    box=hash(label)
    if label not in boxes[box][0]:
      boxes[box][0].append(label)
      boxes[box][1].append(fl)
    else:
      index=boxes[box][0].index(label)
      boxes[box][1][index]=fl
  else:
    label = s.split("-")[0]
    box=hash(label)
    if label in boxes[box][0]:
      index=boxes[box][0].index(label)
      boxes[box][0].pop(index)
      boxes[box][1].pop(index)

fl_sum=0
for box, lenses in boxes.items():
  for i in range(len(lenses[0])):
    fl=int(lenses[1][i])
    fl_sum+=fl*(i+1)*(box+1)

print("Part 2: ",fl_sum)