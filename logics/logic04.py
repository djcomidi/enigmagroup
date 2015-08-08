# aliquot sum:
# if n = p1^a1 * p2^a2 * ... * pm^am
# then count proper divisors = (a1+1)*(a2+1)*...*(am+1)

# factor 1000 = 2 2 2 5 5 5
# so a1..am is combination of 4,4,4,1,1,1

from itertools import combinations
from functools import reduce

BILLION = 10**9
target = 10**10
POWERS = [4, 4, 4, 1, 1, 1]
PRIMES = sorted(set(combinations([2, 3, 5, 7, 11, 13, 17], 6)))
for primes in PRIMES:
    pp = list(zip(primes, POWERS))
    n = reduce(lambda a, b: a*b, [p[0]**p[1] for p in pp], 1)
    if BILLION < n < target:
        print(n, pp)
        target = n
print(target)
