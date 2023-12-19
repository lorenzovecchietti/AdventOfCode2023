input = "input.txt"
#input = "input_test.txt"

from time import perf_counter
from copy import deepcopy


def profiler(method):

  def wrapper_method(*arg, **kw):
    t = perf_counter()
    ret = method(*arg, **kw)
    print("Method " + method.__name__ + " took : " +
          "{:2.5f}".format(perf_counter() - t) + " sec")
    return ret

  return wrapper_method


@profiler
def part_1():
  accepted = 0
  instructions = {}
  with open(input, 'r') as file:
    for line in file:
      if line == "\n":
        break
      n, inst = line.rstrip().replace("}", "").split("{")
      inst = inst.split(",")
      inst = [i.split(":") for i in inst[:-1]] + [inst[-1]]
      instructions[n] = inst

    for line in file:
      current_check = "in"
      check_value = line.replace("{", "").replace("}", "").split(",")
      while current_check != "A" and current_check != "R":
        for inst in instructions[current_check]:
          if isinstance(inst, list):
            if eval(inst[0], {
                val.split("=")[0]: int(val.split("=")[1])
                for val in check_value
            }):
              current_check = inst[1]
              break
          else:
            current_check = inst
            break
      if current_check == "A":
        for val in check_value:
          accepted += int(val.split("=")[1])
  return accepted

@profiler
def part_2():
  instructions = {}
  with open(input, 'r') as file:
    for line in file:
      if line == "\n":
        break
      n, inst = line.rstrip().replace("}", "").split("{")
      inst = inst.split(",")
      inst = [i.split(":") for i in inst[:-1]] + [inst[-1]]
      instructions[n] = inst

  def combinations(current_check, ranges):
    if current_check == "R":
      return 0
    elif current_check == "A":
      return (ranges["x"][1] - ranges["x"][0] +
              1) * (ranges["m"][1] - ranges["m"][0] +
                    1) * (ranges["a"][1] - ranges["a"][0] +
                          1) * (ranges["s"][1] - ranges["s"][0] + 1)
    accepted = 0
    for inst in instructions[current_check]:
      if isinstance(inst, list):
        new_val = int(inst[0][2:])
        letter = inst[0][0]
        old_range = ranges[letter]  #x,m,a or s
        new_range = deepcopy(ranges)
        if old_range[0] < new_val < old_range[1]:
          if inst[0][1] == "<":
            new_range[letter] = (old_range[0], new_val - 1)
            ranges[letter] = (new_val, old_range[1])
          else:
            new_range[letter] = (new_val + 1, old_range[1])
            ranges[letter] = (old_range[0], new_val)
          accepted += combinations(inst[1], new_range)
      else:
        accepted += combinations(inst, ranges)
    return accepted

  ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
  return combinations("in", ranges)


a = part_1()
print("Part 1: ", a)
b = part_2()
print("Part 2: ", b)