def func_1(k, n, s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count1 = {}
    count2 = {}
    for ch in alphabet:
        count1[ch] = 0
        count2[ch] = 0
    for ch in s:
        count1[ch] += 1
    NumOfOpenGates = 0
    for ch in s:
        if count2[ch] == 0:
            if NumOfOpenGates == k:
                return 'Yes'
            NumOfOpenGates += 1
        if count2[ch] == count1[ch] - 1:
            NumOfOpenGates -= 1
        count2[ch] += 1
    return 'No'
(n, k) = map(int, raw_input().split(' '))
s = raw_input()
print(func_1(k, n, s))