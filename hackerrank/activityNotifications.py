import math
import numpy as np

# Given the number of trailing days d and a client's total daily expenditures
# for a period of n days, find and print the number of times the client will
# receive a notification over all n days.
#
# For example, d=3 and expenditure=[10,20,30,40,50]. On the first three days,
# they just collect spending data. At day 4, we have trailing expenditures
# of [10,20,30]. The median is 20 and the day's expenditure is 40.
# Because 40>=2x20, there will be a notice. The next day, our trailing
# expenditures are [20,30,40] and the expenditures are 50. This is less than
# 2x30 so no notice will be sent. Over the period, there was one notice sent.

# def median(lst):
#     n = len(lst)
#     s = sorted(lst)
#     return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def activityNotifications(expenditure, d):
    count = 0
    for i in range((len(expenditure)-d)):
        m = np.median(expenditure[i:i+d])
        # print(expenditure[i:i+d])
        # print('median: {}'.format(m))
        # print('next : {}\n'.format(expenditure[i+d]))

        if m * 2 <= expenditure[i+d]:
            count += 1

    return count

d = 5
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(activityNotifications(expenditure, d))
