import random

num_runs = 1000

has_foundation_long_term_wins = 0
has_foundation_short_term_wins = 0
no_foundation_long_term_wins = 0
no_foundation_short_term_wins = 0

for i in range(num_runs):
  has_foundation = random.choice([True, False])

  holding_period = random.choice(["long-term", "short-term"])

  if has_foundation and holding_period == "long-term":
    win_prob = 0.8
  elif has_foundation and holding_period == "short-term":
    win_prob = 0.6
  elif not has_foundation and holding_period == "long-term":
    win_prob = 0.4
  else:
    win_prob = 0.2

  if random.random() < win_prob:
    if has_foundation and holding_period == "long-term":
      has_foundation_long_term_wins += 1
    elif has_foundation and holding_period == "short-term":
      has_foundation_short_term_wins += 1
    elif not has_foundation and holding_period == "long-term":
      no_foundation_long_term_wins += 1
    else:
      no_foundation_short_term_wins += 1
      
print(f"Number of simulations run: {num_runs}")
print(f"Win rate for has_foundation / long-term: {has_foundation_long_term_wins / num_runs:.2f}")
print(f"Win rate for has_foundation / short-term: {has_foundation_short_term_wins / num_runs:.2f}")
print(f"Win rate for no_foundation / long-term: {no_foundation_long_term_wins / num_runs:.2f}")
print(f"Win rate for no_foundation / short-term: {no_foundation_short_term_wins / num_runs:.2f}")
