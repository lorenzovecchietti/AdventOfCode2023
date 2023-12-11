import bisect

filename = "input.txt"
#filename = "test_input.txt"

with open(filename, "r") as f:
  lines = f.readlines()

sorted_hands = {
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: [],
    0: [],
}

mapping = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0
}


def classify_hand(hand):
  letter_set = set(hand)
  values = []
  for letter in letter_set:
    values.append(hand.count(letter))
  if 5 in values:
    return 6
  elif 4 in values:
    return 5
  elif 3 in values and 2 in values:
    return 4
  elif 3 in values:
    return 3
  elif values.count(2) == 2:
    return 2
  elif 2 in values:
    return 1
  else:
    return 0


def insert_sorted_hand(hand, sorted_hands):
  score_string = sum(mapping[hand[0][i]] * (10**(8 - 2 * i)) for i in range(5))
  hand.append(score_string)
  bisect.insort(sorted_hands, hand, key=lambda x: x[2])
  return sorted_hands


# PART ONE
for l in lines:
  hand = l.split(" ")
  rank = classify_hand(hand[0])
  sorted_hands[rank] = insert_sorted_hand(hand, sorted_hands[rank])

total_sum = 0
index_rank = 1
for i in range(7):
  for card in sorted_hands[i]:
    total_sum += int(card[1].rstrip()) * index_rank
    index_rank += 1

print(total_sum)

# PART TWO
def value(card):
  return "J23456789TQKA".index(card)


def score(hand):
  # Count cards of each type in hand
  # This creates a sorting that favors the highest count, then the highest value
  # Five of a kind:  5
  # Four of a kind:  4 1
  # Full house:      3 2
  # Three of a kind: 3 1 1
  # Two pair:        2 2 1
  # One pair:        2 1 1 1
  # High card:       1 1 1 1 1

  counts = {}
  for card in hand:
    if card not in counts:
      counts[card] = 0
    counts[card] += 1
  return sorted(counts.values(), reverse=True)


def bestScore(hand):
  # Assuming J is a wildcard, find the best score for this hand
  cards = "23456789TQKA"
  if 'J' in hand:
    return max([bestScore(hand.replace('J', c, 1)) for c in cards])
  return score(hand)


# get best score and append tiebreaker values
def tiebreak(hand):
  sc = bestScore(hand)
  sc.extend([value(x) for x in hand])
  return sc


scored = []
for line in lines:
  hand, bid = line.split()
  scored.append((tiebreak(hand), hand, int(bid)))
scored.sort()

mul = 1
total = 0
for g in scored:
  bid = g[2]
  total += mul * bid
  mul += 1

print(total)
