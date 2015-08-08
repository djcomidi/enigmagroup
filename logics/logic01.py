from itertools import permutations

nBreads = 3
nMeats = 4

cheeses = set()
for p in permutations('000ASGC', r=2):
    cheeses.add(''.join(sorted(p)))
nCheeses = len(cheeses)

toppings = set()
for p in permutations('000ABCDEFGH', r=3):
    toppings.add(''.join(sorted(p)))
nToppings = len(toppings)

print(nBreads * nMeats * nCheeses * nToppings)
