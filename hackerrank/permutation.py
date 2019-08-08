from itertools import combinations
from itertools import permutations

filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/itertools-permutations-testcases/input/input00.txt'

sample = ["HACK", 2]
mylist = sorted(list(permutations(sample[0], int(sample[1]))))
for _ in mylist:
    print(''.join(_))

print('\n')

S, number = ["ABCD", 3]
print(S, number)

for i in range(1, int(number) + 1):
    c = sorted(list(combinations(sorted(S), i)))
    for _ in c:
        print(''.join(_))
