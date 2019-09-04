def maximumSum(a, m):
    # r = 0
    # for i in a:
    #     t = i % m
    #     if t > r:
    #         r = t
    #
    # for i in range(len(a)-1):
    #     t = sum(a[i:]) % m
    #     if t > r:
    #         r = t
    result = 0
    min, max, k = 0, 1, 0
    for i in range(len(a)):
        for j in range(len(a)-k):
            temp = sum(a[min:max]) % m
            if temp > result:
                result = temp
            min += 1
            max += 1
        min = 0
        max = k+1
        k += 1

    return result


m = 7
a = [3, 3, 9, 9, 5]
print(maximumSum(a, m))

m = 5
a = [1, 5, 9]
print(maximumSum(a, m))  # 4
