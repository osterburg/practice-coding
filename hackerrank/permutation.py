from itertools import permutations

filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/itertools-permutations-testcases/input/input00.txt'

sample = ["HACK", 2]
mylist = sorted(list(permutations(sample[0], int(sample[1]))))
for _ in mylist:
    print(''.join(_))
