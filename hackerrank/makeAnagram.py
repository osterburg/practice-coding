def makeAnagram(a, b):
    count = [0] * 26
    offset = ord('a') # unicode representation of a character, a = 97

    for char in a:
    	count[ord(char) - offset] += 1
    for char in b:
    	count[ord(char) - offset] -= 1

    total = 0
    for value in count:
    	total += abs(value)

    return(total)


a = 'cde'
b = 'abc'
print(makeAnagram(a, b))
