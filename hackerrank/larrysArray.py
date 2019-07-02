# Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array.
# He mustdetermine whether the array can be sorted using the following operation any number of times:
# * Choose any 3 consecutive indices and rotate their elements in such a way that
#     ABC -> BCA -> CAB -> ABC.
# For example, if A = {1, 6, 5, 2, 4, 3}:
#   A             rotate
#   [1,6,5,2,4,3] [6,5,2] -> [5,2,6]
#   [1,5,2,6,4,3] [5,2,6] -> [2,6,5]
#   [1,2,6,5,4,3] [5,4,3] -> [3,4,5]
#   [1,2,6,3,5,4] [6,3,5] -> [3,5,6]
#   [1,2,3,5,6,4] [5,6,4] -> [4,5,6]
#   [1,2,3,4,5,6]
#   YES
#
# ----------------------------------------
#   My way of thinking:
#   [1,6,5,2,4,3] [1,6,5] -> don't rotate
#   [1,6,5,2,4,3] [6,5,2] -> [5,2,6]
#   [1,5,2,6,4,3] [5,2,6] -> [2,6,5]
#   [1,2,6,5,4,3] [6,5,4] -> [5,4,6]
#   [1,2,5,4,6,3] [5,4,6] -> [4,6,5]
#   [1,2,4,6,5,3] [6,5,3] -> [5,3,6]
#   [1,2,4,5,3,6] [1,2,4] -> don't rotate
#   [1,2,4,5,3,6] [2,4,5] -> don't rotate
#   [1,2,4,5,3,6] [4,5,3] -> [5,3,4]
#   [1,2,5,3,4,6] [5,3,4] -> [3,4,5]
#   [1,2,3,4,5,6]
#
# ----------------------------------------
#
# On a new line for each test case, print YES if A can be fully sorted. Otherwise, print NO.
#
# Input Format
# The first line contains an integer t, the number of test cases.
# The next t pairs of lines are as follows:
#     * The first line contains an integer n, the length of A.
#     * The next line contains n space-separated integers A[i].
#
# Constraints
#     * 1 <= t <= 10
#     * 3 <= n <= 1000
#     * 1 <= A[i] <= n
#     * A(sorted) = integers incrementing by 1 from 1 to n
#
# Output Format
# For each test case, print YES if A can be fully sorted. Otherwise, print NO.
# Sample Input
# 3
# 3
# 3 1 2
# 4
# 1 3 4 2
# 5
# 1 2 3 5 4
# Sample Output
# YES
# YES
# NO
#
# Explanation
# In the explanation below, the subscript of A denotes the number of operations performed.
#
# Test Case 0:
# A0 = {3, 1, 2} -> rotate(3,1,2) -> A1 = {1, 2, 3}
# A is now sorted, so we print YES on a new line.
#
# Test Case 1:
# A0 = {1, 3, 4, 2} -> rotate(3,4,2) -> A1 = {1, 4, 2, 3}
# A1 = {1, 4, 2, 3} -> rotate(4,2,3) -> A2 = {1, 2, 3, 4}
# A is now sorted, so we print YES on a new line.
#
# Test Case 2:
# No sequence of rotations will result in a sorted A. Thus, we print NO on a new line.
def rotate(arr, a):
    s = sorted(arr[a: a + 3])
    for i in range(3):
        if arr[a] == s[0]:
            return True
        # "rotate" elements in list, ie. [1, 2, 3] -> [3, 1, 2]
        arr[a], arr[a + 1], arr[a + 2] = arr[a + 2], arr[a], arr[a + 1]
    return False


A = [1, 6, 5, 2, 4, 3]
sorted_A = sorted(A)  # To check if we can sort the list
for y in range(len(A)):  # iterate over list
    for x in range(len(A) - 2):  # iterate over list, but keep room to capture array + 2
        rotate(A, x)

print("YES" if sorted_A == A else "NO")
