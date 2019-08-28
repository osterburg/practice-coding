import os
from collections import Counter

def checkMagazine(magazine, note):
    # print(magazine, '\n', note)
    # This works but return an error if input is very long:
    # Terminated due to timeout
    # for k, v in enumerate(note):
    #     n = note.count(v)
    #     m = magazine.count(v)
    #     if v not in magazine or n > m:
    #         print('No')
    #         return
    #
    # print('Yes')
    print(magazine, '\n', note)
    x = Counter(note)
    y = Counter(magazine)

    shared_items = {k: x[k] for k in x if k in y and x[k] != y[k]}
    if len(shared_items) > 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/hackerrank/ctci-ransom-note-testcases/input/input22.txt", 'r')

    mn = filename.readline().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = filename.readline().rstrip().split()
    note = filename.readline().rstrip().split()

    checkMagazine(magazine, note)
