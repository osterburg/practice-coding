# Determine the number of pairs of array elements that have a difference
# equal to a target value. For example, given an array of [1, 2, 3, 4] and
# a target value of 1, we have three values meeting the condition:
# 2 -1 = 1, 3 -2 = 1, and 4 -3 = 1
#
def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] - arr[j] == k:
                count += 1

    return count


k = 2
arr = [1, 5, 3, 4, 2]
print(pairs(k, arr))  # 3
