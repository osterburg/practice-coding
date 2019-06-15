# This problem was asked by Square.
#
# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50
# (but also not 0-100 or 100-0). You do not know the bias of the coin.
#
# Write a function to simulate an unbiased coin toss.
# Note: In unbiased coin flip H or T occurs 50% of times.
import random

coin = ["Head", "Tail"]
i = random.randint(0, 1)

print(coin[i])

"""
# Biased
samples = [ random.randint(0, 1) for i in range(100) ]
heads = samples.count(1)
tails = samples.count(2)

for s in samples:
    msg = 'Heads' if s == 0 else 'Tails'
    print( msg )

print("Heads count = {}, Tails count = {}".format(heads, tails))
"""
