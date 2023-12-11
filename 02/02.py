import copy

color_dict = {"red": 12, "green": 13, "blue": 14}

#### Part 1 ####
print("#PART ONE")
sum_game_id = 0
with open("input.txt", "r") as f:
  for line in f:
    game_id, games = line.split(":")
    games = games.split(";")
    possible_game = True
    for game in games:
      colors = game.split(",")
      for color in colors:
        n_color, color_name = color.rstrip().lstrip().split(" ")
        if int(n_color) > color_dict[color_name]:
          possible_game = False
          break
    game_id = game_id.replace("Game ", "")
    if possible_game:
      print("Possible ", game_id, "\n", "\t", line)
      sum_game_id += int(game_id)
    else:
      print("Not Possible ", game_id, "\n", "\t", line)

print(sum_game_id)

#### Part 2 ####
print("\n\n#PART TWO")

max_color_dict = {"red": 0, "green": 0, "blue": 0}
sum_powers = 0
with open("input.txt", "r") as f:
  for line in f:
    max_color_temp = copy.deepcopy(max_color_dict)
    game_id, games = line.split(":")
    games = games.split(";")
    possible_game = True
    for game in games:
      colors = game.split(",")
      for color in colors:
        n_color, color_name = color.rstrip().lstrip().split(" ")
        max_color_temp[color_name] = max(max_color_temp[color_name],
                                         int(n_color))
    game_id = game_id.replace("Game ", "")
    print("Game ", game_id, "\n", "\t", max_color_temp)
    temp_pow = 1
    for i, v in max_color_temp.items():
      temp_pow *= int(v)
    sum_powers += temp_pow
print(sum_powers)