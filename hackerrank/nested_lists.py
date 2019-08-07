filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/nested-list-testcases/input/input01.txt'

with open(filename) as f:
    lines = [line.rstrip('\n') for line in f]
    print(int(lines[0]))

mylist = []
for i in range(1, len(lines), 2):
    mylist.append([lines[i + 1], lines[i]])

mylist.sort()
mylist.reverse()
mylist.pop()
mylist.sort()

note = mylist[0][0]
for i in mylist:
    if i[0] == note:
        print(i[1])
