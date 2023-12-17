input = "input.txt"
#input = "input_test.txt"
map = []
with open(input) as f:
  for l in f:
    map.append(list(l.rstrip()))


class Beam():

  def __init__(self):
    self.pos_x = -1
    self.pos_y = 0
    self.vel_x = 1
    self.vel_y = 0

  def deflect(self, ch):
    if ch == '.':
      return None
    elif ch == '|':
      if abs(self.vel_x) == 1:
        self.vel_x = 0
        self.vel_y = 1
        new_b = Beam()
        new_b.pos_x, new_b.pos_y = self.pos_x, self.pos_y
        new_b.vel_x, new_b.vel_y = self.vel_x, -self.vel_y
        return new_b
      return None
    elif ch == "-":
      if abs(self.vel_y) == 1:
        self.vel_x = 1
        self.vel_y = 0
        new_b = Beam()
        new_b.pos_x, new_b.pos_y = self.pos_x, self.pos_y
        new_b.vel_x, new_b.vel_y = -self.vel_x, self.vel_y
        return new_b
      return None
    elif ch == "\\":
      if self.vel_y == -1:
        self.vel_x = -1
        self.vel_y = 0
      elif self.vel_y == 1:
        self.vel_x = 1
        self.vel_y = 0
      elif self.vel_x == -1:
        self.vel_x = 0
        self.vel_y = -1
      elif self.vel_x == 1:
        self.vel_x = 0
        self.vel_y = 1
      return None
    elif ch == "/":
      if self.vel_y == -1:
        self.vel_x = 1
        self.vel_y = 0
      elif self.vel_y == 1:
        self.vel_x = -1
        self.vel_y = 0
      elif self.vel_x == -1:
        self.vel_x = 0
        self.vel_y = 1
      elif self.vel_x == 1:
        self.vel_x = 0
        self.vel_y = -1
      return None

  def advance(self):
    self.pos_x += self.vel_x
    self.pos_y += self.vel_y

max_x = len(map[0])
max_y = len(map)

beams = [Beam()]
visited = set()
while beams:
  beam = beams[0]
  while True:
    beam.advance()
    print(beam.pos_x, beam.pos_y)
    check_visited = ",".join(
        [str(i) for i in [beam.pos_x, beam.pos_y, beam.vel_x, beam.vel_y]])
    if check_visited in visited or beam.pos_x >= max_x or beam.pos_y >= max_y or beam.pos_x < 0 or beam.pos_y < 0:
      beams.pop(0)
      break
    else:
      visited.add(check_visited)
    new_beam = beam.deflect(map[beam.pos_y][beam.pos_x])
    if new_beam:
      beams.append(new_beam)

visited_pos = set([(int(i.split(',')[0]), int(i.split(',')[1]))
                   for i in visited])
print("Part 1: ", len(visited_pos))


# Part 2
max_visited=-1
initial_beams=[]
for x in range(max_x):
  for y, vy in zip([-1, max_y], [1, -1]):
    initial_beam=Beam()
    initial_beam.pos_x=x
    initial_beam.pos_y=y
    initial_beam.vel_x=0
    initial_beam.vel_y=vy
    initial_beams.append(initial_beam)
for y in range(max_y):
  for x, vx in zip([-1, max_x], [1, -1]):
    initial_beam=Beam()
    initial_beam.pos_x=x
    initial_beam.pos_y=y
    initial_beam.vel_x=vx
    initial_beam.vel_y=0
    initial_beams.append(initial_beam)
    
max_visited=-1
for beam_0 in initial_beams:
  print(beam_0)
  beams = [beam_0]
  visited = set()
  while beams:
    beam = beams[0]
    while True:
      beam.advance()
      print(beam.pos_x, beam.pos_y)
      check_visited = ",".join(
          [str(i) for i in [beam.pos_x, beam.pos_y, beam.vel_x, beam.vel_y]])
      if check_visited in visited or beam.pos_x >= max_x or beam.pos_y >= max_y or beam.pos_x < 0 or beam.pos_y < 0:
        beams.pop(0)
        break
      else:
        visited.add(check_visited)
      new_beam = beam.deflect(map[beam.pos_y][beam.pos_x])
      if new_beam:
        beams.append(new_beam)

  visited_pos = set([(int(i.split(',')[0]), int(i.split(',')[1]))
                     for i in visited])
  max_visited=max(max_visited, len(visited_pos))
print("Part 2: ", max_visited)