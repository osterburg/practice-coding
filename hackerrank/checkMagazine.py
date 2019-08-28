import os

def checkMagazine(magazine, note):
    # print(magazine, '\n', note)
    # This works but return an error if input is very long:
    # Terminated due to timeout
    for k, v in enumerate(note):
        n = note.count(v)
        m = magazine.count(v)
        if v not in magazine or n > m:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/hackerrank/ctci-ransom-note-testcases/input/input20.txt", 'r')

    mn = filename.readline().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = filename.readline().rstrip().split()
    note = filename.readline().rstrip().split()

    checkMagazine(magazine, note)
