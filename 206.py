#   _____ _____ _____
#  |   | |__   |   | | ProjectEuler/206.py
#  | | | |   __| | | | Nikolai Nymo
#  |_|___|_____|_|___| 24-09-18

# Find the unique positive integer whose square has the form 
# 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

from math import sqrt, ceil, log

smallestForm = 1020304050607080900
largestForm  = 1929394959697989990
formList     = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 0]
start = int(ceil(sqrt(smallestForm)))
end   = int(ceil(sqrt(largestForm)))
print('Checking ' + str(start) + ' to ' + str(end) + ' = ' + str(end-start) + ' combinations.')

sampleRange = range(start, end)
for j in sampleRange:
    try:
        sample = j*j
        sampleList = [(sample//(10**i))%10 for i in range(ceil(log(sample, 10))-1, -1, -1)]

        for k in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
            if sampleList[k] is formList[k]:
                if k is 18:
                    print(j)
            else:
                break
    except KeyboardInterrupt:
        print(j)
        break


# Returns 1389019170 after like three hours.