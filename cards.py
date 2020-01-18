import random

# initial, setting up data
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Diamonds","Hearts","Spades"]
deck = []
for r in ranks:
    for s in suits:
        deck.append(r + " of " + s)

class Randomizr:

    @staticmethod
    def random_seeds(n, min, max):
        seeds = set()
        while len(seeds) != n:
            seeds.add(random.randint(min,max))
        return list(seeds)

# 1: random cards, cards may repeat
def get_random_cards(n):
    if n is None or not isinstance(n, int) or n < 0 or n > 52:
        return None
    return [random.choice(ranks) + " of " + random.choice(suits) for ix in range(n)]

#2 random cards, cards will not repeat   
def ensure_random_cards(n):
    if n is None or not isinstance(n, int) or n < 0 or n > 52:
        return None
    seeds = Randomizr.random_seeds(n, 0, len(deck)-1)
    return [deck[ix] for ix in seeds]

print(get_random_cards(10))
print(ensure_random_cards(10))
