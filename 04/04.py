print("#PART ONE")
scratches_sum = 0
with open("input.txt", "r") as f:
  for line in f:
    winning_numbers, my_numbers = line.split("|")
    my_numbers = my_numbers.rstrip().lstrip()
    my_numbers = [int(n) for n in my_numbers.split(" ") if n != '']
    winning_numbers = winning_numbers.split(":")[1].rstrip().lstrip()
    winning_numbers = [int(n) for n in winning_numbers.split(" ") if n != '']
    card_score = -1
    for n in my_numbers:
      if n in winning_numbers:
        card_score += 1
    if card_score > -1:
      card_score = 2**card_score
      scratches_sum += card_score
print(scratches_sum)

print("\n\n#PART TWO")
cards_sum = 0
cards_dict = {}
with open("input.txt", "r") as f:
  for i, line in enumerate(f.readlines()):
    i = i + 1
    if i not in cards_dict:
      cards_dict[i] = 1
    winning_numbers, my_numbers = line.split("|")
    my_numbers = my_numbers.rstrip().lstrip()
    my_numbers = [int(n) for n in my_numbers.split(" ") if n != '']
    winning_numbers = winning_numbers.split(":")[1].rstrip().lstrip()
    winning_numbers = [int(n) for n in winning_numbers.split(" ") if n != '']
    card_score = 0
    for n in my_numbers:
      if n in winning_numbers:
        card_score += 1
    for n in range(card_score):
      if i + n + 1 not in cards_dict:
        cards_dict[i + n + 1] = 1
      cards_dict[i + n + 1] += 1*cards_dict[i]

for c in cards_dict.values():
  cards_sum+=c
print(cards_sum)